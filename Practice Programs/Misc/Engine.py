#Python program for Image Steganography
from PIL import Image #PIL module


#FILEMANAGEMENT
#load data from textfile
def load(x):
    data=''
    f=open(str(x),'r')
    data=f.read()
    return data

#create file 
def create(x,data):
    f=open(str(x),'w')
    data='Coded Data:\n\n'+data
    f.write(data)
    f.close()
    
    
    
#CONVERSION TO BINARY
def gendata(data):
    newdata=[] #list of binary of each bit of data
    for i in data:
        newdata.append(format(ord(i),"08b"))
    return(newdata)

#MODIFICATION OF EACH PIXEL 
def modPix(pix,data):
#even for 0,odd for 1
#8th bit for data end 0-continue,1-end
    datalist=gendata(data)
    lendata=len(datalist)#total bits
    imdata=iter(pix)#pixel numeric data

    for i in range(lendata):
        #Extracting 3 pixels per iteration
        #[:3] for...if more bits in pixel
        pix=[value for value in imdata.__next__()[:3]+imdata.__next__()[:3]+imdata.__next__()[:3]]

        for j in range(0,8):
            if (datalist[i][j]=='0') and (pix[j]%2!=0):
                pix[j]-=1
            elif (datalist[i][j]=='1') and (pix[j]%2==0):
                pix[j]-=1
        #8thbit
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

#ENCODE MODIFIED PIXELS INTO NEW IMAGE
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

#DECODE DATA
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

#ENCODE DATA
def encode(i,d,n):
    image=Image.open(i,"r")
    data=d
    newimage=image.copy()
    encode_img(newimage,data)
    newimage.save(n,str(n.split(".")[1].upper()))

#MAIN FUNCTION
def main():
    a=int(input("::Welcome to Steganography::\n1:Encode\n2:Decode\nEnter choice:"))
    if a==1:
        i="bg.png"#input("Enter image name with extension:")
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
    
