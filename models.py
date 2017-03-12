from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime

db = SqliteExtDatabase('bank_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    surname = CharField(null=True)
    lastname = CharField(null=True)
    email = CharField(null=False)
    password = CharField(null=False)

class Token(BaseModel):
    token = CharField(null=False)
    user_id = IntegerField(null=False)

class Gif(BaseModel):
    gif_url = CharField(null=False)
    gif_name = CharField(null=False)
    user_id = IntegerField(null=False)

# create table
User.create_table(True)
Token.create_table(True)
Gif.create_table(True)

# connect db
db.connect()
