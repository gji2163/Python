try:
#Take input in DD-mmm-YYYY format
    x=input().split("-")

#leap year shift per month
    if int(x[2])%4==0:
        a=1
    else:
        a=0

#Contains day shift per month
    an=[0,0,3,a+3,a-1,a+1,a+4,a-1,a+2,a-2,a+0,a+3,a-2]

#months of the year
    m=["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    
    print(["Sat","Sun","Mon","Tue","Wed","Thu","Fri"][(((int(x[2])-1)//4)*5+(int(x[2])-1)%4+an[m.index(x[1])]+int(x[0]))%7])
except:
    pass
