import os
import click
import shutil
import pathlib

REMOVE_PATHS = [
    '{% if cookiecutter.project_database == "mongodb" %} migrations {% endif %}',
    '{% if cookiecutter.sql_orm == "peewee" %} migrations {% endif %}',
    '{% if cookiecutter.packaging != "pip" %} requirements.txt {% endif %}',
]

project_database = "{{cookiecutter.project_database}}"
if project_database != "mongodb":
    # create versions directory as it can't be committed to git
    dir_path = os.path.join(os.getcwd(), "migrations/versions")
    pathlib.Path(dir_path).mkdir(parents=False, exist_ok=True)


for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)

remove_parent = "{{cookiecutter._remove_parent}}"
project_name = "{{cookiecutter._project_name}}"

if remove_parent == "True":
    # Move app to specified directory if path is provided
    source_dir = os.getcwd()
    target_dir = os.path.join(source_dir, "..")

    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

    shutil.rmtree(source_dir)

    click.echo(click.style("Project scaffold complete. Happy hacking!!!", fg="bright_green"))
else:

    click.echo(click.style(f"{project_name} generated successfully. Happy hacking!!! ", fg="bright_green"))
