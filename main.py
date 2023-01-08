import sqlite3 as sql

## initiate plain database

#from sqlite3 import Error

# code snipped from https://www.sqlitetutorial.net/sqlite-python/creating-database/
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sql.connect(db_file)
        print(sql.version)
    except sql.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection('db/birdy_sqlit3.db')