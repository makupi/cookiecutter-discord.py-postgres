import json
import os

default_config = {"token": "", "prefix": "{{cookiecutter.prefix}}", "database": "postgresql://localhost/bot"}


class Config:
    def __init__(self, filename="config.json"):
        self.filename = filename
        self.config = {}
        if not os.path.isfile(filename):
            with open(filename, "w") as file:
                json.dump(default_config, file)
        with open(filename) as file:
            self.config = json.load(file)
        self.prefix = self.config.get("prefix", default_config.get("prefix"))
        self.token = self.config.get("token", default_config.get("token"))
        self.database = self.config.get("database", default_config.get("database"))

    def store(self):
        data = {"prefix": self.prefix, "token": self.token, "database": self.database}
        with open(self.filename, "w") as file:
            json.dump(data, file)
