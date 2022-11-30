import os 
from dataclasses import dataclass
from argparse import ArgumentParser
from json import loads as load_json


@dataclass
class Bot:
    token: str

@dataclass
class Userbot:
    api_id: int
    api_hash: str
    phone_number: str # Format: +1234567890

    def validate_phone_number():
        pass

@dataclass
class Database:
    username: str
    password: str
    host: str
    port: int
    db_name: str

@dataclass
class Logger:
    path: str
    level: str

@dataclass
class Config:
    bot: Bot
    userbot: Userbot
    database: Database
    logger: Logger


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-dev", help="use production configuration", action="store_true")
    parser.add_argument("-prod", help="use developer configuration", action="store_true")

    args = parser.parse_args()
    if not args.dev and not args.prod:
        parser.print_help()
        exit(1)

    if args.dev:
        return "dev_config.json"

    return "config.json"


def load_config():
    PATH_CONFIG = parse_args()

    if not os.path.exists(PATH_CONFIG):
        PATH_CONFIG = os.path.normpath(
            os.getcwd()+ os.sep + os.pardir) +os.sep+ PATH_CONFIG

    f = open(PATH_CONFIG, "r")
    config = load_json(f.read())
    f.close()

    return Config(
        bot = Bot(
            token = config["bot"]["token"],
        ),
        userbot = Userbot(
            api_id = config["userbot"]["api_id"],
            api_hash = config["userbot"]["api_hash"],
            phone_number = config["userbot"]["phone_number"], 
        ),
        database = Database(
            username = config["database"]["username"],
            password = config["database"]["password"],
            host = config["database"]["host"],
            port = config["database"]["port"],
            db_name = config["database"]["db_name"],
        ),
        logger = Logger(
            path = config["logger"]["path"],
            level = config["logger"]["level"],
        ),
    )
