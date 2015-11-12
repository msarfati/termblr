# -*- coding: utf-8 -*-

from Termblr import models, security
import os

MODULE_PATH = os.path.split(os.path.realpath(__file__))[0]


def typical_fixtures():
    models.User.add_system_users()
    typical_users()


def typical_users():
    models.User.register(
        email='joe',
        name='Joe MacMillan',
        password='aaa',
        confirmed=True,
        roles=["User"],
    )
    models.User.register(
        email='cameron',
        name='Cameron Howe',
        password='aaa',
        confirmed=True,
        roles=["User"],
    )

