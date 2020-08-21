from bot import utils
from gino import Gino

db = Gino()

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