import src.catalog_data as catalog_data


class Category:
    def __init__(self, category_id, name, created_at, modified_at):
        self.id = category_id
        self.name = name
        self.created_at = created_at
        self.modified_at = modified_at


def create_category(context, name):
    category_id, name, created_at, modified_at = \
        catalog_data.make_category(context, name)

    return Category(category_id, name, created_at, modified_at)
