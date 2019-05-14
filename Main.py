from tkinter import *
import sqlite3
import tkinter.messagebox
from tkinter import messagebox
from tkinter import  Tk,ttk,StringVar
import random
import time;
import datetime



def man():
    global operator
    
    root =Tk()
    root.geometry("1350x750+0+0")
    root.title("Train Ticket")
    root.configure(background='black')

    Top = Frame(root,width=1350,height =100,bd=14,relief ="raise")
    Top.pack(side=TOP)

    f1= Frame(root,width=900,height =650,bd=8,relief ="raise")
    f1.pack(side=LEFT)
    f2= Frame(root,width=440,height =650,bd=8,relief ="raise")
    f2.pack(side=RIGHT)

    ftopright= Frame(f2,width=500,height =650,bd=12,relief ="raise")
    ftopright.pack(side=TOP)
    fbottomright= Frame(f2,width=500,height =50,bd=20,relief ="raise")
    fbottomright.pack(side=BOTTOM)

    f1a= Frame(f1,width=900,height =330,bd=8,relief ="raise")
    f1a.pack(side=TOP)
    f2a= Frame(f1,width=900,height =320,bd=6,relief ="raise")
    f2a.pack(side=BOTTOM)

    topleft1= Frame(f1a,width=300,height =200,bd=8,relief ="raise")
    topleft1.pack(side=LEFT)
    topleft2= Frame(f1a,width=300,height =200,bd=8,relief ="raise")
    topleft2.pack(side=RIGHT)
    topleft3= Frame(f1a,width=300,height =200,bd=8,relief ="raise")
    topleft3.pack(side=RIGHT)

    bottomleft1= Frame(f2a,width=450,height =450,bd=14,relief ="raise")
    bottomleft1.pack(side=LEFT)
    bottomleft2= Frame(f2a,width=450,height =450,bd=14,relief ="raise")
    bottomleft2.pack(side=RIGHT)

    Top.configure(background = "orange")
    f1.configure(background = "Black")
    f2.configure(background = "Black")

    lbltitle=Label(Top,font=('arial',40,"bold"),text = "Train Ticketing System",bd=10,width =41,justify = "center")
    lbltitle.grid(row = 0 , column = 0 )

#--------------------------------------------------------------------VARIABLES-----------------------------------------------------------

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = StringVar()
    var8 = StringVar()
    var9 = StringVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    route = StringVar()
    tax= StringVar()
    subtotal= StringVar()
    ticketclass= StringVar()
    ticketprice= StringVar()
    childticket= StringVar()
    adultticket= StringVar()
    fromdestination= StringVar()
    todestination= StringVar()
    feeprice= StringVar()
    x= StringVar()
    person = IntVar()

    receiptref=StringVar()



    text_input = StringVar()
    operator= ""
    date1 = StringVar()
    time1 = StringVar()


    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var9.set("0")
    var12.set("0")
    var10.set("0")
    var11.set("0")
    person.set("")

 
