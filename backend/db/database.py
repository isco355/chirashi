from peewee import MySQLDatabase
import datetime
from peewee import *
from playhouse.db_url import connect
# Initialize the SQLite database
# The database file will be created automatically if it doesn't exist

import json
db = MySQLDatabase('chirashi_db', user='root', password="root", host='mysql', port=3306)

class Flier(Model):
    title = CharField()
    description=TextField()
    address=CharField()
    time=CharField()
    image_url=CharField()
    tags=TextField()
    user_id=IntegerField()

     
    def to_json(self):
        return json.loads(json.dumps(self.__data__))


    class Meta:
        database = db 


db.create_tables([Flier])

