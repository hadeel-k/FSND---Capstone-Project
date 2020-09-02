import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from flask_cors import CORS
from datetime import date
import json
import sys
import inspect

# Database

# database_name = "capstone"
# database_host = "localhost:5432"
# username_pwd = "postgres:Bb009900"
# database_path = "postgresql://{}@{}/{}".format(
#     username_pwd, database_host, database_name)
# database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://mkdnlldthfxwej:859277a4f237a38029bfac0ee498776f2b5bd971177b95ac57eda17f79a7478b@ec2-54-146-91-153.compute-1.amazonaws.com:5432/db7lcj9q8jmhhn"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# Movies


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(db.DateTime(timezone=False), nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

# Actors


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    gender = Column(String, nullable=False)
    age = Column(String, nullable=False)

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age
        }

# # Development

# class Actor(db.Model):
#     __tablename__ = 'development'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, unique=True)
#     gender = Column(String, nullable=False)
#     age = Column(String, nullable=False)
