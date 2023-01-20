import psycopg2
import json


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

    def add_new_user(self, id, name, surname):
        cur = self.con.cursor()
        request = "INSERT INTO sport_betting.users_info (id, name, surname) VALUES ('" + str(id) + "', '" + str(name) + "', '" + str(surname) + "');"
        cur.execute(request)
        self.con.commit()


if __name__ == '__main__':
    DataBaseManagemantSystem().add_new_user('123', 'Ann', 'Nokia')

