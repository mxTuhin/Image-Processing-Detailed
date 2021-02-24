import MySQLdb
import time
from time import ctime
from dbconfig import db
import pyglet
import winsound
import os


# # Open database connection
# db = MySQLdb.connect(host="192.168.0.101" ,user="tuhin",passwd="trex",db="py")

# prepare a cursor object using cursor() method
cursor = db.cursor()

def playPyglet():
    music = pyglet.resource.media('wakeUp.wav')
    music.play()
    time.sleep(2)


while 1:
    disTime = ctime().split(" ")
    discreteTime = disTime[3]
    alChecker = discreteTime.split(":")
    reminderChecker = str((alChecker[0]))+':'+str((alChecker[1]))
    # print(reminderChecker)

    sql = "SELECT * FROM reminder  order by id DESC LIMIT 1"
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          id = row[0]
          alarmData = row[1]
          # Now print fetched result
          # print(ctime())
          # print ("id=%d,alarmAt=%s" %  (id, alarmData ))
          # print(alarmChecker)
    except:
       print ("Error: unable to fecth data")

    if(reminderChecker==alarmData):
        winsound.PlaySound("wakeUp.wav", winsound.SND_ASYNC)
        time.sleep(2)
        break

    # disconnect from server
db.close()
