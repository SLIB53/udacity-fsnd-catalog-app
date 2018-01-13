from os.path import abspath, isfile
from sqlite3 import connect
import src.catalog_api as api
import src.catalog_http as http

DB_FILE_PATH = abspath("catalog.db")


def setup():
    try:
        connection = connect(DB_FILE_PATH)
        cursor = connection.cursor()
        cursor.execute(open("src/sql/create_category_table.sql").read())
        cursor.execute(open("src/sql/create_item_table.sql").read())
        cursor.execute(open("src/sql/create_category_item_table.sql").read())
    finally:
        cursor.close()
        connection.commit()

    context = http.gen_context()
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
    print("Checking for sqlite database file at %s" % DB_FILE_PATH)
    if isfile(DB_FILE_PATH):
        print("Found sqlite database file at %s" % DB_FILE_PATH)
    else:
        print("Missing sqlite database file at %s" % DB_FILE_PATH)
        return False

    return True
