from sqlite3 import connect
import src.catalog_errors as catalog_errors


def make_category(context, name):
    """
    Returns tuple (id, name, created_at, modified_at).
    """
    try:
        connection = connect(context.db_uri)
        with connection:
            cursor = connection.cursor()

            # Write row

            insert_query = '''
                INSERT INTO category("name",
                                     "created_at", "modified_at")
                VALUES (?,
                        strftime('%s', 'now'), strftime('%s', 'now'));
            '''
            cursor.execute(insert_query, name)
            connection.commit()

            # Pull results

            fetch_query = '''
                SELECT id, name, created_at, modified_at
                  FROM category
                 WHERE id=?;
            '''

            cursor.execute(fetch_query, (cursor.lastrowid,))
            category_id, name, created_at, modified_at = cursor.fetchone()

            cursor.close()

            return (category_id, name, created_at, modified_at)
    except:
        raise catalog_errors.DBError()


def make_item(context, name, description):
    """
    Returns tuple (id, name, description, created_at, modified_at).
    """
    try:
        connection = connect(context.db_uri)
        with connection:
            cursor = connection.cursor()

            # Write row

            insert_query = '''
                INSERT INTO item ("name", "description",
                                  "created_at", "modified_at")
                VALUES (?, ?,
                        strftime('%s', 'now'), strftime('%s', 'now'));
            '''
            cursor.execute(insert_query, (name, description))
            connection.commit()

            # Pull results

            fetch_query = '''
                SELECT "id",
                       "name",
                       "description",
                       "created_at",
                       "modified_at"
                  FROM item
                 WHERE id = ?;
            '''
            cursor.execute(fetch_query, (cursor.lastrowid,))
            item_id, name, description, created_at, modified_at = \
                cursor.fetchone()

            cursor.close()

            return (item_id, name, description, created_at, modified_at)
    except:
        raise catalog_errors.DBError()


def add_category_item_relationship(context, category_id, item_id):
    try:
        connection = connect(context.db_uri)
        with connection:
            cursor = connection.cursor()

            # Write row

            insert_query = '''
                INSERT INTO category_item("category_id", "item_id")
                VALUES (?, ?);
            '''
            cursor.execute(insert_query, (category_id, item_id))
            connection.commit()

            cursor.close()

            return
    except:
        raise catalog_errors.DBError()
