# input directly on the computer
#input from a file and output in another file
#input from a sql table and update the table

import numpy as np


student_marks = [np.random.randint(101) for _ in range(25)]

def passorfail(marks):
    return ["Pass" if mark>=50 else "Fail" for mark in marks]

#print(passorfail(student_marks))

def inputfile():
    with open("python projects\input.txt","r") as f:
        x=f.read().split("\n")
        f.close()
    with open("python projects\output.txt","w") as f:
        for i in x:
            if int(i) >=50:
                f.write("Pass\n")
            elif int(i)<=50:
                f.write("Fail\n")
        f.close()

#inputfile()

import pymysql

def inputsql():
    conn=pymysql.connect(host="localhost",user="root",passwd="Mnsg@6275",db="teacher")
    cursor=conn.cursor()
    cursor.execute("ALTER TABLE exams ADD `result` VARCHAR(255)")
    cursor.execute("UPDATE `exams` SET `result`= CASE WHEN `marks`>=50 THEN %s ELSE %s END",("Pass","Fail"))
    conn.commit()
    cursor.close()
    conn.close()

inputsql()