#--------------------------------------------------------------------FUNCTIONS----------------------------------------------------------

    def btnclick(numbers):
           global operator
           operator = operator + str(numbers)
           text_input.set(operator)

    def btncleardisplay():
           global operator
           operator =" "
           text_input.set(" ")

    def btnequal():
           global operator
           sumup= str(eval(operator))
           text_input.set(sumup)
           operator =" "

    def iexit():
           qexit = messagebox.askyesno("Quit System","Do U want to Quit ?")
           if qexit >0:
                      root.destroy()
                      return
    def travelcost():
        if(var9.get() == "Delhi" and var1.get() == 1 and var4.get() == 1):
                      tcost = float(300.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("Standard")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Delhi")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Delhi" and var3.get() == 1 and var4.get() == 1 ):
                      tcost = float(1000.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("First Class")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Delhi")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Delhi" and var2.get() == 1 and var4.get() == 1):
                      tcost = float(450.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("Economy")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Delhi")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
                      

    
                      
        elif(var9.get() == "Delhi" and var1.get() == 1  and var5.get() == 1):
                      tcost = float(250.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("Standard")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Delhi")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
    
        elif(var9.get() == "Delhi" and var2.get() == 1  and var5.get() == 1):
                      tcost = float(300.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("Economy")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Delhi")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Delhi" and var3.get() == 1  and var5.get() == 1):
                      tcost = float(800.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("First Class")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Delhi")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
#--------------------------------------------------------------------PUNE----------------------------------------------------------

        elif(var9.get() == "Pune" and var1.get() == 1 and var4.get() == 1):
                      tcost = float(500.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("Standard")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Pune")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Pune" and var2.get() == 1 and var4.get() == 1):
                      tcost = float(650.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("Economy")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Pune")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Pune" and var3.get() == 1 and var4.get() == 1):
                      tcost = float(1400.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("First Class")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Pune")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
                      
        elif(var9.get() == "Pune" and var1.get() == 1  and var5.get() == 1):
                      tcost = float(300.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("Standard")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Pune")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
    
        elif(var9.get() == "Pune" and var2.get() == 1  and var5.get() == 1):
                      tcost = float(450.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("Economy")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Pune")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Pune" and var3.get() == 1  and var5.get() == 1):
                      tcost = float(1600.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("First Class")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Pune")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

#--------------------------------------------------------------------Banglore----------------------------------------------------------

        elif(var9.get() == "Banglore" and var1.get() == 1 and var4.get() == 1):
                      tcost = float(1500.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("Standard")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Banglore")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Banglore" and var2.get() == 1 and var4.get() == 1):
                      tcost = float(1800.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("Economy")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Banglore")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Banglore" and var3.get() == 1 and var4.get() == 1):
                      tcost = float(2800.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("First Class")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Banglore")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
                      
        elif(var9.get() == "Banglore" and var1.get() == 1  and var5.get() == 1):
                      tcost = float(1000.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("Standard")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Banglore")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
    
        elif(var9.get() == "Banglore" and var2.get() == 1  and var5.get() == 1):
                      tcost = float(1300.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("Economy")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Banglore")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Banglore" and var3.get() == 1  and var5.get() == 1):
                      tcost = float(2500.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("First Class")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Banglore")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

#--------------------------------------------------------------------Mumbai----------------------------------------------------------

        elif(var9.get() == "Mumbai" and var1.get() == 1 and var4.get() == 1):
                      tcost = float(1200.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("Standard")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Mumbai")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Mumbai" and var2.get() == 1 and var4.get() == 1):
                      tcost = float(1500.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("Economy")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Mumbai")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Mumbai" and var3.get() == 1 and var4.get() == 1):
                      tcost = float(2500.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("First Class")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Mumbai")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
                      
        elif(var9.get() == "Mumbai" and var1.get() == 1  and var5.get() == 1):
                      tcost = float(800.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("Standard")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Mumbai")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
    
        elif(var9.get() == "Mumbai" and var2.get() == 1  and var5.get() == 1):
                      tcost = float(1000.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("Economy")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Mumbai")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Mumbai" and var3.get() == 1  and var5.get() == 1):
                      tcost = float(2000.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("First Class")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Mumbai")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)


#--------------------------------------------------------------------Hyderabad----------------------------------------------------------

        elif(var9.get() == "Hyderabad" and var1.get() == 1 and var4.get() == 1):
                      tcost = float(2000.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("Standard")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Hyderabad")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Hyderabad" and var2.get() == 1 and var4.get() == 1):
                      tcost = float(2300.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("Economy")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Hyderabad")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Hyderabad" and var3.get() == 1 and var4.get() == 1):
                      tcost = float(3500.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      adulttax = "Rs." ,str("%.2f"%((tcost *single*0.05) +(tcost *rr*0.05)))
                      adultfees = "Rs." ,str("%.2f"%((tcost *single) + (tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.05) + (tcost *rr)+ (tcost *rr*0.05)
                      nn=int(rr+single)
                      person.set(nn)

                      tax.set(adulttax)
                      subtotal.set(adultfees)
                      ticketclass.set("First Class")
                      ticketprice.set(adultfees)
                      childticket.set("No")
                      adultticket.set("Yes")
                      fromdestination.set("Rajasthan")
                      todestination.set("Hyderabad")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
                      
        elif(var9.get() == "Hyderabad" and var1.get() == 1  and var5.get() == 1):
                      tcost = float(1500.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("Standard")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Hyderabad")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)
    
        elif(var9.get() == "Hyderabad" and var2.get() == 1  and var5.get() == 1):
                      tcost = float(2000.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("Economy")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Hyderabad")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)

        elif(var9.get() == "Hyderabad" and var3.get() == 1  and var5.get() == 1):
                      tcost = float(3200.50)
                      single = float(var12.get())
                      rr = float(var6.get())
                      childtax = "Rs." ,(tcost *single)*0
                      childfees = "Rs." ,str("%.2f"%((tcost *single)+(tcost *rr)))
                      totalcost = "Rs." ,(tcost *single)+ ((tcost *single)*0.0)+(tcost *rr)+ ((tcost *rr)*0.0)
                      nn=int(rr+single)
                      person.set(nn)
                      tax.set(childtax)
                      subtotal.set(childfees)
                      ticketclass.set("First Class")
                      ticketprice.set(childfees)
                      childticket.set("Yes")
                      adultticket.set("No")
                      fromdestination.set("Rajasthan")
                      todestination.set("Hyderabad")
                      feeprice.set(totalcost)
                      total.set(totalcost)
                      route.set("Direct")

                      x=random.randint(109,5876)
                      randomref = str(x)
                      receiptref.set("TFL" + randomref)


    def reset():
           var1.set("0")
           var2.set("0")
           var3.set("0")
           var4.set("0")
           var5.set("0")
           var6.set("0")
           var7.set("")
           var9.set("")
           var10.set("0")
           var8.set(" ")
           var11.set("0")
           var12.set("0")
           date1.set(time.strftime("%d/%m/%Y"))
           time1.set(time.strftime("%H: %M :%S"))
           ticketclass.set("")
           ticketprice.set("")
           childticket.set("")
           adultticket.set("")
           fromdestination.set("")
           todestination.set("")
           feeprice.set("")
           person.set("")
           receiptref.set("")
           tax.set("")
           subtotal.set("")
           total.set("")
           route.set("")

           

    def chkbutton1():
           if(var10.get() == 1 ):
                      var12.set(" ")
                      entsingle.configure(state = NORMAL)
           elif(var10.get() == 0 ):
                      var12.set("0")
                      entsingle.configure(state = DISABLED)
                      
    def chkbutton():
           if(var11.get() == 1 ):
                      var6.set(" ")
                      entreturn.configure(state = NORMAL)
           elif(var11.get() == 0 ):
                      var6.set("0")
                      entreturn.configure(state = DISABLED)


                                       

#--------------------------------------------------------------------Right----------------------------------------------------------



    lblreceipt=Label(ftopright,font=('arial ',20,"bold"),text = "Traveller Ticket",width =19,height =4,justify = "center")
    lblreceipt.grid(row = 0 , column = 0 )

    lblclass=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "Class",width =10,justify = "center",relief = "sunken")
    lblclass.grid(row = 0 , column = 0 )
    lblclass2=Label(fbottomright,font=('arial ',12,"bold"),width =10,textvariable = ticketclass,justify = "center",relief = "sunken")
    lblclass2.grid(row = 1 , column = 0 )

    lblticket=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "Ticket",width =10,justify = "center",relief = "sunken")
    lblticket.grid(row = 0 , column = 1 )
    lblticket2=Label(fbottomright,font=('arial ',12,"bold"),width =10,textvariable = ticketprice,justify = "center",relief = "sunken")
    lblticket2.grid(row = 1 , column = 1 )


    lbladult=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "Adult",width =10,justify = "center",relief = "sunken")
    lbladult.grid(row = 0 , column = 2 )
    lbladult2=Label(fbottomright,font=('arial ',12,"bold"),width =10,justify = "center",textvariable = adultticket,relief = "sunken")
    lbladult2.grid(row = 1 , column = 2 )

    lblspace= Label(fbottomright,font=('arial',5,"bold"),text = " \n",bd=2)
    lblspace.grid(row = 2,column=2)

    lblchild=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "Child",width =10,justify = "center",relief = "sunken")
    lblchild.grid(row = 3 , column = 0 )
    lblchild2=Label(fbottomright,font=('arial ',12,"bold"),width =10,justify = "center",textvariable = childticket,relief = "sunken")
    lblchild2.grid(row = 4 , column = 0 )

    lblspace= Label(fbottomright,font=('arial',5,"bold"),text = " \n",bd=0)
    lblspace.grid(row = 5,column=2)


    lblfrom=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "From",width =10,justify = "center",relief = "sunken")
    lblfrom.grid(row = 3 , column = 1 )
    lblfrom2=Label(fbottomright,font=('arial ',12,"bold"),width =10,justify = "center",textvariable =fromdestination,relief = "sunken")
    lblfrom2.grid(row = 4 , column = 1 )

    lblto=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "To",width =10,justify = "center",relief = "sunken")
    lblto.grid(row = 3 , column = 2 )
    lblto2=Label(fbottomright,font=('arial ',12,"bold"),width =10,justify = "center",textvariable =todestination,relief = "sunken")
    lblto2.grid(row = 4 , column = 2 )

    lblprice=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "Price",width =10,justify = "center",relief = "sunken")
    lblprice.grid(row = 6, column = 0 )
    lblprice2=Label(fbottomright,font=('arial ',12,"bold"),width =10,justify = "center",textvariable = feeprice,relief = "sunken")
    lblprice2.grid(row = 7 , column = 0 )

    lblref=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "Ref. No.",width =10,justify = "center",relief = "sunken")
    lblref.grid(row = 6, column = 1 )
    lblref2=Label(fbottomright,font=('arial ',12,"bold"),width =10,justify = "center",textvariable = receiptref,relief = "sunken")
    lblref2.grid(row = 7 , column = 1 )

    lblno=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "Person",width =10,justify = "center",relief = "sunken")
    lblno.grid(row = 6, column = 2 )
    lblno2=Label(fbottomright,font=('arial ',12,"bold"),width =10,justify = "center",textvariable = person,relief = "sunken")
    lblno2.grid(row = 7 , column = 2 )

    lblspace= Label(fbottomright,font=('arial',8,"bold"),text = " \n",bd=0)
    lblspace.grid(row = 8,column=0)

    lbltime=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "Time",width =10,justify = "center",relief = "sunken")
    lbltime.grid(row = 9 , column = 0 )
    lbltime2=Label(fbottomright,font=('arial ',12,"bold"),width =10,justify = "center",relief = "sunken",
               textvariable = time1)
    lbltime2.grid(row = 10 , column = 0 )

    lblDate=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "Date",width =10,justify = "center",relief = "sunken")
    lblDate.grid(row = 9 , column = 1 )
    lblDate2=Label(fbottomright,font=('arial ',12,"bold"),width =10,justify = "center",relief = "sunken" ,
               textvariable = date1)
    lblDate2.grid(row = 10 , column = 1 )

    lblroute=Label(fbottomright,font=('arial ',12,"bold"),bg ="silver",text = "Route",width =10,justify = "center",relief = "sunken")
    lblroute.grid(row = 9 , column = 2 )
    lblroute2=Label(fbottomright,font=('arial ',12,"bold"),width =10,justify = "center",relief = "sunken",textvariable = route)
    lblroute2.grid(row = 10 , column = 2 )



#--------------------------------------------------------------------Date and time--------------------------------------------------
    date1.set(time.strftime("%d/%m/%Y"))
    time1.set(time.strftime("%H: %M :%S"))

#--------------------------------------------------------------------CREATE WIDGET topleft1--------------------------------------------------

    lblClass = Label(topleft1,font=('arial',22,"bold"),text = "Class",bd=8)
    lblClass.grid(row = 0,column=0,sticky=W)

    chkstandard = Checkbutton(topleft1,font=('arial',20,"bold"),text = "Standard", variable = var1 , onvalue =1 ,offvalue = 0)
    chkstandard.grid(row = 1,column=0,sticky=W)
    chkeconomy = Checkbutton(topleft1,font=('arial',20,"bold"),text = "Economy", variable = var2 , onvalue =1 ,offvalue = 0)
    chkeconomy.grid(row = 2,column=0,sticky=W)
    chkfirstclass = Checkbutton(topleft1,font=('arial',20,"bold"),text = "First Class", variable = var3 , onvalue =1 ,offvalue = 0)
    chkfirstclass.grid(row = 3,column=0,sticky=W)

#--------------------------------------------------------------------CREATE WIDGET topleft2--------------------------------------------------

    lblseldest = Label(topleft3,font=('arial',20,"bold"),text = "Destination Selector",bd=8)
    lblseldest.grid(row = 0,column=0,sticky=W,columnspan =2)

    lbldest = Label(topleft3,font=('arial',20,"bold"),text = "Destination",bd=8)
    lbldest.grid(row = 1,column=0,sticky=W)

    cbmdest = ttk.Combobox(topleft3 , textvariable = var9 ,state = "readonly",font=('arial',20,"bold"),width = 10)
    cbmdest["value"]=(" ","Delhi","Pune","Banglore","Mumbai","Hyderabad")
    cbmdest.current(0)
    cbmdest.grid(row = 1,column=1)

    chkadult = Checkbutton(topleft3,font=('arial',20,"bold"),text = "Adult", variable = var4 , onvalue =1 ,offvalue = 0)
    chkadult.grid(row = 2,column=0,sticky=W)
    chkchild = Checkbutton(topleft3,font=('arial',20,"bold"),text = "Child", variable = var5 , onvalue =1 ,offvalue = 0)
    chkchild.grid(row = 3,column=0,sticky=W)

#--------------------------------------------------------------------TICKET--------------------------------------------------

    lblClass = Label(topleft2,font=('arial',22,"bold"),text = "Ticket Type",bd=8)
    lblClass.grid(row = 0,column=0,sticky=W)

    chksingle = Checkbutton(topleft2,font=('arial',20,"bold"),text = "Single",command=chkbutton1,
                        variable = var10 , onvalue =1 ,offvalue = 0)
    chksingle.grid(row = 1,column=0,sticky=W)
    entsingle = Entry (topleft2,font=('arial',20,"bold"),textvariable = var12,bd=2,width=8,state = DISABLED)
    entsingle.grid(row = 1,column=1,sticky=W)

    chkreturn = Checkbutton(topleft2,font=('arial',20,"bold"),text = "Return",command=chkbutton,
                        variable = var11 , onvalue =1 ,offvalue = 0)
    chkreturn.grid(row = 2,column=0,sticky=W)
    entreturn = Entry (topleft2,font=('arial',20,"bold"),textvariable = var6,bd=2,width=8,state = DISABLED)
    entreturn.grid(row = 2,column=1,sticky=W)

    lblcomment = Label(topleft2,font=('arial',22,"bold"),text = "Comment",bd=8)
    lblcomment.grid(row = 3,column=0,sticky=W)
    entcomment = Entry (topleft2,font=('arial',20,"bold"),textvariable = var7,bd=2,width=8)
    entcomment.grid(row = 3,column=1,sticky=W)

#--------------------------------------------------------------------CALCULATOR--------------------------------------------------

    text_input = StringVar()
    txtdisplay = Entry(bottomleft2,font=('arial',10,"bold"),width=35,textvariable = text_input,bd=8,justify ="right")
    txtdisplay.grid(columnspan = 4)

    lblspace= Label(bottomleft2,font=('arial',4,"bold"),text = " \n",bd=2,anchor = "w")
    lblspace.grid(row = 1,column=2)

    btn7 = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="7",bg="light grey",
              command=lambda : btnclick(7),width=4).grid(row =2,column = 0)
    btn8 = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="8",bg="light grey",
              command=lambda : btnclick(8),width=4).grid(row =2,column = 1)
    btn9 = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="9",bg="light grey",
              command=lambda : btnclick(9),width=4).grid(row =2,column = 2)

    add = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="+",bg="light grey",
              command=lambda : btnclick("+"),width=4).grid(row =2,column = 3)

#-------------------------------------------------------------------------------------------------------------------

    btn4 = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="4",bg="light grey",
              command=lambda : btnclick(4),width=4).grid(row =3,column = 0)
    btn5 = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="5",bg="light grey",
              command=lambda : btnclick(5),width=4).grid(row =3,column = 1)
    btn6 = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="6",bg="light grey",
              command=lambda : btnclick(6),width=4).grid(row =3,column = 2)

    sub = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="-",bg="light grey",
              command=lambda : btnclick("-"),width=4).grid(row =3,column = 3)

