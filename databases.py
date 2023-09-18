import sqlite3


class Databases:
    conn = None
    cur = None

    @classmethod
    def init_connection(cls, db_file):
        cls.conn = sqlite3.connect(db_file)
        cls.cur = cls.conn.cursor()
        cls.create_user_table()
        cls.create_movies_table()
        cls.conn.commit()

    # create table for users in SQLITE DATABASE
    @classmethod
    def create_user_table(cls):
        cls.cur.execute(
            """
           CREATE TABLE IF NOT EXISTS user (
                id  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                email TEXT NOT NULL,
                username  TEXT NOT NULL,  
                password TEXT NOT NULL
            )
        """
        )

    # create table for movies in SQLITE DATABASE
    @classmethod
    def create_movies_table(cls):
        cls.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                title TEXT NOT NULL,
                release_year INTEGER NOT NULL,
                genre TEXT NOT NULL
            )
        """
        )

    # get connetion in SQLITE DATABASE
    @classmethod
    def get_connection(cls):
        return cls.conn

    # get cursor for query in SQLITE DATABASE
    @classmethod
    def get_cursor(cls):
        return cls.cur

    # close conection in SQLITE DATABASE
    @classmethod
    def close(cls):
        if cls.conn:
            cls.conn.close()
