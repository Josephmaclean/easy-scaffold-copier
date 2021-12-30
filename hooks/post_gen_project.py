import os
import shutil
import git

REMOVE_PATHS = [
    '{% if cookiecutter.project_database == "mongodb" %} migrations {% endif %}',
    '{% if cookiecutter.packaging != "pip" %} requirements.txt {% endif %}',
    '{% if cookiecutter.packaging != "poetry" %} poetry.lock {% endif %}',
    '{% if cookiecutter.packaging != "poetry" %} pyproject.toml {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)

