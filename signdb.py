#!d:\Python34\python.exe
import cgi
import mysql.connector
con=mysql.connector.connect(user='root',password='root',host='localhost',database='project')
cursor=con.cursor()
form=cgi.FieldStorage()
user=form.getvalue('a1')
pswd=form.getvalue('a2')
print("Content.Type: text/html")
print("""
     <html>
     <head>
     <title>DEMO</title>
     </head>
     </html>
"""
)
sql="select * from state where email='{email}' and password='{password}'".format(email=user,password=pswd)
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    if(len(results)==1):
        print("LOGIN SUCCESSFUL")
    else:
        print("LOGIN SUCCESSFULLY") 
except Exception as e:
    print(e)

    
