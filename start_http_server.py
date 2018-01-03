import json
from bottle import post, request, response, run
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
            return (json_body['name'],)
        except:
            raise catalog_errors.JSONBodyError()

    try:
        arg_name = parse_body(request.json)
        category = catalog_api.create_category(gen_context(), arg_name)

        return {
            "id": category.id,
            "name": category.name,
            "created_at": category.created_at,
            "modified_at": category.modified_at
        }
    except catalog_errors.JSONBodyError as BodyError:
        print("Application Error:", BodyError)
        response.status = 400
        return {"reason": "Body missing required parameter(s)."}
    except Exception as Error:
        import traceback
        print("Unknown Error:", Error)
        print("Trace:", traceback.format_exc())
        response.status = 500
        return


def start():
    server_config = json.loads(open("config/server_config.json").read())

    run(host=server_config["host"],
        port=server_config["port"])
