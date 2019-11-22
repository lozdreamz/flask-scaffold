from flask import Flask
from newapp.config import app_config
from newapp.ext import db, migrate, debug_toolbar
from newapp.main.views import bp as main_bp


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    register_blueprints(app)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    debug_toolbar.init_app(app)
    app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
    return None


def register_blueprints(app):
    app.register_blueprint(main_bp)
    return None
