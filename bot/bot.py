import hashlib
import os
import uuid

import psycopg2
import telebot
import jwt

passkey = os.environ.get("PASS_KEY")

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
BOT = telebot.TeleBot(TOKEN, parse_mode=None)
username = os.environ.get("DB_USER")
db_name = os.environ.get("DB_NAME")
us_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")

class DataBaseManagemantSystemBot:
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

    def check_registered(self, username):
        cur = self.con.cursor()
        request = f"SELECT COUNT(*) FROM sport_betting.private_users_info WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}' and approved=True"
        cur.execute(request)
        return cur.fetchone()[0] != 0

    def check_has_code_or_insert(self, username):
        cur = self.con.cursor()
        request = f"SELECT * FROM sport_betting.codes WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}' AND created_at = (SELECT MAX(created_at) FROM sport_betting.codes WHERE id = '{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}')"
        cur.execute(request)
        ans = cur.fetchone()
        if ans is not None and len(ans) != 0:
            return ans[2]
        code = str(uuid.uuid4())
        request = f"INSERT INTO sport_betting.codes (id, secret_code) VALUES ('{str(jwt.encode({'id': username}, passkey, algorithm='HS256'))}', '{code}')"
        cur.execute(request)
        self.con.commit()
        return code

    def update_password(self, name, password):
        cur = self.con.cursor()
        request = f"UPDATE sport_betting.private_users_info SET password = '{password}' WHERE id='{str(jwt.encode({'id': name}, passkey, algorithm='HS256'))}'"
        cur.execute(request)
        self.con.commit()


@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    info about commands
    """
    BOT.reply_to(message,
                 'Мои команды: \n /get_code - выдаст код для регистрации, /get_password - поможет восстановить пароль')


@BOT.message_handler(commands=['get_code'])
def send_code(message):
    """
    gives the code to registration or error
    """
    db = DataBaseManagemantSystemBot()
    try:
        if db.check_registered(message.from_user.username):
            BOT.reply_to(message,
                         'Вы уже зарегистрированы')
            return
        BOT.reply_to(message,
                     f'Введите код регистрации на странице: {db.check_has_code_or_insert(message.from_user.username)}')
    except Exception:
        BOT.reply_to(message,
                     f'Что-то пошло нет: проверьте правильность введенного ника на сайте')


def get_password(message):
    db = DataBaseManagemantSystemBot()
    command = str(hashlib.sha256(message.text.encode()).hexdigest())
    db.update_password(message.from_user.username, command)
    BOT.reply_to(message, 'Ваш пароль обновлен')


@BOT.message_handler(commands=['get_password'])
def send_password(message):
    """
    gives the code to registration or error
    """
    db = DataBaseManagemantSystemBot()
    try:
        if db.check_registered(message.from_user.username):
            BOT.reply_to(message, f'Придумайте новый пароль: ')
            BOT.register_next_step_handler(message, get_password)
            return
    except Exception:
        BOT.reply_to(message,
                     f'Что-то пошло нет: проверьте правильность введенного ника на сайте')
    BOT.reply_to(message,
                 f'Что-то пошло нет: проверьте правильность введенного ника на сайте')


if __name__ == '__main__':
    BOT.infinity_polling()
