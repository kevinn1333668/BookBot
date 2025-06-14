from dataclasses import dataclass

from environs import Env #type: ignore


@dataclass
class TgBot:
    token: str
    admins_ids: list[int]

@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) ->  Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admins_ids=list(map(int, env.list('ADMINS_IDS')))
        )
    )