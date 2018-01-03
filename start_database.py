from os.path import abspath, isfile
from sqlite3 import connect

DB_FILE_PATH = abspath("catalog.db")


def setup():
    try:
        connection = connect(DB_FILE_PATH)
        cursor = connection.cursor()
        cursor.execute(open("src/sql/create_category_table.sql").read())
    finally:
        cursor.close()
        connection.commit()


def check():
    print("Checking for sqlite database file at %s" % DB_FILE_PATH)
    if isfile(DB_FILE_PATH):
        print("Found sqlite database file at %s" % DB_FILE_PATH)
    else:
        print("Missing sqlite database file at %s" % DB_FILE_PATH)
        return False

    return True
