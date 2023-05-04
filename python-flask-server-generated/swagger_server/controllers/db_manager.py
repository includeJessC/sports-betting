import json
import os
import uuid

import jwt
import psycopg2

import __main__ as mmm
from swagger_server.controllers.parser import parse_competition, parse_match
from swagger_server.models.bets_result import BetsResult  # noqa: E501
from swagger_server.models.competition import Competition  # noqa: E501
from swagger_server.models.match import Match  # noqa: E501

passkey = os.environ.get("PASS_KEY")
username = os.environ.get("DB_USER")
db_name = os.environ.get("DB_NAME")
us_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")


def update_competition(competition_id, url):
    res = parse_competition(url)
    db = DataBaseManagemantSystem()
    db.update_competition(competition_id, res)


def update_match(competition_id, url):
    res = parse_match(url)
    db = DataBaseManagemantSystem()
    db.update_match(competition_id, res)


class DataBaseManagemantSystem:
    def __init__(self):
        self.con = psycopg2.connect(
            database=db_name,
            user=username,
            password=us_password,
            host=db_host,
        )
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def add_new_user(self, id, name, surname, password):
        cur = self.con.cursor()
        request = "INSERT INTO sport_betting.users_info (id, name, surname) VALUES ('" + str(
            jwt.encode({"id": id}, passkey, algorithm="HS256")) + "', '" + str(
            name) + "', '" + str(surname) + "') ON CONFLICT DO NOTHING;"
        cur.execute(request)
        self.con.commit()
        cur = self.con.cursor()
        request = "INSERT INTO sport_betting.private_users_info (id, password) VALUES ('" + str(
            jwt.encode({"id": id}, passkey, algorithm="HS256")) + "', '" + str(
            password) + "') ON CONFLICT DO NOTHING;"
        cur.execute(request)
        self.con.commit()

    def get_user_info(self, username):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.private_users_info WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}' AND approved = true"
        cur.execute(request)
        private_info = cur.fetchone()
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.users_info WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}'"
        cur.execute(request)
        info = cur.fetchone()
        return {"password": private_info[1], "name": info[1], "surname": info[2]}

    def get_user_token(self, username):
        cur = self.con.cursor()
        request = f"DELETE FROM sport_betting.login_token WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}'"
        cur.execute(request)
        self.con.commit()
        cur = self.con.cursor()
        token = uuid.uuid4()
        request = f"INSERT INTO sport_betting.login_token (id, token) VALUES ('{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}', '{token}')"
        cur.execute(request)
        self.con.commit()
        return token

    def check_registered(self, username):
        cur = self.con.cursor()
        request = f"SELECT COUNT(*) FROM sport_betting.private_users_info WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}' AND approved = true"
        cur.execute(request)
        return cur.fetchone()[0] != 0

    def check_registeration_approve(self, username, code):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.codes WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}' AND created_at = (SELECT MAX(created_at) FROM sport_betting.codes WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}')"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is not None:
            return ans[2] == code
        return False

    def update_approved_info(self, username):
        cur = self.con.cursor()
        request = f"UPDATE sport_betting.private_users_info SET approved = true WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}'"
        cur.execute(request)
        self.con.commit()

    def add_user_to_competition(self, competition_id, username):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.competition_bets WHERE special_id='{competition_id}' AND user_id='{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}'"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is not None:
            raise Exception()
        request = f"INSERT INTO sport_betting.competition_bets (competition_id, user_id, result) VALUES ('{competition_id}', '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}', NULL)"
        cur.execute(request)
        self.con.commit()

    def add_competition(self, username, competition):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.competitions_info WHERE created_by = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}' AND id='{competition['competition_id']}'"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is not None:
            raise Exception()
        special_id = str(uuid.uuid4())
        if competition['parsing_ref'] is not None:
            request = f"INSERT INTO sport_betting.competitions_info (created_by, id, name, is_active, parsing_ref, special_id) VALUES ('{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}', '{competition['competition_id']}', '{competition['name']}', {competition['is_active']}, '{competition['parsing_ref']}', '{special_id}')"
        else:
            request = f"INSERT INTO sport_betting.competitions_info (created_by, id, name, is_active, special_id) VALUES ('{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}', '{competition['competition_id']}', '{competition['name']}', {competition['is_active']}, '{special_id}')"
        cur.execute(request)
        cur = self.con.cursor()
        for match in competition['ended_matches']:
            if match['team1_name'] is None:
                continue
            if match['end_time'] is None:
                request = f"INSERT INTO sport_betting.matches_info (competition_id, id, name, is_active, parsing_ref, start_time, first_team_name, second_team_name, first_team_result, second_team_result) VALUES ('{special_id}', '{match['id']}', '{match['name']}', {match['is_active']}, '{match['parsing_ref']}', '{match['start_time']}', '{match['team1_name']}', '{match['team2_name']}', {match['team1_res']}, {match['team2_res']})"
            else:
                request = f"INSERT INTO sport_betting.matches_info (competition_id, id, name, is_active, parsing_ref, start_time, end_time, first_team_name, second_team_name, first_team_result, second_team_result) VALUES ('{special_id}', '{match['id']}', '{match['name']}', {match['is_active']}, '{match['parsing_ref']}', '{match['start_time']}', '{match['end_time']}', '{match['team1_name']}', '{match['team2_name']}', {match['team1_res']}, {match['team2_res']})"
            cur.execute(request)
        cur = self.con.cursor()
        for match in competition['not_ended_matches']:
            if match['team1_name'] is None:
                continue
            request = f"INSERT INTO sport_betting.matches_info (competition_id, id, name, is_active, parsing_ref, start_time, first_team_name, second_team_name) VALUES ('{special_id}', '{match['id']}', '{match['name']}', {match['is_active']}, '{match['parsing_ref']}', '{match['start_time']}', '{match['team1_name']}', '{match['team2_name']}')"
            cur.execute(request)
        cur = self.con.cursor()
        request = f"INSERT INTO sport_betting.competition_bets (competition_id, user_id, result) VALUES ('{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}', NULL)"
        cur.execute(request)
        self.con.commit()
        if competition['parsing_ref'] is not None:
            mmm.scheduler.add_job(update_competition, 'interval', hours=1,
                                  args=(special_id, competition['parsing_ref']),
                                  id=special_id)
        return special_id

    def add_match(self, username, competition_id, match, special_bets):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.competitions_info WHERE created_by = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}' AND special_id='{competition_id}'"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is None:
            raise Exception()
        if match['parsing_ref'] is not None:
            request = f"INSERT INTO sport_betting.matches_info (competition_id, id, name, is_active, start_time, first_team_name, second_team_name, parsing_ref) VALUES ('{competition_id}', '{match['id']}', '{match['name']}', {match['is_active']}, '{match['start_time']}', '{match['team1_name']}', '{match['team2_name']}', '{match['parsing_ref']}')"
        else:
            request = f"INSERT INTO sport_betting.matches_info (competition_id, id, name, is_active, start_time, first_team_name, second_team_name) VALUES ('{competition_id}', '{match['id']}', '{match['name']}', {match['is_active']}, '{match['start_time']}', '{match['team1_name']}', '{match['team2_name']}')"
        cur.execute(request)
        self.con.commit()
        special_bets = [] if special_bets is None else special_bets
        for bet in special_bets:
            request = f"INSERT INTO sport_betting.special_created_bets (match_id, bet_name, competition_id) VALUES ('{match['id']}', '{bet}', '{competition_id}')"
            cur.execute(request)
            self.con.commit()
        if match['parsing_ref'] is not None:
            mmm.scheduler.add_job(update_match, 'interval', hours=1, args=(competition_id, match['parsing_ref']),
                                  id=f"{competition_id}_{match['parsing_ref']}")

    def update_match(self, competition_id, match):
        cur = self.con.cursor()
        if match['end_time'] is None:
            request = f"UPDATE sport_betting.matches_info SET is_active={match['is_active']}, start_time='{match['start_time']}', first_team_result={match['team1_res']}, second_team_result={match['team2_res']}) WHERE competition_id='{competition_id}' and id='{match['id']}' RETURNING is_active"
        else:
            request = f"UPDATE sport_betting.matches_info SET is_active={match['is_active']}, start_time='{match['start_time']}', end_time='{match['end_time']}', first_team_result={match['team1_res']}, second_team_result={match['team2_res']}) WHERE competition_id='{competition_id}' and id='{match['id']}' RETURNING is_active"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is not None and not ans[0]:
            self.update_bets_result(competition_id, match)
            mmm.scheduler.remove_job(job_id=f"{competition_id}_{match['id']}")
        self.con.commit()

    def get_competition(self, competition_id):
        cur = self.con.cursor()
        request = f"SELECT name, is_active, special_id, created_by FROM sport_betting.competitions_info WHERE special_id='{competition_id}'"
        cur.execute(request)
        ans_competition = cur.fetchone()
        if ans_competition is None:
            raise Exception()
        request = f"SELECT DISTINCT id FROM sport_betting.matches_info WHERE competition_id='{competition_id}'"
        cur.execute(request)
        ans_matches = cur.fetchall()
        request = f"SELECT user_id, result FROM sport_betting.competition_bets WHERE competition_id='{competition_id}'"
        cur.execute(request)
        ans_bets = cur.fetchall()
        matches = []
        leader_board = []
        for match_id in ans_matches:
            matches.append(self.get_match_info(match_id[0], competition_id, None))
        for bet in ans_bets:
            leader_board.append(BetsResult(jwt.decode(bet[0], passkey, algorithms=["HS256"])['id'], bet[1]))
        return Competition(ans_competition[0], ans_competition[2], ans_competition[1], matches, leader_board,
                           jwt.decode(ans_competition[3], passkey, algorithms=["HS256"])['id'])

    def get_all_competitions(self, username):
        cur = self.con.cursor()
        request = f"SELECT DISTINCT competition_id FROM sport_betting.competition_bets WHERE user_id='{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}'"
        cur.execute(request)
        ans_bets = cur.fetchall()
        competitions = []
        for info in ans_bets:
            competitions.append(self.get_competition(info[0]))
        return competitions

    def update_bets_result(self, competition_id, match):
        cur = self.con.cursor()
        request = f"SELECT DISTINCT user_id FROM sport_betting.match_bets WHERE match_id='{match['id']}' and competition_id='{competition_id}'"
        cur.execute(request)
        users = cur.fetchall()
        users_bets = []
        for user in users:
            request = f"SELECT bets from sport_betting.match_bets WHERE match_id='{match['id']}' AND competition_id='{competition_id}' AND user_id='{user[0]}'"
            cur.execute(request)
            ans = cur.fetchone()
            bets_json = json.loads(ans[0])
            user_bet_1 = 0
            user_bet_2 = 0
            for bet in bets_json['bets']:
                if bet['name'] == 'first_team_result':
                    user_bet_1 = bet['bet']
                if bet['name'] == 'second_team_result':
                    user_bet_2 = bet['bet']
            users_bets.append([user_bet_1, user_bet_2, user[0], 0, 0, 0])
        coefs = [0., 0., 0.]
        for item in users_bets:
            if (match['team1_res'] - match['team2_res'] >= 0 and item[0] - item[1] >= 0) or (
                    match['team1_res'] - match['team2_res'] < 0 and item[0] - item[1] < 0):
                coefs[0] += 1
                item[3] = 10
            if (match['team1_res'] - match['team2_res'] == item[0] - item[1]) or (
                    match['team1_res'] - match['team2_res'] == item[0] - item[1]):
                coefs[1] += 1
                item[4] = 10
            if match['team1_res'] - match['team2_res'] == item[0] - item[1]:
                coefs[2] += 1
                item[5] = 10
        for i in (0, 3):
            coefs[i] = (len(users_bets) - coefs[i]) / len(users_bets)
        for item in users_bets:
            request = f"UPDATE sport_betting.match_bets SET result={item[3] * coefs[0] + item[4] * coefs[1] + item[5] * coefs[2]} WHERE match_id='{match['id']}' AND competition_id='{competition_id}' AND user_id='{item[2]}'"
            cur.execute(request)
            self.con.commit()
            cur = self.con.cursor()
            request = f"UPDATE sport_betting.competition_bets SET result=(SELECT SUM(result) FROM sport_betting.match_bets WHERE user_id='{item[2]}') WHERE competition_id='{competition_id}' AND user_id='{item[2]}'"
            cur.execute(request)
            self.con.commit()

    def update_competition(self, competition_id, competition):
        cur = self.con.cursor()
        request = f"SELECT special_id FROM sport_betting.competitions_info WHERE special_id = '{competition_id}'"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is None:
            raise Exception()
        request = f"UPDATE sport_betting.competitions_info SET is_active={competition['is_active']} WHERE special_id='{ans[0]}' RETURNING is_active"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is not None and not ans[0]:
            mmm.scheduler.remove_job(job_id=competition_id)
        cur = self.con.cursor()
        for match in competition['ended_matches']:
            if match['end_time'] is None:
                request = f"UPDATE sport_betting.matches_info SET is_active={match['is_active']}, start_time='{match['start_time']}', first_team_result={match['team1_res']}, second_team_result={match['team2_res']}) WHERE competition_id='{competition_id}' and id='{match['id']}' RETURNING is_active"
            else:
                request = f"UPDATE sport_betting.matches_info SET is_active={match['is_active']}, start_time='{match['start_time']}', end_time='{match['end_time']}', first_team_result={match['team1_res']}, second_team_result={match['team2_res']}) WHERE competition_id='{competition_id}' and id='{match['id']}' RETURNING is_active"
            cur.execute(request)
            ans = cur.fetchone()
            if ans is not None and not ans[0]:
                self.update_bets_result(competition_id, match)
        cur = self.con.cursor()
        for match in competition['not_ended_matches']:
            if match['team1_name'] is None:
                continue
            request = f"INSERT INTO sport_betting.matches_info (competition_id, id, name, is_active, parsing_ref, start_time, first_team_name, second_team_name) VALUES ('{competition_id}', '{match['id']}', '{match['name']}', {match['is_active']}, '{match['parsing_ref']}', '{match['start_time']}', '{match['team1_name']}', '{match['team2_name']}') ON CONFLICT (id, competition_id) DO UPDATE SET is_active={match['is_active']}, start_time='{match['start_time']}'"
            cur.execute(request)
        self.con.commit()

    def get_competition_by_match_id(self, competition_id):
        cur = self.con.cursor()
        request = f"SELECT parsing_ref, special_id FROM sport_betting.competitions_info WHERE special_id = '{competition_id}'"
        cur.execute(request)
        ans = cur.fetchone()
        return {'parsing_ref': ans[0], 'special_id': ans[1]}

    def get_match_parsing_ref(self, competition_id, match_id):
        cur = self.con.cursor()
        request = f"SELECT parsing_ref, competition_id FROM sport_betting.matches_info WHERE competition_id = '{competition_id}' and id = '{match_id}'"
        cur.execute(request)
        ans = cur.fetchone()
        return {'parsing_ref': ans[0], 'special_id': ans[1]}

    def check_if_match_active(self, match_id, competition_id):
        cur = self.con.cursor()
        request = f"SELECT is_active FROM sport_betting.matches_info WHERE id = '{match_id}' AND competition_id = '{competition_id}'"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is None or not ans[0]:
            raise Exception()

    def add_bets_to_match(self, match_id, competition_id, username, bets):
        cur = self.con.cursor()
        request = f"INSERT INTO sport_betting.match_bets (match_id, competition_id, user_id, bets) VALUES ('{match_id}', '{competition_id}', '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}', '{json.dumps(bets)}'::json)"
        cur.execute(request)
        self.con.commit()

    def get_match_info(self, match_id, competition_id, username):
        cur = self.con.cursor()
        request = f"SELECT first_team_name, second_team_name, first_team_result, second_team_result, start_time, is_active, name, id FROM sport_betting.matches_info WHERE id='{match_id}' and competition_id='{competition_id}'"
        cur.execute(request)
        ans1 = cur.fetchone()
        cur = self.con.cursor()
        ans2 = None
        if username is not None:
            request = f"SELECT bets, result FROM sport_betting.match_bets WHERE match_id='{match_id}' and competition_id='{competition_id}' and user_id='{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}'"
            cur.execute(request)
            ans2 = cur.fetchone()
        request = f"SELECT bet_name FROM sport_betting.special_created_bets WHERE match_id='{match_id}' and competition_id='{competition_id}'"
        cur.execute(request)
        ans3 = cur.fetchall()
        special_bets = []
        for b in ans3:
            special_bets.append(b[0])
        return Match(match_id, ans1[6], ans1[0], ans1[1], ans1[2], ans1[3], ans1[5],
                     ans2[1] if ans2 is not None else None, ans2[0] if ans2 is not None else None, ans1[4],
                     special_bets)
