from pathlib import Path

from flask import Flask

from .config import DefaultConfig
from .albums import albums_blueprint
from .auth import Users, auth_blueprint
from .plugins import db, migrate, login_manager


__all__ = ["create_app"]

DEFAULT_BLUEPRINTS = (albums_blueprint, auth_blueprint)


def create_app(config=None, app_name=None, blueprints=None):
    if not app_name:
        app_name = DefaultConfig.PROJECT
    if not blueprints:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name, instance_path=Path().resolve(), instance_relative_config=True)

    configure_app(app, config)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_error_handlers(app)

    return app


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)

    if config:
        app.config.from_object(config)


def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(id)

    login_manager.setup_app(app)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        return "Oops! You don't have permission to access this page.", 403

    @app.errorhandler(404)
    def page_not_found(error):
        return "Opps! Page not found.", 404

    @app.errorhandler(500)
    def server_error_page(error):
        return "Oops! Internal server error. Please try after sometime.", 500
