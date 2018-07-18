from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_security import RoleMixin
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash
import re

db = SQLAlchemy()

# Define modelo de dados para usuários e regras de acesso
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


# Modelo de dados para pessoa
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Enum('BASIC', 'ADMIN', 'MASTER', name='user_roles'), default='BASIC')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Validação para o nome
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise AssertionError('Nome deve ser preenchido')

        if User.query.filter(Pessoa.name == name).first():
            raise AssertionError('Nome já está em uso')

        if len(name) < 5 or len(name) > 20:
            raise AssertionError('Nome deve ter entre 5 e 20 caracteres')

        return name

    # Validação para o e-mail
    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('Email deve ser preenchido')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Email preenchido não é um endereço válido')

        return email

    def set_password(self, password):
        if not password:
            raise AssertionError('Senha deve ser preenchida')

        if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
            raise AssertionError('Senha deve conter 1 letra maiúscula e 1 número')

        if len(password) < 5 or len(password) > 50:
            raise AssertionError('Senha deve ter entre 8 e 50 caracteres')

        self.password_hash = generate_password_hash(password)
