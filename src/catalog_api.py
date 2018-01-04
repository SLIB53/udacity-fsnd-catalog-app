import src.catalog_data as catalog_data


class Category:
    def __init__(self, category_id, name, created_at, modified_at):
        self.id = category_id
        self.name = name
        self.created_at = created_at
        self.modified_at = modified_at


class Item:
    def __init__(self, item_id, name, description, created_at, modified_at):
        self.id = item_id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.modified_at = modified_at


def create_category(context, name):
    category_id, name, created_at, modified_at = \
        catalog_data.make_category(context, name)

    return Category(category_id, name, created_at, modified_at)


def create_item(context, name, description):
    item_id, name, description, created_at, modified_at = \
        catalog_data.make_item(context, name, description)

    return Item(item_id, name, description, created_at, modified_at)


def create_child_item(context,
                      parent_category_id,
                      item_name,
                      item_description):
    # TODO: implement as single transaction in data layer
    new_item = create_item(context, item_name, item_description)
    catalog_data.add_category_item_relationship(context,
                                                parent_category_id,
                                                new_item.id)
    return new_item
