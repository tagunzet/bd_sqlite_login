import sqlite3

##########################################################################################
##Базы данных#############################################################################
##########################################################################################
##########################################################################################

class Connect:

    # конструктор
    def __init__(self, name):
        self.name = name  # устанавливаем имя

    def connect_to_bd(self):
        print("подключение", self.name)
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()
        conn.commit()

import random
import string
login = random.random()
password = random.random()
class Create:
    def __init__(self, name):
        self.name = name

    def randomString(self,stringLength):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))

    def create_db(self, name_bd):
        print(self.name)
        print(self.randomString(8))
        conn = sqlite3.connect("base.db")  # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        cursor.execute("""CREATE TABLE """ +name_bd+
                          """(login text, password text)""")
        conn.commit()
        sql2zap = """INSERT INTO """ +name_bd+ """ VALUES ("""+"""" """ +self.randomString(8)+ """",""" +""" " """ +self.randomString(8)+""" ")                 
                    """
        print(sql2zap)
        cursor2.execute(sql2zap)
        conn.commit()


class Check_database:


    # конструктор
    def __init__(self, name):
        self.name = name  # устанавливаем имя

    def checker_bd(self,name_bdd):
        print(self.name)
        try:
            conn = sqlite3.connect("base.db")
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM """ +name_bdd+
                          """;
                       """)
            conn.commit()

        except sqlite3.OperationalError:
            print('Такой таблицы нету в базе , возможно создать ')