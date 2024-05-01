## Table of Contents

- [Installation](#markdown-header-installation)

## Installation

This Project requires Python 3.11.x, PostgreSQL and OS-specific dependency tools.

> Setting up environment and installing requirements

```bash
# Installing virtualenv from PyPi.
python -m pip install virtualenv
```
# Creating virtual environment.
mkdir .venv && virtualenv .venv/.

# Activating virtual environment.

# Mac and Linux
source .venv/bin/activate
# Windows
.venv/Scripts/activate


> Install requirements

```bash
pip install -r requirements.txt
```

> Referring to .env.template, create and complete .env
> 
>Create and Migrate Django migrations to create the database tables

```bash
# creating database table in db
python manage.py makemigrations && python manage.py migrate
```

> Create a Superuser

```bash
# creating superuser
python manage.py createsuperuser
```

> Start a server with

```bash
# running the server
python manage.py runserver 
```
> For Swagger UI hit below link to browser

```bash
http:127.0.0.1:8000/swagger
```