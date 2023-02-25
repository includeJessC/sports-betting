import json

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
        request = "INSERT INTO sport_betting.users_info (id, name, surname) VALUES ('" + str(id) + "', '" + str(name) + "', '" + str(surname) + "') ON CONFLICT DO NOTHING;"
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

