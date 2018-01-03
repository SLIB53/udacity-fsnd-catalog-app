from os.path import isfile
from sqlite3 import connect

DB_FILE_PATH = "catalog.db"


def setup():
    try:
        connection = connect(DB_FILE_PATH)
        cursor = connection.cursor()
    finally:
        cursor.close()
        connection.commit()


def check():
    print("Checking for sqlite database file at %s" % DB_FILE_PATH)
    if not isfile(DB_FILE_PATH):
        print("Missing sqlite database file at %s" % DB_FILE_PATH)
        return False

    return True
