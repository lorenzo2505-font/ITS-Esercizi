import json

PATH : str = "lezione_15/config.json"

mode: str = "r"

encoding: str = "utf-8"


with open (PATH, mode = mode, encoding = encoding) as file:

    config: dict = json.load(file)



#print(config["SUPERCLASS"]["nome"])

config["aggiunta"] = "NUOVO!!!!!"
config["host"] = "google.it"

with open (PATH, mode = "w") as file:

    json.dump(config, file, indent = 4)


