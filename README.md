# Flask-Starter

Flask-Starter is a boilerplate starter template designed to help you quickstart your Flask web application development. It has all the ready-to-use bare minimum essentials.

## Features

- Flask 3.1
- Signup, Login via email-password
- Templates (Layouts, Auth)
- User roles (admin, user, staff)
- User profile status (active, inactive)
- Basic models (easily replace with your use-case)
- Bootstrap template (minimal)
- CLI scripts (initiate dummy database, run test server)
- Test & Production Configs

## Primary Goals

 - To help you save lots of hours as a developer, even if for a hobby project or commercial project :-)
 - To provide basic features of standard web apps, while staying as unopinionated as possible
 - To make back-end development quick to start, with robust foundations
 - To help you quickly learn how to build a Flask based web application
 - To help you quick start coding your web app's main logic and features

## Getting Started

[install uv](https://docs.astral.sh/uv/getting-started/installation/
)

clone the project

```bash
$ git clone https://github.com/daslef/flask-starter.git
$ cd flask-starter
```

create and activate uv enviroment

```bash
$ uv venv
$ .venv/Scripts/activate
```

install dependencies in virtualenv

```bash
$ uv sync
```

initialize database and dummy data

```bash
$ uv run python manage.py initdb
```

start dev server

```bash
$ uv run python manage.py runserver
```

format code

```bash
$ uv tool run ruff format
```

lint code

```bash
$ uv tool run ruff check
```

## Project Structure

```bash
flask-starter/
├── flaskstarter
│   ├── app.py
│   ├── config.py
│   ├── decorators.py
│   ├── extensions.py
│   ├── __init__.py
│   ├── albums
│   │   ├── models.py
│   │   ├── __init__.py
│   │   └── views.py
│   ├── static
│   │   ├── bootstrap.bundle.min.js
│   │   ├── bootstrap.min.css
│   │   └── jquery.slim.min.js
│   ├── auth
│   │   ├── constants.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── views.py
│   ├── templates
│   │   ├── albums
│   │   │   └── add_album.html
│   │   │   ├── all_albums.html
│   │   │   ├── edit_album.html
│   │   │   ├── view_album.html
│   │   ├── auth
│   │   │   ├── change_password.html
│   │   │   ├── contact_us.html
│   │   │   ├── landing.html
│   │   │   ├── login.html
│   │   │   ├── reset_password.html
│   │   │   └── signup.html
│   │   ├── layouts
│   │   │   ├── base.html
│   │   │   └── header.html
│   │   ├── macros
│   │   │   ├── _confirm_account.html
│   │   │   ├── _flash_msg.html
│   │   │   ├── _form.html
│   │   │   └── _reset_password.html
│   └── bootstrap.py
│   └── config.py
│   └── decorators.py
│   └── plugins.py
└── tests
    ├── __init__.py
    └── test_flaskstarter.py
├── manage.py
├── pyproject.toml
├── README.md
└── uv.lock
```


## Modules

This application uses the following modules

 - Flask
 - Flask-SQLAlchemy
 - Flask-Migrate
 - Flask-Login
 - pytest
 - Bootstrap (sorry)
 - Jinja2
