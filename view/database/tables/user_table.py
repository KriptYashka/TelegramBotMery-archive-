import datetime
import telebot
from view.database.base import DB
from view.database.db_setting import *


class UserDB(DB):
    table_name = "users"

    def __init__(self):
        super().__init__(db_name)

    def init_table(self):
        """
        Создает таблицу пользователей
        """
        request = """CREATE TABLE IF NOT EXISTS {} (
                id INT PRIMARY KEY,
                tg_id INT,
                profile_id INT
                );""".format(self.table_name)
        self.cursor.execute(request)

    def is_exist(self, user_id: int):
        obj = self.select(self.table_name, "id", user_id)
        return len(obj)

    def add_user(self, user: telebot.types.User, status="common"):
        data = [
            user.id, datetime.datetime.now().isoformat(), status
        ]
        self.insert(self.table_name, data)

    def delete_user(self, user_id: int):
        self.delete(self.table_name, "id", user_id)