#-------------------------------------------------------------------------------------------------------------------

    btn1 = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="1",bg="light grey",
              command=lambda : btnclick(1),width=4).grid(row =4,column = 0)
    btn2 = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="2",bg="light grey",
              command=lambda : btnclick(2),width=4).grid(row =4,column = 1)
    btn3 = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="3",bg="light grey",
              command=lambda : btnclick(3),width=4).grid(row =4,column = 2)

    mul = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="*",bg="light grey",
              command=lambda : btnclick("*"),width=4).grid(row =4,column = 3)

#-------------------------------------------------------------------------------------------------------------------

    btn0 = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="0",bg="light grey",
              command=lambda : btnclick(0),width=4).grid(row =5,column = 0)
    btnclear = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="C",bg="light grey"
                  ,width=4,command =btncleardisplay).grid(row =5,column = 1)
    btnequal = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="=",bg="light grey",
              command=btnequal,width=4).grid(row =5,column = 2)

    div = Button(bottomleft2,padx=8,pady=10,bd =8,font=('arial',10,"bold"),text ="/",bg="light grey",
              command=lambda : btnclick("/"),width=4).grid(row =5,column = 3)

    lblspace= Label(bottomleft2,font=('arial',4,"bold"),text = " \n",bd=2,anchor = "w")
    lblspace.grid(row = 6,column=2)


