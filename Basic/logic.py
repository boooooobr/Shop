import sqlite3
from config import DATABASE


class DB_Manager:
    def __init__(self, database):
        self.database = database
    def create_tables(self):
                conn = sqlite3.connect(self.database)
                with conn:
                     conn.execute('''CREATE TABLE Questions (
                user_id TEXT,
                Vopros TEXT ,
                Email TEXT

)''')  
                conn.execute('''CREATE TABLE ot  (
                otzuv TEXT

)''')             
                      
                conn.commit()
    def __execute(self, sql, data): #Метод который принимает три параметра
                conn = sqlite3.connect(self.database) #Подключения к базе данных
                with conn: #менеджер который обесппечивает коретное открытие коректный выполнения операций
                        conn.execute(sql, data) #выполняет sql запрос с использыванием метода executemany
                conn.commit() #сохраняет изменения в базе данных
    
    

    def insert_project(self, data): #Метод который принимает два параметр
                sql = 'INSERT OR IGNORE INTO Questions ( user_id,Vopros, Email) values(?,?,?)' #sql запрос который обращяется к табличке Questions и записывает туда параметры которые указына
                self.__execute(sql, data,) #Вставляет данные в базу
    def insert(self, data): #Метод который принимает два параметр
                sql = 'INSERT OR IGNORE INTO ot (otzuv) values(?)' #sql запрос который обращяется к табличке Questions и записывает туда параметры которые указына
                self.__execute(sql, data,) #Вставляет данные в базу

    
if __name__ == '__main__':
    manager = (DATABASE)
    manager.create_tables()