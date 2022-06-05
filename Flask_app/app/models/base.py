import flask_sqlalchemy
import sqlalchemy as sa
from flask_login import UserMixin


db = flask_sqlalchemy.SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True
    )
    username = sa.Column(sa.String(255), unique=True)
    password = sa.Column(sa.String(255))