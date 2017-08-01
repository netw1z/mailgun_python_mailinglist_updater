#/usr/bin/python
# postermaster@yourdomain.com  [ your mailgun email ]
# This script currently only does 1000 users, but it will successfulyl upsert your email list/user database with varibles.
# Data contains up to 1000 seperate email entries to be upsert to your mailing list at mailgun
# Two generic Varibles Profile and Logo Are show as an example of user defined varibles you can pack into each email record at mailgun.
# You can access these when sending mail out to customize your newsletter/mailing with the users name, or their logo/avatar photo from your website/database. You can add as many as you want
# Refer to the documentation on how to access them in your newsletter HTML.

import json
import requests
import MySQLdb
import os
from time import sleep

def add_list_member(data):
    return requests.post(
        "https://api.mailgun.net/v3/lists/list@yourdomain.com/members.json",
        auth=('api', 'key-xxxxxxxxxxxxxxxxxxxxxxxxxxxx'),
        data=data)

# Database Setup
db = MySQLdb.connect("localhost","yourDB","yourDBLogin","yourDBpassword")
db.set_character_set('utf8')
cursor = db.cursor()
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')


data = []

cursor.execute("SELECT * FROM user_database LIMIT 1000")
result = cursor.fetchall()
for y in result:
        newdata = {}  
        id = y[0]
        username = y[1]
        email = y[3]
        start_date = y[5]
	profile = y[6]
	logo = y[7]
        newdata = {'subscribed': True, 'upsert' : True, 'address': email ,'name': username, 'vars': {"description": profile , "logo" : logo } }
        data.append(newdata)
data = {"members": json.dumps(data)}
msg = add_list_member(data)
# msg will return Success or Error message will be Output here.
print msg.json()

