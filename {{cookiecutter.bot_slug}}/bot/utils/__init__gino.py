from .config import Config

config = Config()


def get_guild_prefix(_bot, guild_id):
    prefix = config.prefix
    guild_data = _bot.guild_data.get(guild_id, None)
    if guild_data is not None:
        _prefix = guild_data.get("prefix")
        if _prefix is not None:
            prefix = _prefix
    return prefix
