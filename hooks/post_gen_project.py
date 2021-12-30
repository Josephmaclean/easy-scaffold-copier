import os
import shutil

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

remove_parent = "{{cookiecutter._remove_parent}}"

if remove_parent == "True":
    project_name = "{{cookiecutter._project_name}}"
    source_dir = os.getcwd()
    target_dir = os.path.join(source_dir, "..")

    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

    shutil.rmtree(source_dir)

