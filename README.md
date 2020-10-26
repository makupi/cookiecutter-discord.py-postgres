# Simple discord.py-postgres bot template
A simple cookiecutter template for a discord.py-postgres bot. Comes with some basic utility commands prepared.

# Requirements
```
pip install cookiecutter pipenv
```

# Using the template
```
cookiecutter https://github.com/makupi/cookiecutter-discord.py
```

# Features
- `pipenv` to manage your virtual environment 
- `config.json` file with token and prefix
- `.gitignore` with python template and `config.json` already ignored
- basic utility cog with `ping`, `info` etc.
- `gino` as a postgresql ORM
- `alembic` for database migrations
- `docker` and `docker-compose` for easier deployment (and development)

# Setup 
If you are utilizing the postgresql database you have to configure your URI in the `config.json` file.    
Then you have to generate an initial revision with alembic:
```
pipenv install
pipenv shell
alembic revision --autogenerate -m "Initial Revision"
```
And apply the revision with
```
alembic upgrade head
```
Whenever you make changes to your models you will have to generate a new revision and apply it. 

# Running the bot
```
pipenv install
pipenv shell
python run.py
```

# Credits
Parts of my template are inspired by [`discord-bot-cli`](https://github.com/stroupbslayen/discord-bot-cli) from StroupBSlayen.
