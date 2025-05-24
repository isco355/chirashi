from peewee import MySQLDatabase
import datetime
from peewee import *
from playhouse.db_url import connect
# Initialize the SQLite database
# The database file will be created automatically if it doesn't exist

db = MySQLDatabase('chirashi_db', user='root', password="root", host='mysql', port=3306)

class Flier(Model):
    title = CharField()
     

    class Meta:
        database = db 


db.create_tables([Flier])

