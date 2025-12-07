import sqlite3
from config import DATABASE



class DB_Managr:
    def __init__(self, database):
        self.database = database
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE Class (
                            Vopros TEXT,
                            user_id INTEGER,
                            Email TEXT
                        )''')                                  
            
    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()

    

    def insert_project(self, data):
        sql = 'INSERT OR IGNORE INTO Class ( Vopros, Email) values( ?, ?)'
        self.__executemany(sql, data)


    



    
if __name__ == '__main__':
    manager = DB_Managr(DATABASE)
    manager.create_tables()