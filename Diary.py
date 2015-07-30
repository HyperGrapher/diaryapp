#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#29-07-2015 18:57:59 

from collections import OrderedDict
import datetime
import sys

from peewee import *

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
    choice = None
    
    while choice != 'q':
        print("\n\nÇıkmak için 'q' tuşuna basın")
        for key, value in menu.items():
            print ('{}-) {}'.format(key, value.__doc__))
        choice = input("Seçiminiz: ").lower().strip()
        
        if choice in menu:
            menu[choice]()

    
def add_entry():
    """Entry girin"""
    print("Entry'nizi girdikten sonra ctrl+d yaparak tamamlayın")
    data = sys.stdin.read().strip()
    
    if data:
        if input("\n\nKaydedilsin mi? [Y/n] ").lower() != "n":            
            Entry.create(content = data)
            print("\n\nEntry'iniz kaydedildi!")
            
    
def view_entries():
    "Önceki entry'lere bakın"
    entries = Entry.select().order_by(Entry.timestamp.desc()).get()
    print(entries.content)
    
    
def delete_entry():
    "Bir entry silin"
    

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
])

    
if __name__ == '__main__':
    initialize()
    menu_loop()



    


    



