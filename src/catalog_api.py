import src.catalog_data as catalog_data
import src.catalog_errors as catalog_errors


# ==============================================================================
# Content
# ==============================================================================

# ------------------------------------------------------------------------------
# Category
# ------------------------------------------------------------------------------

class Category:
    def __init__(self, category_id, name, created_at, modified_at):
        self.id = category_id
        self.name = name
        self.created_at = created_at
        self.modified_at = modified_at


def create_category(context, name):
    return Category(*catalog_data.make_category(context, name))


def get_category(context, category_id):
    data = catalog_data.fetch_category(context, category_id)
    return Category(*data) if data else None


def list_all_categories(context):
    return [Category(*data)
            for data in catalog_data.fetch_all_categories(context)]


# ------------------------------------------------------------------------------
# Item
# ------------------------------------------------------------------------------

class Item:
    def __init__(self, item_id, name, description, created_at, modified_at):
        self.id = item_id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.modified_at = modified_at

    @staticmethod
    def is_valid_name(item_name):
        return isinstance(item_name, str) and item_name != ""

    @staticmethod
    def is_valid_description(item_description):
        return isinstance(item_description, str)


def create_item(context, name, description):
    if Item.is_valid_name(name) and Item.is_valid_description(description):
        return Item(*catalog_data.make_item(context, name, description))
    else:
        raise catalog_errors.ItemDomainError()


def get_item(context, item_id):
    data = catalog_data.fetch_item(context, item_id)
    return Item(*data) if data else None


def update_item(context, item_id, name=None, description=None):
    if Item.is_valid_name(name) and Item.is_valid_description(description):
        if get_item(context, item_id):
            catalog_data.update_item(context, item_id, name, description)
        else:
            raise catalog_errors.ObjectNotFoundError()
    else:
        raise catalog_errors.ItemDomainError()


def delete_item(context, item_id):
    catalog_data.delete_item(context, item_id)


def list_all_items(context, order_by='id', order='ascend', limit=10):
    return [Item(*data)
            for data in catalog_data.fetch_all_items(context,
                                                     order_by,
                                                     order,
                                                     limit)]


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


def list_child_items(context,
                     parent_category_id):
    return [Item(*data)
            for data in catalog_data.fetch_child_items(context,
                                                       parent_category_id)]
