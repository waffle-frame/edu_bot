import os 
from dotenv import load_dotenv
from dataclasses import dataclass


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

def load_config():
    load_dotenv()

    return Config(
        bot = Bot(
            token = os.environ.get("BOT_TOKEN"),
        ),
        userbot = Userbot(
            api_id = os.environ.get("USERBOT_BOT_API_ID"),
            api_hash = os.environ.get("USERBOT_API_HASH"),
            phone_number = os.environ.get("USERBOT_PHONE_NUMBER"),
        ),
        database = Database(
            username = os.environ.get("POSTGRES_USERNAME"),
            password = os.environ.get("POSTGRES_PASSWORD"),
            host = os.environ.get("POSTGRES_HOST"),
            port = os.environ.get("POSTGRES_PORT"),
            db_name = os.environ.get("POSTGRES_DB_NAME"),
        ),
        logger = Logger(
            path = os.environ.get("LOGGER_PATH"),
            level = "DEBUG",
        ),
    )
