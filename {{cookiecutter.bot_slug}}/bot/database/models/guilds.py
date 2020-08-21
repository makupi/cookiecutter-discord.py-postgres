from bot.database import db


class Guild(db.Model):
    __tablename__ = "guilds"

    id = db.Column(db.BIGINT, primary_key=True)
    prefix = db.Column(db.Text)
