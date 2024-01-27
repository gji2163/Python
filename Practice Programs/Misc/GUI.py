import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog,messagebox
import Engine
import tkinter.messagebox
from tkinter.ttk import Progressbar,Style


try:
    class MainWindow(tk.Tk):

        def __init__(self, *args, **kwargs):
            
            tk.Tk.__init__(self, *args, **kwargs)
            container = tk.Frame(self)

            container.pack(side='top',fill="both", expand = True)
            
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            for F in (About,Encode,Decode):

                frame = F(container, self)

                self.frames[F] = frame

                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(About)

        def show_frame(self, cont):

            frame = self.frames[cont]
            frame.tkraise()

    class About(tk.Frame):
        bg=0
        def __init__(self, parent, controller):
            global bg
            tk.Frame.__init__(self,parent,bg='black') 

            menu=tk.Frame(self,bg='black',height=100,width=100,highlightthickness=2,highlightbackground='red')

            canvas=tk.Canvas(menu,width=400, height=333,highlightthickness=0)
            canvas.config(bg='black')
            bg=tk.PhotoImage(file='bg.png')
            canvas.create_image(0,0,image=bg,anchor=tk.NW)
            canvas.pack()


            encode=tk.Button(menu,text="ENCODE",font=("Bell TM",24),fg="red",bg='black',activebackground='red',bd=0,command=lambda: controller.show_frame(Encode))

            decode=tk.Button(menu,text="DECODE",font=("Bell TM",24),fg="red",bg='black',bd=0,activebackground='red',command=lambda: controller.show_frame(Decode))

            about=tk.Button(menu,text="ABOUT",font=("Bell TM",24),fg="black",bg='red',bd=0,activebackground='red')

            quit=tk.Button(menu,text="QUIT",font=("Bell TM",24),fg="red",bg='black',bd=0,activebackground='red',command=lambda: controller.destroy())

            version=tk.Label(menu,text="V0.087.012",bg='black',fg="red",font=("Impact",20))
            version.pack(pady=20)

            encode.pack(pady=10)

            decode.pack(pady=10)

            about.pack(pady=10)

            quit.pack(pady=10)


            body=tk.Frame(self,bg='black',height=100,width=100,highlightthickness=0,highlightbackground='red')

            about_msg=tk.Label(body,text="\n\n\nMade By Girik Jindal",bg='black',fg="red",font=("Bell TM",40))
            about_msg.pack()

            menu.pack(side=tk.LEFT,fill=tk.Y)
            body.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)

    class Encode(tk.Frame):
        bg2=0
        def __init__(self, parent, controller):
            global bg2
            tk.Frame.__init__(self,parent,bg='black') 

            menu=tk.Frame(self,bg='black',height=100,width=100,highlightthickness=2,highlightbackground='red')

            canvas=tk.Canvas(menu,width=400, height=333,highlightthickness=0)
            canvas.config(bg='black')
            bg2=tk.PhotoImage(file='bg.png')
            canvas.create_image(0,0,image=bg2,anchor=tk.NW)
            canvas.pack()


            encode=tk.Button(menu,text="ENCODE",font=("Bell TM",24),fg="black",bg='red',activebackground='red',bd=0)

            decode=tk.Button(menu,text="DECODE",font=("Bell TM",24),fg="red",bg='black',bd=0,activebackground='red',command=lambda: controller.show_frame(Decode))

            about=tk.Button(menu,text="ABOUT",font=("Bell TM",24),fg="red",bg='black',bd=0,activebackground='red',command=lambda: controller.show_frame(About))

            quit=tk.Button(menu,text="QUIT",font=("Bell TM",24),fg="red",bg='black',bd=0,activebackground='red',command=lambda: controller.destroy())

            Status=tk.Label(menu,text="Status: Not Encoded",bg='black',fg="red",font=("Impact",20,))
            Status.pack(pady=20)
            
            encode.pack(pady=10)

            decode.pack(pady=10)

            about.pack(pady=10)

            quit.pack(pady=10)


            body=tk.Frame(self,bg='black',height=100,width=100,highlightthickness=0,highlightbackground='red')

            choose_file=tk.Label(body,text="Choose Image:",bg='black',fg="white",font=("Impact",25,tk.UNDERLINE))
            choose_file.pack(pady=10)
            filename=''
            x10=''

            def datafile():
                global x
                datafile = filedialog.askopenfilename()
                x10=Engine.load(datafile)
                st.insert(1.0,str(x10)) 
            
            def data():
                try:
                    global filename
                    d=((st.get(1.0, tk.END)))
                    if len(d)==1:
                        raise(ValueError)
                    n=((n_name.get())+'.png')
                    if n=='.png':
                        raise NameError
                    i=filename
                    Engine.encode(i,d,n)
                    Status.config(text="Status: Data Encoded ✔",fg='green')
                    
                except OSError:
                    tkinter.messagebox.showwarning("No Image Found!", "Choose An Image File")
                except NameError:
                    tkinter.messagebox.showwarning("Incorrect Directory!", "Enter Image Location/New File Name")
                except ValueError:
                    tkinter.messagebox.showwarning("No Data To Encode!", "Please Enter Some Data")
                
            
            def browsefunc():
                global filename
                filename = filedialog.askopenfilename()
                pathlabel.config(text=filename)

            

            browsebutton = tk.Button(body,text="Browse",font=("Impact",15),fg="black",bg='white',activebackground='red',bd=0, command=browsefunc)
            pathlabel = tk.Label(body,bg='white',bd=2,fg='black',width=40)
            pathlabel.config(font=("Bell TM",12))
            pathlabel.pack(pady=10)
            browsebutton.pack(pady=10)
            
            
            data_msg=tk.Label(body,text="Enter Data To Be Coded:",bg='black',fg="white",font=("Impact",25,tk.UNDERLINE))
            data_msg.pack(pady=20)
            
            st = ScrolledText(body, height=10,width=50,bg='white',fg='black',bd=0)
            st.config(insertbackground='black',font=("Bell TM",12))
            st.pack(pady=10)

            browsedata = tk.Button(body,text="Browse data file",font=("Impact",15),fg="black",bg='white',activebackground='red',bd=0,command=datafile)
            browsedata.pack(pady=10)

            newfile=tk.Label(body,text="Name of Coded Image:",bg='black',fg="white",font=("Impact",25,tk.UNDERLINE))
            newfile.pack(pady=20)

            n_name=tk.Entry(body)
            n_name.config(width=30,bg='white',fg='black',bd=0,font=("Bell TM",12))
            n_name.pack(pady=10)

            encode_data=tk.Button(body,text="ENCODE DATA",font=("Impact",24),fg="black",bg='white',activebackground='red',bd=0,command=data)
            encode_data.pack(pady=40)

            menu.pack(side=tk.LEFT,fill=tk.Y)
            body.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)


    class Decode(tk.Frame):
        bg3=0
        def __init__(self, parent, controller):
            global bg3
            tk.Frame.__init__(self,parent,bg='black') 

            menu=tk.Frame(self,bg='black',height=100,width=100,highlightthickness=2,highlightbackground='red')

            canvas=tk.Canvas(menu,width=400, height=333,highlightthickness=0)
            canvas.config(bg='black')
            bg3=tk.PhotoImage(file='bg.png')
            canvas.create_image(0,0,image=bg3,anchor=tk.NW)
            canvas.pack()


            encode=tk.Button(menu,text="ENCODE",font=("Bell TM",24),fg="red",bg='black',activebackground='red',bd=0,command=lambda: controller.show_frame(Encode))

            decode=tk.Button(menu,text="DECODE",font=("Bell TM",24),fg="black",bg='red',bd=0,activebackground='red')

            about=tk.Button(menu,text="ABOUT",font=("Bell TM",24),fg="red",bg='black',bd=0,activebackground='red',command=lambda: controller.show_frame(About))

            quit=tk.Button(menu,text="QUIT",font=("Bell TM",24),fg="red",bg='black',bd=0,activebackground='red',command=lambda: controller.destroy())
            version=tk.Label(menu,text="Version = 1.1_087beta012",bg='black',fg="red",font=("Bell TM",16))

            Status=tk.Label(menu,text="Status: Not Decoded",bg='black',fg="red",font=("Impact",20,))
            Status.pack(pady=20)

            encode.pack(pady=10)

            decode.pack(pady=10)

            about.pack(pady=10)

            quit.pack(pady=10)

            version.pack(pady=50)

            body=tk.Frame(self,bg='black',height=100,width=100,highlightthickness=0,highlightbackground='red')

            choose_file=tk.Label(body,text="Encoded Image:",bg='black',fg="white",font=("Impact",25,tk.UNDERLINE))
            choose_file.pack(pady=10)

            filename1=''
            x11=''
            a11=''
            

            def data():
                try:
                    global x11
                    global filename1
                    i=(filename1)
                    x11=Engine.decode(i)
                    if len(x11)==1:
                        raise ValueError
                    st.config(state='normal')
                    st.insert(1.0,str(x11))
                    Status.config(text="Status: Data Decoded ✔",fg='green')
                    st.config(state='disable')
                except OSError:
                    tkinter.messagebox.showwarning("No Image Found!", "Choose An Image File")
                except NameError:
                    tkinter.messagebox.showwarning("Incorrect Directory!", "Enter Image Location")
                except ValueError:
                    tkinter.messagebox.showwarning("No Data To Decode", "Choose Another file!")

            def store():
                try:
                    global x11
                    if len(x11)==1:
                            raise NameError
                    
                    def ss():
                        try:
                            global x11
                            global a11
                            if len(n_name.get())==0:
                                raise ValueError
                            a11=n_name.get()+'.txt'
                            Engine.create(a11,x11)
                            Status.config(text="Status: File Saved ✔",fg='green')
                            root1.destroy()
                        except ValueError:
                            tkinter.messagebox.showwarning("No Name!", "Enter Some File Name!")
                            root1.destroy()
                        
                    
                    root1=tk.Tk()
                    root1.geometry('200x200')
                    root1.configure(bg='black')

                    name1=tk.Label(root1,text="File Name:",bg='black',fg="red",font=("Impact",25,tk.UNDERLINE))
                    name1.pack(pady=10)

                    n_name=tk.Entry(root1)
                    n_name.config(bg='red',fg='white',bd=0,font=("Bell TM",10),insertbackground='white')
                    n_name.pack(pady=10)

                    enterdata=tk.Button(root1,text="Submit",font=("Impact",16),fg="black",bg='red',activebackground='red',bd=0,command=ss)
                    enterdata.pack(pady=20)

                    
                    
                    root1.mainloop()
                except NameError:
                            tkinter.messagebox.showwarning("No Data", "Decode First to store data!")
                    
                    


                
            def browsefunc():
                global filename1
                filename1 = filedialog.askopenfilename()
                pathlabel.config(text=filename1)

            browsebutton = tk.Button(body,text="Browse",font=("Impact",15),fg="black",bg='white',activebackground='red',bd=0, command=browsefunc)
            pathlabel = tk.Label(body,bg='white',bd=2,fg='black',width=40)
            pathlabel.config(font=("Bell TM",12))
            pathlabel.pack(pady=10)
            browsebutton.pack(pady=10)

            data_msg=tk.Label(body,text="Decoded Data:",bg='black',fg="white",font=("Impact",25,tk.UNDERLINE))
            data_msg.pack(pady=20)

            st = ScrolledText(body, height=20,width=50,bg='white',fg='black',bd=0)
            st.config(insertbackground='black',font=("Bell TM",12),state='disable')
            st.pack(pady=10)

            bottom=tk.Frame(body,bg='black')

            decode_data=tk.Button(bottom,text="DECODE DATA",font=("Impact",20),fg="black",bg='white',activebackground='red',bd=0,command=data)
            decode_data.grid(row=0,column=0,padx=10,pady=20)

            file_data=tk.Button(bottom,text="STORE DATA",font=("Impact",20),fg="black",bg='RED',activebackground='red',bd=0,command=store)
            file_data.grid(row=0,column=2,padx=10,pady=20)
            
            bottom.pack()
            menu.pack(side=tk.LEFT,fill=tk.Y)
            body.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)

           

    app = MainWindow()
    app.configure(bg='black')
    app.attributes('-fullscreen',True)
    app.mainloop()

except ValueError :
    print("UnknownError")
