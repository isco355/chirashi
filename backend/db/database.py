from peewee import MySQLDatabase
import datetime
from peewee import *
from playhouse.db_url import connect
import os
import json

database_name =os.getenv("DATABASE_NAME") 

db = MySQLDatabase(database_name, user='root', password="root", host='mysql', port=3306)

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

