from json import loads
from bottle import run
import src.catalog_http  # load bottle routes


def start():
    server_config = loads(open("config/server_config.json").read())

    run(host=server_config["host"],
        port=server_config["port"])
