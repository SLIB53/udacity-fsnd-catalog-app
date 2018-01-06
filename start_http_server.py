import json
import traceback
from bottle import get, post, request, response, run
import src.catalog_api as catalog_api
import src.catalog_errors as catalog_errors
import start_database


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
        return _category_to_dict(catalog_api.create_category(gen_context(),
                                                             arg_name))
    except catalog_errors.JSONBodyError as BodyError:
        _report_application_error(BodyError)
        response.status = 400
        return {"reason": "Body missing required parameter(s)."}
    except Exception as Error:
        _report_unkown_error(Error)
        response.status = 500


@get("/api/v1/categories")
def list_all_categories():
    try:
        categories = list(map(_category_to_dict,
                              catalog_api.list_all_categories(gen_context())))
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


def start():
    server_config = json.loads(open("config/server_config.json").read())

    run(host=server_config["host"],
        port=server_config["port"])


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
