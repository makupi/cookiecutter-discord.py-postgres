import os
import shutil

print(os.getcwd())


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


add_gino_database = '{{cookiecutter.add_gino_database}}'.lower() == 'y'
base_path = 'bot'


if not add_gino_database:
    remove(os.path.join(base_path, 'database'))
    remove(os.path.join(base_path, 'utils', 'config_gino.py'))
    remove(os.path.join(base_path, '__init__gino.py'))
    remove('config_gino.json')
    remove('alembic')
    remove("alembic.ini")
    remove("Pipfile_gino")
else:
    init_gino = os.path.join(base_path, '__init__gino.py')
    init = os.path.join(base_path, '__init__.py')
    shutil.move(init_gino, init)

    config_gino = os.path.join(base_path, 'utils', 'config_gino.py')
    config = os.path.join(base_path, 'utils', 'config.py')
    shutil.move(config_gino, config)

    config_init_gino = os.path.join(base_path, 'utils', '__init__gino.py')
    config_init = os.path.join(base_path, 'utils', '__init__.py')
    shutil.move(config_init_gino, config_init)

    shutil.move('config_gino.json', 'config.json')
    shutil.move("Pipfile_gino", "Pipfile")

