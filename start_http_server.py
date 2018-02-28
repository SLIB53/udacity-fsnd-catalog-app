from json import loads
from bottle import run
import app_env


def start():
    import src.catalog_http  # load bottle routes

    run(host=app_env.SERVER_HOST,
        port=app_env.SERVER_PORT)
