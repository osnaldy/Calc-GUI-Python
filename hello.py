import mysql.connector

dbh = mysql.connector.Connect( host='localhost', port=3307, database='employees', user='root', password='' )
dbh.set_autocommit( True )

# --- query, but do not fetch all records
sql = "DESCRIBE user"
cursor = dbh.cursor(buffered=True)
cursor.execute( sql )

for row in cursor.fetchall():
    print (row)
cursor.close()