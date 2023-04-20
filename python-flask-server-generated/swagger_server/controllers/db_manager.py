import uuid

import psycopg2


class DataBaseManagemantSystem:
    def __init__(self):
        self.con = psycopg2.connect(
            database="postgres",
            user="aabogacheva",
            password="Stack_073A",
        )
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def add_new_user(self, id, name, surname, password):
        cur = self.con.cursor()
        request = "INSERT INTO sport_betting.users_info (id, name, surname) VALUES ('" + str(id) + "', '" + str(
            name) + "', '" + str(surname) + "') ON CONFLICT DO NOTHING;"
        cur.execute(request)
        self.con.commit()
        cur = self.con.cursor()
        request = "INSERT INTO sport_betting.private_users_info (id, password) VALUES ('" + str(id) + "', '" + str(
            password) + "') ON CONFLICT DO NOTHING;"
        cur.execute(request)
        self.con.commit()

    def get_user_info(self, username):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.private_users_info WHERE id = '{username}' AND approved = true"
        cur.execute(request)
        private_info = cur.fetchone()
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.users_info WHERE id = '{username}'"
        cur.execute(request)
        info = cur.fetchone()
        return {"password": private_info[1], "name": info[1], "surname": info[2]}

    def get_user_token(self, username):
        cur = self.con.cursor()
        request = f"DELETE FROM sport_betting.login_token WHERE id = '{username}'"
        cur.execute(request)
        self.con.commit()
        cur = self.con.cursor()
        token = uuid.uuid4()
        request = f"INSERT INTO sport_betting.login_token (id, token) VALUES ('{username}', '{token}')"
        cur.execute(request)
        self.con.commit()
        return token

    def check_registered(self, username):
        cur = self.con.cursor()
        request = f"SELECT COUNT(*) FROM sport_betting.private_users_info WHERE id = '{username}' AND approved = true"
        cur.execute(request)
        return cur.fetchone()[0] != 0

    def check_registeration_approve(self, username, code):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.codes WHERE id = '{username}' AND created_at = (SELECT MAX(created_at) FROM sport_betting.codes WHERE id = '{username}')"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is not None:
            return ans[2] == code
        return False

    def update_approved_info(self, username):
        cur = self.con.cursor()
        request = f"UPDATE sport_betting.private_users_info SET approved = true WHERE id = '{username}'"
        cur.execute(request)
        self.con.commit()

    def add_competition(self, username, competition):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.competitions_info WHERE created_by = '{username}' AND id='{competition['competition_id']}'"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is not None:
            raise Exception()
        request = f"INSERT INTO sport_betting.competitions_info (created_by, id, name, is_active, parsing_ref) VALUES ('{username}', '{competition['competition_id']}', '{competition['name']}', {competition['is_active']}, '{competition['parsing_ref']}')"
        cur.execute(request)
        cur = self.con.cursor()
        for match in competition['ended_matches']:
            print("PLUMBUS")
            request = f"INSERT INTO sport_betting.matches_info (competition_id, id, name, is_active, parsing_ref, start_time, end_time, first_team_name, second_team_name, first_team_result, second_team_result) VALUES ('{competition['competition_id']}', '{match['id']}' '{match['name']}', {match['is_active']}, '{match['parsing_ref']}', {match['start_time']}, {match['end_time']}, '{match['team1_name']}', '{match['team2_name']}', '{match['team1_res']}', '{match['team2_res']}')"
            cur.execute(request)
        cur = self.con.cursor()
        for match in competition['not_ended_matches']:
            request = f"INSERT INTO sport_betting.matches_info (competition_id, id, name, is_active, parsing_ref, start_time, end_time, first_team_name, second_team_name, first_team_result, second_team_result) VALUES ('{competition['competition_id']}', '{match['id']}' '{match['name']}', {match['is_active']}, '{match['parsing_ref']}', {match['start_time']}, {match['end_time']}, '{match['team1_name']}', '{match['team2_name']}', '{match['team1_res']}', '{match['team2_res']}')"
            cur.execute(request)
        self.con.commit()

