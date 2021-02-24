import MySQLdb

# Open database connection
db = MySQLdb.connect(host="localhost", user="root",passwd="",db="py")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM pytab "
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      alarm = row[1]
      reminder = row[2]
      # Now print fetched result
      print ("fname=%d,lname=%s,age=%s" %  (id, alarm, reminder ))
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()