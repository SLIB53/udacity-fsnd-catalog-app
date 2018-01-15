from os.path import isfile
from sqlite3 import connect
import src.catalog_api as api
import src.catalog_http as http
import app_env


def setup():
    print("Initializing database...")
    initialize_db()
    print("Writing default content...")
    create_default_content()
    print("Done.")


def initialize_db():
    try:
        connection = connect(app_env.DB_FILE_PATH)
        cursor = connection.cursor()
        cursor.execute(open("src/sql/create_category_table.sql").read())
        cursor.execute(open("src/sql/create_item_table.sql").read())
        cursor.execute(open("src/sql/create_category_item_table.sql").read())
    finally:
        cursor.close()
        connection.commit()


def create_default_content():
    context = app_env.gen_main_context()
    animals_category = api.create_category(context, "Animals")
    api.create_child_item(context,
                          animals_category.id,
                          "Dog",
                          "A dog is a man's best friend.")
    api.create_child_item(context,
                          animals_category.id,
                          "Cat",
                          '''
“Would you tell me, please, which way I ought to go from here?” [said Alice.]
“That depends a good deal on where you want to get to,” said the Cat.
“I don’t much care where–” said Alice.
“Then it doesn’t matter which way you go,” said the Cat.
“–so long as I get SOMEWHERE,” Alice added as an explanation.
“Oh, you’re sure to do that,” said the Cat, “if you only walk long enough.”

-- from Alice in Wonderland, by Lewis Carrol''')

    jokes_category = api.create_category(context, "Programmer Jokes")
    api.create_child_item(context,
                          jokes_category.id,
                          "There are 10 types of programmers...",
                          "...those who know binary, and those who don't.")
    api.create_child_item(context,
                          jokes_category.id,
                          "2b || !2b",
                          "true")
    api.create_child_item(context,
                          jokes_category.id,
                          "There are 2 hard problems in computer science...",
                          '"There are 2 hard problems in computer science: cache invalidation, naming things, and off-by-1 errors." -- Leon Bambrick')


def check():
    print("Checking for sqlite database file at %s" % app_env.DB_FILE_PATH)
    if isfile(app_env.DB_FILE_PATH):
        print("Found sqlite database file at %s" % app_env.DB_FILE_PATH)
    else:
        print("Missing sqlite database file at %s" % app_env.DB_FILE_PATH)
        return False

    return True
