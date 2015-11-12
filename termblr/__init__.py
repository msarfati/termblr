# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore
import logging

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.security import Security
security = Security()

from flask.ext.restful import Api
rest_extension = Api()


class Termblr(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app=None, name=None, email=False, celery=False, request_handlers=False):
        'Initiailize app'

        if not name:
            name = __name__

        if app is None and self.app is None:
            self.app = Flask(name)
        elif app:
            self.app = app

        self.config()
        self.logs()

        self.database()

        self.ext_security()
        self.rest_api()

        if email:
            self.email()

        if request_handlers:
            self.request_handlers()

        if celery:
            self.init_celery()

        self.blueprints()

        # if hasattr(self.app, 'teardown_appcontext'):
        #     self.app.teardown_appcontext(self.teardown)
        # else:
        #     self.app.teardown_request(self.teardown)

    def blueprints(self):
        'Exposes endpoints and such'
        from .views import simpleview
        self.app.register_blueprint(simpleview)
        # self.app.register_blueprint(simpleview)

    def config(self):
        'Settings passed as environment variables'
        self.app.config.from_envvar('SETTINGS')

    def database(self):
        'Initialize the database'
        db.app = self.app
        db.init_app(self.app)

    def ext_security(self, app_models=None, **kwargs):
        'Protects the models.'
        if not app_models:
            from . import models
        else:
            models = app_models

        user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
        security.init_app(self.app, datastore=user_datastore, **kwargs)
        security._state = self.app.extensions["security"]
        security.datastore = user_datastore

    def logs(self):
        handler = logging.FileHandler(self.app.config['LOG'])
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
        self.app.logger.addHandler(handler)
        if self.app.config.get("LOG_LEVEL") == "DEBUG":
            self.app.logger.setLevel(logging.DEBUG)
        elif self.app.config.get("LOG_LEVEL") == "WARN":
            self.app.logger.setLevel(logging.WARN)
        else:
            self.app.logger.setLevel(logging.INFO)
        self.app.logger.info('Startup with log: %s' % self.app.config['LOG'])

    def rest_api(self, api_map=None):
        "RESTful API"
        if api_map:
            api_map(rest_extension)
        rest_extension.init_app(self.app)
        return rest_extension


def create_app():
    Termblr = Termblr()
    Termblr.init_app()
    return Termblr.app