#-----------------------------------------------------TAX , Subtotal , TOTAl-------------------------------------------------

    tax = StringVar()
    subtotal= StringVar()
    total= StringVar()

    lblspace= Label(bottomleft1,font=('arial',4,"bold"),text = " \n",bd=2,anchor = "w")
    lblspace.grid(row = 1,column=2)

    lblstatetax = Label(bottomleft1,font=('arial',24,"bold"),text = "State Tax",bd=16,anchor = "w")
    lblstatetax.grid(row = 3,column=2)
    txttax = Entry (bottomleft1,font=('arial',16,"bold"),textvariable = tax,bd=10,width=28,bg ="#ffffff",justify ="right")
    txttax.grid(row = 3,column=3)

    lblsub = Label(bottomleft1,font=('arial',24,"bold"),text = "Sub Total",bd=16,anchor = "w")
    lblsub.grid(row = 4,column=2)
    txtsub = Entry (bottomleft1,font=('arial',16,"bold"),textvariable = subtotal,bd=10,width=28,bg ="#ffffff",justify ="right")
    txtsub.grid(row = 4,column=3)

    lbltotal = Label(bottomleft1,font=('arial',24,"bold"),text = "Total Cost",bd=16,anchor = "w")
    lbltotal.grid(row = 5,column=2)
    txttotal = Entry (bottomleft1,font=('arial',16,"bold"),textvariable = total,bd=10,width=28,bg ="#ffffff",justify ="right")
    txttotal.grid(row = 5,column=3)

    lblspace= Label(bottomleft1,font=('arial',20,"bold"),text = " \n",bd=4,anchor = "w")
    lblspace.grid(row = 6,column=2)

