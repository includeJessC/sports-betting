import psycopg2
import json


class DataBaseManagemantSystem:
    def __init__(self):
        self.con = psycopg2.connect(
            database="sports_betting",
            user="root",
            host=""
        )
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()
