import MySQLdb
from dbconfig import db
a=100

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM alarm WHERE alarm='%d'" % (a)
try:
   # Execute the SQL command
   cursor.execute(sql)

   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      alarmData = row[1]
      # Now print fetched result
      print ("id= %s,alarmData= %s" % \
             (id, alarmData))
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()