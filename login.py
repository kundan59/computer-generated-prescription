#Python Tkinter and Sqlite3
#Made 

#imports
from tkinter import *
from tkinter import messagebox as ms

import form
import sqlite3
import os
from PIL import ImageTk,Image
import qrcode
import pyautogui
import speech_recognition as sr
from pygame import mixer



# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL ,password TEXT NOT NULL);')
db.commit()
db.close()

with sqlite3.connect('medi.db') as db1:
    d= db1.cursor()

d.execute('CREATE TABLE IF NOT EXISTS medi(Hospital_Name TEXT NOT NULL ,Doctor_Name TEXT NOT NULL,Paitent_Name TEXT NOT NULL,Date TEXT NOT NULL ,Drugs1 TEXT NOT NULL,Drugs2 TEXT NOT NULL,Drugs3 TEXT NOT NULL,Drugs4 TEXT NOT NULL,Quantity1 TEXT NOT NULL,Quantity2 TEXT NOT NULL,Quantity3 TEXT NOT NULL,Quantity4 TEXT NOT NULL);')
db1.commit()
db1.close()

#main Class
class main():
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()
        self.Hospital_Name = StringVar()
        self.Doctor_Name = StringVar()
        self.Paitent_Name = StringVar()
        self.Date = StringVar()
        self.Drugs1= StringVar()
        self.Drugs2= StringVar()
        self.Drugs3= StringVar()
        self.Drugs4= StringVar()
      
       
        self.Quantity1=StringVar()
        self.Quantity2=StringVar()
        self.Quantity3=StringVar()
        self.Quantity4=StringVar()
        self.Age=StringVar()
        self.sex=StringVar()
        
      
        self.suggest= StringVar()
        #Create Widgets
       ## self.widgets1()
        self.window_title = "gewizzede"
        self.postscript_file = "tmp_snapshot.ps"

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            window.title('Form')
            self.logf.pack_forget()
            self.head.pack_forget()

            self.head = Label(self.master,text = 'PRESCRIPTION',font = ('freesansbold',35),pady = 10)
            self.head.pack()
            self.goff = Frame(self.master,padx =10,pady = 10)
            self.photo=PhotoImage(file='microphone.png').subsample(10,10)
            Label(self.goff,text = 'Hospital: ',font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W)
            Entry(self.goff,textvariable = self.Hospital_Name,bd = 5,font = ('freesansbold',15)).grid(row=0,column=1,sticky=W)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=0,column=2,sticky=W)

            Label(self.goff,text = 'Doctor: ',font = ('freesansbold',15),pady=5,padx=5).grid(row=0,column=3,sticky = W)
            Entry(self.goff,textvariable = self.Doctor_Name,bd = 5,font = ('freesansbold',10)).grid(row=0,column=4,sticky='W')
            

            Label(self.goff,text = 'Date: ',font = ('freesansbold',20),pady=5,padx=5).grid(row=1,column=0,sticky = W)
            Entry(self.goff,textvariable = self.Date,bd = 5,font = ('freesansbold',15)).grid(row=1,column=1)

            Label(self.goff,text = 'Paitent Name: ',font = ('freesansbold',15),pady=5,padx=5).grid(row=1,column=3,sticky = W)
            Entry(self.goff,textvariable = self.Paitent_Name,bd = 4,font = ('freesansbold',10)).grid(row=1,column=4)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=1,column=5,sticky=W)

            Label(self.goff,text = 'Age: ',font = ('freesansbold',20),pady=5,padx=5).grid(row=2,column=0,sticky = W)
            Entry(self.goff,textvariable = self.Age,bd = 5,font = ('freesansbold',15)).grid(row=2,column=1)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=2,column=2,sticky=W)

            

            Label(self.goff,text = 'Prescribed Medicines:- ',font = ('freesansbold',35),pady=10,padx=10).grid(row=3,column=0,sticky = W)

            Label(self.goff,text = 'Drug 1: ',font = ('freesansbold',20),pady=5,padx=5).grid(row=4,column=0,sticky = W)
            Entry(self.goff,textvariable = self.Drugs1,bd = 5,font = ('freesansbold',15)).grid(row=4,column=1)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=4,column=2,sticky=W)
            Label(self.goff,text="- QTY: ",font = ('freesansbold',15),pady=5,padx=5).grid(row=4,column=3,sticky = W)
            Entry(self.goff,textvariable = self.Quantity1,bd = 4,font = ('freesansbold',10)).grid(row=4,column=4)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=4,column=5,sticky=W)

            Label(self.goff,text = 'Drug 2: ',font = ('freesansbold',20),pady=5,padx=5).grid(row=5,column=0,sticky = W)
            Entry(self.goff,textvariable = self.Drugs2,bd = 5,font = ('freesansbold',15)).grid(row=5,column=1)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=5,column=2,sticky=W)
            
            Label(self.goff,text="- QTY: ",font = ('freesansbold',15),pady=5,padx=5).grid(row=5,column=3,sticky = W)
            Entry(self.goff,textvariable = self.Quantity2,bd = 4,font = ('freesansbold',10)).grid(row=5,column=4)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=5,column=5,sticky=W)

            Label(self.goff,text = 'Drug 3: ',font = ('freesansbold',20),pady=5,padx=5).grid(row=6,column=0,sticky = W)
            Entry(self.goff,textvariable = self.Drugs3,bd = 5,font = ('freesansbold',15)).grid(row=6,column=1)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=6,column=2,sticky=W)

            Label(self.goff,text="- QTY: ",font = ('freesansbold',15),pady=5,padx=5).grid(row=6,column=3,sticky = W)
            Entry(self.goff,textvariable = self.Quantity3,bd = 4,font = ('freesansbold',10)).grid(row=6,column=4)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=6,column=5,sticky=W)

            Label(self.goff,text = 'Drug 4: ',font = ('freesansbold',20),pady=5,padx=5).grid(row=7,column=0,sticky = W)
            Entry(self.goff,textvariable = self.Drugs4,bd = 5,font = ('freesansbold',15)).grid(row=7,column=1)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=7,column=2,sticky=W)
            Label(self.goff,text="- QTY: ",font = ('freesansbold',15),pady=5,padx=5).grid(row=7,column=3,sticky = W)
            Entry(self.goff,textvariable = self.Quantity4,bd = 4,font = ('freesansbold',10)).grid(row=7,column=4)
            Button(self.goff,image=self.photo,command=self.buttonclick,bd=0,activebackground='#b7acac',overrelief='groove',relief='sunken').grid(row=7,column=5,sticky=W)

            Label(self.goff,text="Suggestion-: ",font = ('freesansbold',35),pady=5,padx=5).grid(row=8,column=0,sticky = W)
            Text(self.goff,height=5,width=50,font = ('freesansbold',15)).grid(row=10,column=0)
            Button(self.goff,text = 'SUBMIT',bd = 3 ,font = ('freesansbold',15),padx=5,pady=5,command=self.setf).grid(row=9,column=3)

            Label(self.goff,text="Sex: ",font = ('freesansbold',15),pady=5,padx=5).grid(row=2,column=3,sticky = W)
            Radiobutton(self.goff,text="Male",variable=self.sex,value='male',font = ('freesansbold',10),pady=5,padx=5).grid(row=2,column=4,sticky='W')
            Radiobutton(self.goff,text="Female",variable=self.sex,value='female',font = ('freesansbold',10),pady=5,padx=5).grid(row=2,column=5,sticky='W')
            

            self.goff.pack()

            
                

            
           
           
            
        else:
            ms.showerror('Oops!','Username Not Found.')

    #def sel(self):
        #self.label.config(text=selection)
    def buttonclick(self):
        pass

    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('freesansbold',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('freesansbold',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('freesansbold',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('freesansbold',15),padx=5,pady=5,command=self.login).grid(row=2)
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('freesansbold',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('freesansbold',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('freesansbold',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('freesansbold',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('freesansbold',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

         
    def setf(self):
         with sqlite3.connect('medi.db') as db1:
             d = db1.cursor()
           
         
            
         insert = 'INSERT INTO medi(Hospital_Name,Doctor_Name,Paitent_Name,Date,Drugs1,Drugs2,Drugs3,Drugs4,Quantity1,Quantity2,Quantity3,Quantity4) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'
         d.execute(insert,[(self.Hospital_Name.get()),(self.Doctor_Name.get()),(self.Paitent_Name.get()),(self.Date.get()),(self.Drugs1.get()),(self.Drugs2.get()),(self.Drugs3.get()),(self.Drugs4.get()),(self.Quantity1.get()),(self.Quantity2.get()),(self.Quantity3.get()),(self.Quantity4.get())])
         db1.commit()
         window.title('Prescription')
         self.logf.pack_forget()
         self.goff.pack_forget()
         self.head.pack_forget()
         self.topf = Frame(self.master,padx =10,pady = 10)
        
         self.img1 = ImageTk.PhotoImage(Image.open("doctor-logo-hi 1.png"))
         
         Label(self.topf,image=self.img1).grid(sticky=W,row=0,column=0)
         
         Label(self.topf,textvariable =self.Hospital_Name,font = ('freesansbold',30),pady=5,padx=5).grid(sticky = W,row=0,column=2)
         
         self.img2 = ImageTk.PhotoImage(Image.open("nm.jpeg"))
         
         Label(self.topf,image=self.img2).grid(sticky=W,row=0,column=4)

         Label(self.topf,text='HEALTH IS WEALTH',font=('freesansbold',25),pady=5,padx=5).grid(sticky = W,row=1,column=2)
         Label(self.topf,text='Paitent Name: ',font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=3,column=0)
         Label(self.topf,textvariable =self.Paitent_Name,font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=3,column=1)
         Label(self.topf,text='Paitent ID : SH100265 ',font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=3,column=4)
         Label(self.topf,text='Age: ',font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=4,column=0)
         Label(self.topf,textvariable =self.Age,font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=4,column=1)
         Label(self.topf,text='Sex:',font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=4,column=2)
         Label(self.topf,textvariable =self.sex,font = ('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=4,column=3)
         Label(self.topf,text='Date: ',font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=4,column=4)
         Label(self.topf,textvariable=self.Date,font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=4,column=5)

         Label(self.topf,text='Rx',font=('freesansbold',25),pady=5,padx=5).grid(sticky = W,row=5,column=0)

         Label(self.topf,textvariable=self.Drugs1,font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=6,column=0)
         Label(self.topf,textvariable=self.Quantity1,font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=6,column=1)

         Label(self.topf,textvariable=self.Drugs2,font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=7,column=0)
         Label(self.topf,textvariable=self.Quantity2,font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=7,column=1)
 
         Label(self.topf,textvariable=self.Drugs3,font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=8,column=0)
         Label(self.topf,textvariable=self.Quantity3,font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=8,column=1)

         Label(self.topf,textvariable=self.Drugs4,font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=9,column=0)
         Label(self.topf,textvariable=self.Quantity4,font=('freesansbold',20),pady=5,padx=5).grid(sticky = W,row=9,column=1)

         qr = qrcode.QRCode(version = 1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size = 2,border = 1)
         #data =str([self.Hospital_Name.get(),self.Paitent_Name.get(),self.Date.get(),'age:23','sex:male',self.Drugs1.get(),self.Drugs2.get(),self.Drugs3.get(),self.Drugs4.get(),self.Quantity1.get(),self.Quantity2.get(),self.Quantity3.get(),self.Quantity4.get()])
         data={"paiten-id":"ch100265","date":self.Date.get(),"m1":self.Drugs1.get(),"m12":self.Quantity1.get(),"m2":self.Drugs2.get(),"m22":self.Quantity2.get()}
         qr.add_data(data)
         qr.make(fit=True)
         img = qr.make_image()
         img.save("image.png")

         self.img3 = ImageTk.PhotoImage(Image.open("image.png"))
         
         Label(self.topf,image=self.img3).grid(sticky=W,row=8,column=3)

         
         Button(self.topf,text = 'print',bd = 3 ,font = ('freesansbold',15),padx=5,pady=5,command=self.generete_pdf).grid(row=9,column=2)


         
         self.topf.pack()
         
   
   
    def generete_pdf(self):
        pic = pyautogui.screenshot()
        pic.save('Screenshot.png') 
        os.startfile('Screenshot.png')
        
    def gof(self):

         self.Hospital_Name.set('')
         self.Doctor_Name.set('')
         self.Paitent_Name.set('')
         self.Date.set('')
         self.Drugs1.set('')
         self.Drugs2.set('')
         self.Drugs3.set('')
         self.Drugs4.set('')
         self.Quantity1.set('')
         self.Quantity2.set('')
         self.Quantity3.set('')
         self.Quantity4.set('')

           
         
         self.goff.pack()
         self.setf() 

    def view():
        with sqlite3.connect('medi.db') as db1:
           d = db1.cursor()
        d.execute('SELECT * FROM medi')
        rows=d.fetchall()
      
        db1.close()
        return rows
    print(view())

    def views():
        with sqlite3.connect('quit.db') as db:
           c = db.cursor()
        c.execute('SELECT * FROM user')
        rows=c.fetchall()
      
        db.close()
        return rows
    print(views())

if __name__ == '__main__':
	#Create Object
	#and setup window
    window = Tk()
    pyexec = sys.executable
    window.title('LOGIN Form')
   # window.geometry('400x350+300+300')
    main(window)
    #root.mainloop()﻿
