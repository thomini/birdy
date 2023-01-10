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

# code snipped from https://www.sqlitetutorial.net/sqlite-python/creating-tables/
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sql.Error as e:
        print(e)

# now code specific for birdy

sql_create_birdy_table = """ CREATE TABLE IF NOT EXISTS bird_counts (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

print(sql_create_birdy_table)