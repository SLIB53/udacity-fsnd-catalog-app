import json
import bottle


#
# Server Setup
#

server_config = json.loads(open("server_config.json").read())

bottle.run(host=server_config["host"],
           port=server_config["port"])