#------------------------------------------------------------Info---------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------



    lblspace= Label(fbottomright,font=('arial',12,"bold"),text = "",bd=0)
    lblspace.grid(row = 11,column=0)



    btntotal = Button(fbottomright,font=('arial ',12,"bold"),text = "Total",width =6,height = 1,
                  bd=2,command =travelcost).grid(row = 12, column = 0 )


    btnreset = Button(fbottomright,font=('arial ',12,"bold"),text = "Reset",width =6,height = 1,
                  bd=2,command =reset).grid(row = 12 , column = 1 )

    btnexit = Button(fbottomright,font=('arial ',12,"bold"),text = "Exit",width =6,height = 1,
                 bd=2,command =iexit).grid(row = 12 , column = 2 )

    lblspace= Label(fbottomright,font=('arial',6,"bold"),text = " ",bd=2)
    lblspace.grid(row = 14,column=0)

    root.mainloop()

def mann():
        r2.destroy()
        def valid():
            
            conn=sqlite3.connect('reg.db')
            cursor = conn.cursor()
            cursor.execute("select password from datainfo where username ='%s'"% usern.get())
            p=cursor.fetchone()
            if(p[0]==pasword.get()):
                tkinter.messagebox.showinfo("Done" , "Login Successfull")
                r1.destroy()
                man()
        
            else:
              tkinter.messagebox.showinfo("Error" , "Invalid Username or password")


        r1=Tk()
        r1.configure(background = "lightyellow")
        r1.geometry('400x500')
        ll = Label(r1,text = "LOGIN !",height = 3 , width = 28 ,font = ('Ariel black',22,'bold'),
                   fg = 'Black',bg="gold")
        ll.pack()

        user = Label(r1,text = "Username : ",font = ('Ariel black',14,'bold'))
        user.place(x=60,y=200)

        
        usern = Entry(r1)
        usern.place(x=180,y=200)

        passs= Label(r1,text = "Password : ",font = ('Ariel black',14,'bold'))
        passs.place(x=60,y=280)
        
        pasword = Entry(r1)
        pasword.place(x=180,y=280)

        b= Button(r1,text = "Login" , command = valid,font = ('Ariel black',16,'bold'),bg="silver")
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
       
       
    r2.destroy()
    
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

b1 = Button(r2, text = "Signup !",height = 2 , width = 10 , font = ('Times',17,'bold'),bg ='pink',
            command = main)
b1.place(x= 50 , y = 190)

b2 = Button(r2, text = "Login !",height = 2 , width = 10, font = ('Times',17,'bold'),bg ='pink',
            command =mann)
b2.place(x= 280 , y = 190)


r2.mainloop()

