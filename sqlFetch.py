import MySQLdb
a='12:10'
# Open database connection
db = MySQLdb.connect(host="103.108.140.109" ,user="tuhin",passwd="012Dark345",db="py")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.


sql="INSERT INTO pytab(id, alarm) VALUES(NULL, '%s')" % (a)
# sql="INSERT INTO alarm(id, alarm) VALUES(NULL, '12:10')"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()