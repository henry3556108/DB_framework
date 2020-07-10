import sqlite3
import cv2
import os
import numpy as np
import random


class DBCreater():
    def __init__(self, db_name: str):
        # init DB
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.init()

    def init(self):
        try:
            # initialize structure in your DB
            self.conn.execute("""
            """)
            print("db create")
        except:
            print("db already exist")

    def id_generator(self, id_col: str) -> int:
        # ID generator
        self.fetch(f"SELECT {id_col} FROM some_table")
        id = int(random.randint(1, 99999999))
        db_exist_id = list(zip(*self.cur.fetchall()))

        # check duplicate or empty
        if len(db_exist_id) == 0:
            return id
        while id in db_exist_id[0]:
            id = int(random.randint(1, 99999999))
        return id

    def insert(self, command:   str, data: list) -> None:
        try:
            if command == "":
                # check wheather file is exist
                # .....
                # generate ID primary key
                data["id"] = self.id_generator("id")

                # insert data in DB
                self.conn.execute("")

            self.conn.commit()
        except:
            print(f"something wrong when insert {command}")

    def fetch(self, sql: str) -> None:
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except:
            print("something wrong in your sql command or database")

    def commit(self, sql: str):
        try:
            self.conn.execute(sql)
            self.conn.commit()
        except:
            print("something wrong in your sql command or database")


def data_hanlder() -> list:
    """
    need the folder data in the path
    """
    data = []
    category_name = os.listdir("data")
    # data parser
    return data


def main():
    db_name = "test.sqlite"
    creater = DBCreater(db_name)
    datas = data_hanlder()
    for data in datas:
        creater.insert("images", data)

    data = creater.fetch("SQL syntax")


if __name__ == "__main__":
    main()
