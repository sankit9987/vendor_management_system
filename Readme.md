## Table of Contents

- [Installation](#markdown-header-installation)

## Installation

This Project requires Python 3.11.x, PostgreSQL and OS-specific dependency tools.

> Setting up environment and installing requirements

bash
# Installing virtualenv from PyPi.
python -m pip install virtualenv

# Creating virtual environment.
mkdir .venv && virtualenv .venv/.

# Activating virtual environment.

# Mac and Linux
source .venv/bin/activate
# Windows
.venv/Scripts/activate


> Install requirements

bash
pip install -r requirements.txt


> Referring to .env.template, create and complete .env
> 
>Create and Migrate Django migrations to create the database tables

bash
python manage.py makemigrations && python manage.py migrate


> Create a Superuser

bash
python manage.py createsuperuser


> Start a server with

bash
python manage.py runserver 