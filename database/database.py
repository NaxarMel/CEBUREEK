from peewee import Model, CharField, SqliteDatabase

db = SqliteDatabase('users.db')

folder_path = '../database/'


class Users(Model):
    username = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Users])
