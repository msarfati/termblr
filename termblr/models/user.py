# -*- coding: utf-8 -*-
from .. import db, security
from ..utils.mixins import CRUDMixin
import datetime
import flask
from flask.ext.security import UserMixin
from flask.ext.security.utils import encrypt_password

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))
"A secondary table is used for the one-to-many relationship: User has many Roles"


class User(db.Model, UserMixin, CRUDMixin):
    """
    A User.
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column('password', db.String(255), nullable=False)
    active = db.Column(db.Boolean)
    confirmed = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    last_login_at = db.Column(db.DateTime)

    # Profile information
    name = db.Column(db.String(50))
    balance = db.Column(db.Float, default=0, nullable=False)

    roles = db.relationship('Role',
        enable_typechecks=False,
        secondary=roles_users,
        # backref=db.backref('users', lazy='dynamic'),
    )

    def __str__(self):
        return '<User {}>'.format(self.email)

    def confirm(self):
        """
        update a User account so that login is permitted

        :returns: None
        """

        self.confirmed_at = datetime.datetime.now()
        self.confirmed = True
        self.active = True
        self.save()

    def add_role(self, role_name):
        """
        update a User account so that it includes a new Role

        :param role_name: the name of the Role to add
        :type role_name: string
        """

        new_role = security.datastore.find_or_create_role(role_name)
        security.datastore.add_role_to_user(self, new_role)
        db.session.commit()

    @classmethod
    def register(cls, email, password, confirmed=False, name=None, roles=None):
        # import ipdb; ipdb.set_trace()
        security.datastore.create_user(
            email=email,
            password=encrypt_password(password)
        )
        db.session.commit()

        new_user = cls.find(email=email)

        if confirmed:
            new_user.confirm()

        if name:
            new_user.name = name
            db.session.commit()

        if roles:
            for role_name in roles:
                new_user.add_role(role_name)

        flask.current_app.logger.debug("Created user {0}".format(email))
        return new_user

    @classmethod
    def add_system_users(cls):
        """
        Create a basic set of users and roles

        :returns: None
        """

        # make roles
        security.datastore.find_or_create_role("Admin")
        security.datastore.find_or_create_role("User")
        db.session.commit()

        cls.register(
            email="admin",
            password="aaa",
            confirmed=True,
            roles=["Admin"]
        )

        cls.register(
            email="guest",
            password="guest",
            confirmed=True,
            roles=["User"]
        )

        db.session.commit()

    @classmethod
    def rm_system_users(cls):
        """
        remove default system users

        :returns: None
        """

        security.datastore.delete_user(email="admin")
        security.datastore.delete_user(email="guest")
        db.session.commit()
