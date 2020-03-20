#!d:\Python34\python.exe
import cgi
import mysql.connector
con=mysql.connector.connect(user='root',password='root',host='localhost',database='project')
cursor=con.cursor()
form=cgi.FieldStorage()
fname=form.getvalue('t1')
sname=form.getvalue('t2')
email=form.getvalue('t3')
pswd=form.getvalue('t4')
mob=form.getvalue('t5')
cit=form.getvalue('t6')
add=form.getvalue('t7')
print("Content.Type: text/html")
print("""
     <html>
     <head>
     <title>DEMO</title>
     </head>
     </html>
"""
)
sql="insert into state values('%s','%s','%s','%s','%s','%s','%s')"%(fname,sname,email,pswd,mob,cit,add)
try:
    cursor.execute(sql)
    print("User Register Successfully");
    con.commit()
except Exception as e:
    print(e)

    
