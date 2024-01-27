from mysql import connector as c
from sys import stdout

conn=c.connect(user='root',host='localhost',password='Giks@1602')
cur=conn.cursor()

print("""Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 16
Server version: 8.0.13 MySQL Community Server - GPL

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
""")

while True:
    try:
        cur.execute(input('mysql> '))
        try:
            conn.commit()
        except:
            print(cur)
    except Exception as e:
        stdout.shell.write(str(e)+'\n','COMMENT')
