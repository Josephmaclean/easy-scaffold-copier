import os
import click
import shutil
import subprocess


remove_parent = "{{cookiecutter._remove_parent}}"
project_name = "{{cookiecutter._project_name}}"

source_dir = os.getcwd()

subprocess.run(['git', 'init', source_dir], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
subprocess.run(['git', 'add', '*'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
subprocess.run(['git', 'commit', '-m', 'Initial commit'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

if remove_parent == "True":
    # Move app to specified directory if path is provided
    target_dir = os.path.join(source_dir, "..")

    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

    shutil.rmtree(source_dir)

    click.echo(click.style("Project scaffold complete. Happy hacking!!!", fg="bright_green"))
else:

    click.echo(click.style(f"{project_name} generated successfully. Happy hacking!!! ", fg="bright_green"))
