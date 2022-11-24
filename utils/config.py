import json
from typing import List
from dataclasses import dataclass


@dataclass
class Bot:
    token: str

@dataclass
class Database:
    username: str
    password: str
    host: str
    port: int

@dataclass
class Logger:
    path: str
    level: str

@dataclass
class Config:
    bot: Bot
    database: Database
    logger: Logger


def load_config(path: str = None):
    f = open('conf.json', 'r')
    conf = json.loads(f.read())
    f.close()

    return Config(
        bot = Bot(
            token = conf['bot']["token"],
        ),
        database = Database(
            username = conf['database']['username'],
            password = conf['database']['password'],
            host = conf['database']['host'],  
            port = conf['database']['port'],
        ),
        logger = Logger(
            path = conf['logger']['path'],
            level = conf['logger']['level'],
        ),
    )
