from PIL import Image
def load(x):
    return open(str(x),'r').read()
def create(x,data):
    f=open(str(x),'w')
    f.write("Coded Data:\n\n"+data)
    f.close()
def gendata(data):
    newdata=[]
    for i in data:
        newdata+=format(ord(i),"08b")
    return newdata
def modPix(pix,data):
    datalist=gendata(data)
    lendata=len(datalist)
    imdata=iter(pix)
    for i in range(lendata):
        pix=[value for value in imdata.__next__()[:3]+imdata.__next__()[:3]+imdata.__next__()[:3]]
        for j in range(0,8):
            if (datalist[i][j]=='0') and (pix[j]%2!=0):
                pix[j]-=1
            elif (datalist[i][j]=='1') and (pix[j]%2==0):
                pix[j]-=1
        if i==lendata-1:
            if pix[-1]%2==0:
                pix[-1]-=1
        else:
            if pix[-1]%2!=0:
                pix[-1]-=1
        pix=tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]
def encode_img(newimage,data):
    w=newimage.size[0]
    x=0
    y=0
    for pixel in modPix(newimage.getdata(),data):
        newimage.putpixel((x,y),pixel)
        #To chanege row
        if x==w-1:
            x=0
            y+=1
        else:
            x+=1
def decode(i):
    image=Image.open(i,'r')
    d_data=''
    imgdata=iter(image.getdata())
    while True:
        pix=[value for value in imgdata.__next__()[:3]+imgdata.__next__()[:3]+imgdata.__next__()[:3]]
        #String of binary
        bin=''
        for i in pix[0:8]:
            if i%2==0:
                bin+='0'
            else:
                bin+='1'
        d_data+=str(chr(int(bin,2)))
        if pix[-1]%2!=0:        
            return d_data
def encode(i,d,n):
    image=Image.open(i,"r")
    newimage=image.copy()
    encode_img(newimage,d)
    newimage.save(n,str(n.split(".")[1].upper()))
def main():
    a=int(input("::Welcome to Steganography::\n1:Encode\n2:Decode\nEnter choice:"))
    if a==1:
        i=input("Enter image name with extension:")
        print("\n1:choose data from existing txt file\n2:userdefined data")
        c=int(input("Data Input Mode:"))
        if c==1:
            x=input("Enter text file name(with extension):")
            d=load(x)
        if c==2:
            d=input("Enter data to be encoded:")
        n=input("Enter name of new image with extension as.png:")
        encode(i,d,n)
    elif a==2:
        i1 = input("Enter image name(with extension) :")
        print("Decode Data in new text file?")
        q=decode(i1)
        y=input("y/n:")
        if y=='y':
            x2=input("Enter name of text file with extension:")
            create(x2,q)
            print(q)
        else:
            print("Decoded Data:",q)
    else:
        raise Exception("Enter Valid Input")
