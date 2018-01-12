import json
import traceback
from bottle import delete, get, post, put, request, response, static_file, run
import src.catalog_api as catalog_api
import src.catalog_errors as catalog_errors
import start_database


#
# Views
#

@get("/")
def root():
    return static_file(filename="index.html", root="views")


@get("/category")
def category():
    return static_file(filename="category.html", root="views")


@get("/item")
def item():
    return static_file(filename="item.html", root="views")


@get("/new-item")
def item():
    return static_file(filename="new-item.html", root="views")


@get("/edit-item")
def item():
    return static_file(filename="edit-item.html", root="views")


#
# Public Directory
#

@get("/<filepath>")
def public(filepath):
    return static_file(filename=filepath, root="public")


@get("/index.html")
def index():
    return root()


#
# API
#

class RequestContext:
    def __init__(self, db_uri):
        self.db_uri = db_uri


def gen_context():
    return RequestContext(start_database.DB_FILE_PATH)  # TODO: use config file


@post("/api/v1/category")
def create_category():
    def parse_body(json_body):
        try:
            assert(json_body is not None)
            return json_body['name']
        except:
            raise catalog_errors.JSONBodyError()

    try:
        arg_name = parse_body(request.json)
        response.status = 201
        return _category_to_dict(catalog_api.create_category(gen_context(),
                                                             arg_name))
    except catalog_errors.JSONBodyError as BodyError:
        _report_application_error(BodyError)
        response.status = 400
        return {"reason": "Body missing required parameter(s)."}
    except Exception as Error:
        _report_unkown_error(Error)
        response.status = 500


@get("/api/v1/category/<category_id:int>")
def get_category(category_id):
    try:
        i = catalog_api.get_category(gen_context(), category_id)

        if i:
            return _category_to_dict(i)
        else:
            response.status = 404

    except Exception as Error:
        _report_unkown_error(Error)
        response.status = 500


@get("/api/v1/categories")
def list_all_categories():
    try:
        categories = list(map(_category_to_dict,
                              catalog_api.list_all_categories(gen_context())))
        response.set_header('Content-Type', 'application/json')
        return json.dumps(categories)
    except Exception as Error:
        _report_unkown_error(Error)
        response.status = 500


@post("/api/v1/category/<category_id:int>/item")
def create_child_item(category_id):
    def parse_body(json_body):
        try:
            assert(json_body is not None)
            return (json_body['name'], json_body.get('description', ''))
        except:
            raise catalog_errors.JSONBodyError()

    try:
        arg_name, arg_descr = parse_body(request.json)
        response.status = 201
        return _item_to_dict(catalog_api.create_child_item(gen_context(),
                                                           category_id,
                                                           arg_name,
                                                           arg_descr))

    except catalog_errors.JSONBodyError as BodyError:
        _report_application_error(BodyError)
        response.status = 400
        return {"reason": "Body missing required parameter(s)."}
    except Exception as Error:
        _report_unkown_error(Error)
        response.status = 500


@get("/api/v1/item/<item_id:int>")
def get_item(item_id):
    try:
        i = catalog_api.get_item(gen_context(), item_id)

        if i:
            return _item_to_dict(i)
        else:
            response.status = 404

    except Exception as Error:
        _report_unkown_error(Error)
        response.status = 500


@put("/api/v1/item/<item_id:int>")
def update_item(item_id):
    def parse_body(json_body):
        try:
            if json_body:
                return (json_body.get('name'), json_body.get('description'))
            else:
                return (None, None)
        except:
            raise catalog_errors.JSONBodyError()

    try:
        arg_name, arg_descr = parse_body(request.json)
        catalog_api.update_item(gen_context(), item_id, arg_name, arg_descr)

        response.status = 204

    except catalog_errors.ObjectNotFoundError as NotFoundError:
        _report_application_error(NotFoundError)
        response.status = 404
    except Exception as Error:
        _report_unkown_error(Error)
        response.status = 500


@delete("/api/v1/item/<item_id:int>")
def delete_item(item_id):
    try:
        catalog_api.delete_item(gen_context(), item_id)
        response.status = 204

    except Exception as Error:
        _report_unkown_error(Error)
        response.status = 500


@get("/api/v1/items")
def list_all_items():
    try:
        # Parse query

        q_order_by = 'id'
        if request.query.get('order_by') == 'age':
            q_order_by = 'age'

        q_order = 'ascend'
        if request.query.get('order') == 'desc':
            q_order = 'descend'

        q_limit = request.query.get('limit', 10)
        if not isinstance(q_limit, int) and q_limit.isdigit():
            q_limit = int(q_limit)

        # Format fetched items

        items = list(map(_item_to_dict,
                         catalog_api.list_all_items(gen_context(),
                                                    q_order_by,
                                                    q_order,
                                                    q_limit)))

        response.set_header('Content-Type', 'application/json')
        return json.dumps(items)
    except Exception as Error:
        _report_unkown_error(Error)
        response.status = 500


@get("/api/v1/category/<category_id:int>/items")
def list_all_items(category_id):
    try:
        items = list(map(_item_to_dict,
                         catalog_api.list_child_items(gen_context(),
                                                      category_id)))

        response.set_header('Content-Type', 'application/json')
        return json.dumps(items)
    except Exception as Error:
        _report_unkown_error(Error)
        response.status = 500


def _category_to_dict(category):
    return {
        "id": category.id,
        "name": category.name,
        "created_at": category.created_at,
        "modified_at": category.modified_at
    }


def _item_to_dict(item):
    return {
        "id": item.id,
        "name": item.name,
        "description": item.description,
        "created_at": item.created_at,
        "modified_at": item.modified_at
    }


def _report_application_error(application_exception):
    print("Application Error:", application_exception)
    print("Trace:", traceback.format_exc())


def _report_unkown_error(exception):
    print("Unknown Error:", exception)
    print("Trace:", traceback.format_exc())
