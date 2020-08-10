import mysql.connector

#Create the connection object
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root", database = "helloworld")

#create a cursor object
cur = myconn.cursor()

try:
    #Read all the data from the table
    cur.execute("select * from iq;")

    #fetching the rows from the cursor object
    res = cur.fetchall()

    for x in res:
        print(x)
except:
    myconn.rollback()

#Use-case: 1 => Country which has the highest IQ rate.
try:
    cur.execute("select * from iq order by avg_iq desc limit 1;")
    highest = cur.fetchall()

    for i in highest:
        print("Highest IQ =>", i)
except:
    myconn.rollback()

#Use-case: 2 => Country which has the least IQ rate.
try:
    cur.execute("select * from iq order by avg_iq limit 1;")
    least = cur.fetchall()

    for j in least:
        print("Least IQ =>", j)
except:
    myconn.rollback()

#Use-case: 3 => IQ Rate of India.
try:
    cur.execute("select * from iq where country = 'india'")
    average = cur.fetchall()

    for k in average:
        print("IQ of India =>", k)
except:
    myconn.rollback()

myconn.close