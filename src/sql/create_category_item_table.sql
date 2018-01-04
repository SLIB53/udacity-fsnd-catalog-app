CREATE TABLE category_item(
    "category_id"   INTEGER,
    "item_id"       INTEGER,
    FOREIGN KEY("category_id") REFERENCES category("id")
    FOREIGN KEY("item_id") REFERENCES item("id")
)
