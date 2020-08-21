# Simple discord.py bot template
A simple cookiecutter template for a discord.py bot. Comes with some basic utility commands prepared.

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

# Running the bot
```
pipenv install
pipenv shell
python run.py
```
