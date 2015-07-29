#!usr/bin/python

#29-07-2015 18:57:59 

from peewee import *
import datetime

db = SqliteDatabase("diary.db")
    
class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db
 
def initialize():
    """create the db and table if they don't exist"""
    db.connect()
    db.create_tables([Entry], safe=True)
           
        
def menu_loop():
    """shows menu"""
    
def add_entry():
    """adds entry"""
    
def view_entries():
    "view entry"
    
def delete_entry():
    "deletes entry"


if __name__ == '__main__':
    initialize()
    menu_loop()
    print("burak")
    

    


    



