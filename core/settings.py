from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admins_id: list[int]


@dataclass
class Settings:
    bots: Bots


def getSettings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("BOT_TOKEN"),
            admins_id=env.str("ADMINS").split(" ")
        )
    )


settings = getSettings('.env')
print(settings)
