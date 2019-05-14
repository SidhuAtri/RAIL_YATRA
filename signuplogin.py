from tkinter import *
import sqlite3
import tkinter.messagebox

def man():
    r2.destroy()
    
    def valid():
        
        conn=sqlite3.connect('reg.db')
        cursor = conn.cursor()
        cursor.execute("select password from datainfo where username ='%s'"% usern.get())
        p=cursor.fetchone()
        if(p[0]==pasword.get()):
            tkinter.messagebox.showinfo("Done" , "Login Successfull")
            r1.destroy()
        
        else:
              tkinter.messagebox.showinfo("Error" , "Invalid Username or password")

    r1=Tk()
    r1.configure(background = "bisque")
    r1.geometry('400x500')
    ll = Label(r1,text = "LOGIN !",height = 3 , width = 28 ,font = ('Ariel black',22,'bold'),fg = 'Black',bg="gold")
    ll.pack()

    user = Label(r1,text = "Username : ",font = ('Ariel black',14,'bold'))
    user.place(x=60,y=200)

        
    usern = Entry(r1)
    usern.place(x=180,y=200)

    passs= Label(r1,text = "Password : ",font = ('Ariel black',14,'bold'))
    passs.place(x=60,y=280)
        
    pasword = Entry(r1)
    pasword.place(x=180,y=280)

    b= Button(r1,text = "Login" , command = valid,font = ('Ariel black',16,'bold'),bg="tomato")
    b.place(x=150,y=380)

    
def main():
    def con():
    
          
       conn=sqlite3.connect('reg.db')
       cursor = conn.cursor()
            

       #cursor.execute("CREATE TABLE  datainfo (name text  ,age  text  ,username text ,password text)")

       cursor.execute('INSERT INTO  datainfo (name,age,username,password) VALUES(?,?,?,?)',[namee.get(),agee.get(),usernamee.get(),passworde.get()])
       cursor.execute("SELECT * FROM datainfo")

       conn.commit()
       tkinter.messagebox.showinfo("Done" , "Signup Successfull")
       
       
    
    
    r=Tk()
    r.geometry('400x500')

    l = Label(r,text = "SIGN UP HERE !",height = 3 , width = 28 ,font = ('Ariel black',22,'bold'),fg = 'Black',bg="gold")
    l.pack()
    name = Label(r,text = "Name : ",font = ('Ariel black',12,'bold'))
    name.place(x=60,y=130)
    namee = Entry(r)
    namee.place(x=190,y=130)

    age  = Label(r,text = "Age : ",font = ('Ariel black',12,'bold'))
    age.place(x=60,y=200)
    agee = Entry(r)
    agee.place(x=190,y=200)

    username = Label(r,text = "Username : ",font = ('Ariel black',12,'bold'))
    username.place(x=60,y=270)
    usernamee = Entry(r)
    usernamee.place(x=190,y=270)

    password = Label(r,text = "Password : ",font = ('Ariel black',12,'bold'))
    password.place(x=60,y=340)
    passworde = Entry(r)
    passworde.place(x=190,y=340)

    b1= Button(r,text = "Sign Up" ,font = ('Ariel black',16,'bold'), command =con,bg="pink")
    b1.place(x=140,y=410)
    







r2=Tk()
f = Frame(r2, height = 300 ,width = 500,bg ="maroon")
f.pack()

label = Label(r2 ,text = "Government Of INDIA",height = 4 , width = 28 ,font = ('Ariel black',22,'bold'),fg = 'white',bg="blue")
label.place(x=0 ,y=-20)

label = Label(r2,text = "Railway Management System",height = 2 , width = 30 ,font = ('Copper Black',17,'bold'),fg = 'Green',bg="AliceBlue")
label.place(x=30,y=100)

b1 = Button(r2, text = "Signup !",height = 2 , width = 10 , font = ('Times',17,'bold'),bg ='pink',command = main)
b1.place(x= 50 , y = 190)

b2 = Button(r2, text = "Login !",height = 2 , width = 10, font = ('Times',17,'bold'),bg ='pink',command =man)
b2.place(x= 280 , y = 190)


r2.mainloop()

