from peewee import *
from flask_login import UserMixin
import os
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))
else:
    DATABASE = SqliteDatabase('apartments.sqlite') 

class User(UserMixin,Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

class Apartment(Model):
    address = CharField(null=False)
    bedrooms = IntegerField()
    price = IntegerField()
    cats = BooleanField(default=False)
    dogs = BooleanField(default=False)
    washer = BooleanField(default=False)
    dryer = BooleanField(default=False)
    dishwasher = BooleanField(default=False)
    outdoor_space = BooleanField(default=False)
    elevator = BooleanField(default=False)
    doorman = BooleanField(default=False)
    link = CharField()
    scheduled_showing = BooleanField(default=False)
    scheduled_showing_time = CharField()
    seen = BooleanField(default=False)
    applied = BooleanField(default=False)
    approved = BooleanField(default=False)
    user = ForeignKeyField(User, backref='apartments')

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User,Apartment], safe=True)
    print('Connected to database')
    DATABASE.close()
