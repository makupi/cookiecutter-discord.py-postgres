from bot import utils
from gino import Gino


naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

db = Gino(naming_convention=naming_convention)

# import models so Gino can register them
import bot.database.models  # noqa


async def setup():
    await db.set_bind(utils.config.database)


async def shutdown():
    await db.pop_bind().close()


async def query_guild(guild_id: int):
    """query guild, create if not exist"""
    guild = await models.Guild.get(guild_id)
    if guild is None:
        guild = await models.Guild.create(id=guild_id)
    return guild