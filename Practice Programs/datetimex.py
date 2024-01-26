from mysql.connector import connect as c
conn=c(user="root",host="localhost",password="Giks@1602")
cur=conn.cursor()
cur.execute("use datetime")

print("""
Code    Meaning

a 	Abbreviated weekday name (Sun to Sat)
b 	Abbreviated month name (Jan to Dec)
c 	Numeric month name (0 to 12)
D 	Day of the month as a numeric value, followed by suffix (1st, 2nd, 3rd,...)
d 	Day of the month as a numeric value (01 to 31)
e 	Day of the month as a numeric value (0 to 31)
f 	Microseconds (000000 to 999999)
H 	Hour (00 to 23)
h 	Hour (00 to 12)
I 	Hour (00 to 12)
i 	Minutes (00 to 59)
j 	Day of the year (001 to 366)
k 	Hour (0 to 23)
l 	Hour (1 to 12)
M 	Month name in full (January to December)
m 	Month name as a numeric value (00 to 12)
p 	AM or PM
r 	Time in 12 hour AM or PM format (hh:mm:ss AM/PM)
S 	Seconds (00 to 59)
s 	Seconds (00 to 59)
T 	Time in 24 hour format (hh:mm:ss)
U 	Week where Sunday is the first day of the week (00 to 53)
u 	Week where Monday is the first day of the week (00 to 53)
V 	Week where Sunday is the first day of the week (01 to 53). Used with Code X
v 	Week where Monday is the first day of the week (01 to 53). Used with Code X
W 	Weekday name in full (Sunday to Saturday)
w 	Day of the week where Sunday=0 and Saturday=6
X 	Year for the week where Sunday is the first day of the week. Used with Code V
x 	Year for the week where Monday is the first day of the week. Used with Code V
Y 	Year as a numeric, 4-digit value
y 	Year as a numeric, 2-digit value
""")
while True:
    cur.execute("insert into datetime values(date_format(sysdate(),"+"\"%"+(input("sep with:")+"%").join(input("Enter Code:").split())+"\"))")
    conn.commit()
    cur.execute("select DATE from datetime")
    a=cur.fetchall()
    x=len(cur.description[0][0])
    for i in range(len(a)):
        if len(a[i][0])>x:
            x=len(a[i][0])
    print("+"+"-"*x+"+"+"\n|"+str(cur.description[0][0])+"|\n"+"+"+"-"*x+"+")
    for i in a:
        print("|"+i[0]+" "*(x-len(i[0]))+"|")
    print("+"+"-"*x+"+")
