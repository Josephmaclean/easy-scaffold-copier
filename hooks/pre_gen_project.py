import sys
project_name = "{{cookiecutter.project_name}}"

if project_name == "My Awesome project":
    print("Please input a name for your project")
    sys.exit(1)
