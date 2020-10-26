import json
import os

default_config = {"token": "", "prefix": "{{cookiecutter.prefix}}", "database": "postgresql://localhost/postgres"}


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
        self.database = os.getenv("DB_DSN")  # for docker
        if not self.database:
            self.database = self.config.get("database", default_config.get("database"))

    def store(self):
        data = {"prefix": self.prefix, "token": self.token, "database": self.database}
        with open(self.filename, "w") as file:
            json.dump(data, file)
