#!d:\Python34\python.exe
import cgi
import mysql.connector
con=mysql.connector.connect(user='root',password='root',host='localhost',database='project')
cursor=con.cursor()
form=cgi.FieldStorage()
nfr=form.getvalue('p1')
pa=form.getvalue('p2')
nl=form.getvalue('p3')
hf=form.getvalue('p4')
nm=form.getvalue('p5')
print("Content.Type: text/html")
print("""
     <html>
     <head>
     <title>DEMO</title>
     </head>
     </html>
"""
)
sql="insert into data values('%s','%s','%s','%s','%s')"%(nfr,pa,nl,hf,nm)
try:
    cursor.execute(sql)
    print("Information has been stored");
    con.commit()
except Exception as e:
    print(e)

    
