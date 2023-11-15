def factorial(x):
    if x==1:
        return 1
    return factorial(x-1)*x

import pymysql

conn=pymysql.connect(host="localhost",user="root",passwd="Mnsg@6275",db="teacher")
cursor=conn.cursor()
#cursor.execute("ALTER TABLE numbers ADD `result` VARCHAR(255)")
cursor.execute("SELECT number from numbers")
rows=cursor.fetchall()
fact=[]
for row in rows:
    fact.append(factorial(row[0]))
for i,j in enumerate(fact[::-1]):
    cursor.execute("UPDATE `numbers` SET `result`=%s LIMIT %s",(j,abs(i-4)))
conn.commit()
cursor.close()

conn.close()