import sqlite3
from models.menu import Menu

class Databasemanager:

    def __init__(self, db_path) -> None:
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()


    def __insert_data(self, sql, data):

        self.cursor.execute(sql, data)
        self.conn.commit()

        print("Succesfully !!")


    def __select_data(self, sql):

        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return result

    def add_food(self, data):
        sql_insert = """INSERT INTO food(Pizza, Price, Ingeridients) VALUES(?,?)"""
        self.__insert_data(sql_insert, data)
    
    
    def add_drink(self, data):
        sql_insert = """INSERT INTO drink(Drink, Price, Size) VALUES(?,?)"""
        self.__insert_data(sql_insert, data)


    def get_list_foods(self):
        sql_select = """SELECT * FROM food;"""
        return self.__select_data(sql_select)



def show_menu():
    menu1 = Menu()
    menu1.create_menu()
    menu2 = Databasemanager()
    menu2.get_list_foods()