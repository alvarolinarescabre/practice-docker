import MySQLdb

db = MySQLdb.connect (user='root',
                      passwd='pass',
                      port=3306,
                      host='127.0.0.1',
                      db='my_db')
cur = db.cursor()

def get_allrecords() :
    cur.execute("SELECT * FROM Persons")
    for row in cur.fetchall() :
        print (row[0])
        print (row[1])
        print (row[2])
        print (row[3])

get_allrecords()

db.close()
