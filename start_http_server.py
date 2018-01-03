import json
import bottle


def start():
    server_config = json.loads(open("config/server_config.json").read())

    bottle.run(host=server_config["host"],
               port=server_config["port"])
