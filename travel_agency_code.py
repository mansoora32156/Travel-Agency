import random
import datetime
import time;
from tkinter import*
from tkinter import ttk
import tkinter.messagebox


class Travel_Agency:
    def __init__(self,root):
        self.root = root
        self.root.title(' Travel Agency ')
        self.root.geometry('1350x750+0+0') #dimensions of window
        self.root.configure(background = 'black')


        date=StringVar()
        date.set(time.strftime('%d %m %Y'))#this module takes date month year

        class1=StringVar()
                    
        receipt=StringVar()
        tax=StringVar()
        subtotal=StringVar()
        total=StringVar()
        firstname=StringVar()
        lastname=StringVar()
        address=StringVar()
        mobile=StringVar()
        email=StringVar()

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Defined functions xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        def iexit ():
            iexit=tkinter.messagebox.askyesno("India's No.1 Travel Agency","confirm if you want to exit")
            if iexit>0:
                root.destroy()
                return
        def reset():
             date=StringVar()
             date.set(time.strftime('%d/%m/%Y'))#this module takes date month year
                          
             tax.set('')
             subtotal.set('')
             total.set('')

             firstname.set('')
             lastname.set('')
             address.set('')
             mobile.set('')
             email.set('')
             receipt=StringVar('')

             var1.set('')
             var2.set('')
             var3.set('')
             
             self.txtreceipt.delete("1.0",END)

             
        def receipt1():
            self.txtreceipt.delete("1.0",END)
            X=random.randint(10000,5000000)
            randomref=str(X)
            receipt.set("Travel Bill: " + randomref)

            self.txtreceipt.insert(END,'receipt ref:\t\t\t\t\t'+ receipt.get()+"\n")
            self.txtreceipt.insert(END,'Date:\t\t\t\t\t'+ date.get()+"\n")
            self.txtreceipt.insert(END,'Flight:\t\t\t\t\t'+ "Travelling Details \n")
            self.txtreceipt.insert(END,'firstname:\t\t\t\t\t'+ firstname.get()+"\n")
            self.txtreceipt.insert(END,'lastname:\t\t\t\t\t'+ lastname.get()+"\n")
            self.txtreceipt.insert(END,'adress:\t\t\t\t\t'+ address.get()+"\n")
            self.txtreceipt.insert(END,'mobile no,:\t\t\t\t\t'+ mobile.get()+"\n")
            self.txtreceipt.insert(END,'email id:\t\t\t\t\t'+ email.get()+"\n")
            self.txtreceipt.insert(END,'class is:\t\t\t\t\t'+ class1.get()+"\n")
            self.txtreceipt.insert(END,'Tax:\t\t\t\t\t'+ tax.get()+"\n")
            self.txtreceipt.insert(END,'Subtotal:\t\t\t\t\t'+ subtotal.get()+"\n")
            self.txtreceipt.insert(END,'Total:\t\t\t\t\t'+ total.get()+"\n")


            
        def Total():

            if(var1.get()== var2.get()):
                tkinter.messagebox.showerror("Error", "Please enter valid DESTINATION !")
                   
            
            elif((var1.get()=="Bangalore" or var1.get()=="Hyderabad"or var1.get()=="Chennai"or var1.get()=="Mumbai"or var1.get()=="Delhi"or
                  var1.get()=="Kolkata" or var1.get()=="Pune" or var1.get()=="Ahmedabad" ) and (var1.get()=="Bangalore" or var1.get()=="Hyderabad"
                  or var1.get()=="Chennai" or var1.get()=="Mumbai" or var1.get()=="Delhi" or var1.get()=="Kolkata" or var1.get()=="Pune" or
                var1.get()=="Ahmedabad" )) :

                if (class1.get()=='First class'):
                    cost_of_fare=8000*(int(var3.get()))*2

                if (class1.get()=='Business class'):
                    cost_of_fare=8000*(int(var3.get()))*3

                else:
                    cost_of_fare=8000*(int(var3.get()))
                    

                tax_paid = "₹" +str('%.2f'%((cost_of_fare)*0.1))
                ST=  "₹" +str('%.2f'%((cost_of_fare)))
                TT=  "₹" +str('%.2f'%(cost_of_fare +((cost_of_fare)*0.1)))

                tax.set(tax_paid)
                subtotal.set(ST)
                total.set(TT)

            elif((var1.get()=="Bangalore" or var1.get()=="Hyderabad" or var1.get()=="Chennai" or var1.get()=="Mumbai" or var1.get()=="Delhi" or
                var1.get()=="Kolkata" or var1.get()=="Pune" or var1.get()=="Ahmedabad" ) and (var1.get()=="New York" or var1.get()=="Los Angeles"
                or var1.get()=="Rome" or var1.get()=="Paris" or var1.get()=="Dubai" )):
                
                if (class1.get()=='First class'):
                    cost_of_fare=50000*(int(var3.get()))*2

                if (class1.get()=='Business class'):
                    cost_of_fare=50000*(int(var3.get()))*3

                else:
                    cost_of_fare=50000*(int(var3.get()))

                tax_paid = "₹" +str('%.2f'%((cost_of_fare)*0.1))
                ST=  "₹" +str('%.2f'%((cost_of_fare)))
                TT=  "₹" +str('%.2f'%(cost_of_fare +((cost_of_fare)*0.1)))

                tax.set(tax_paid)
                subtotal.set(ST)
                total.set(TT)
                
            
           
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        Mainframe=Frame(self.root)
        Mainframe.grid()

        
        on_top=Frame(Mainframe,bd=20,width=1350,relief=RIDGE)#Frame allows us to operate on Mainframe which has border, width, appearance of border  
        on_top.pack(side=TOP)

        self.title=Label(on_top,font=('arial',70,'bold'),text='India\'s No.1 Travel Agency',bg='pink')
        self.title.grid()
        
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

        cust_details_frame=Frame(Mainframe,width=1350,height=500,bd=20,pady=5,relief=RIDGE)#pady is vertical padding i.e it fills out the extra space
        cust_details_frame.pack(side=BOTTOM)

        frame_details=Frame(cust_details_frame,width=880,height=400,bd=10,relief=RIDGE)
        frame_details.pack(side=LEFT)

        cust_name=LabelFrame(frame_details,width=150,height=250,bd=20,font=('arial',12,'bold'),text='Customer Name',relief=RIDGE)
        cust_name.grid(row=0,column=0)

        travel_frame=LabelFrame(frame_details,width=300,height=250,bd=10,font=('arial',12,'bold'),text='Travel Details',relief=RIDGE)
        travel_frame.grid(row=0,column=1)

        ticket_frame=LabelFrame(frame_details,width=300,height=150,relief=FLAT)
        ticket_frame.grid(row=1,column=0)

        cost_frame=LabelFrame(frame_details,width=150,height=150,relief=FLAT)
        cost_frame.grid(row=1,column=1)
        
        receipt_buttonframe=Frame(cust_details_frame,width=450,height=400,bd=10,relief=RIDGE)
        receipt_buttonframe.pack(side=RIGHT)

        receipt_frame=LabelFrame(receipt_buttonframe,width=350,height=300,bd=10,font=('arial',12,'bold'),text='Receipt',relief=RIDGE)
        receipt_frame.grid(row=0,column=0)

        button_frame=LabelFrame(receipt_buttonframe,width=350,height=100,bd=5,font=('arial',12,'bold'),text='Options',relief=RIDGE)
        button_frame.grid(row=1,column=0)
        
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  Customer Details  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

        self.lbl_first_name=Label(cust_name,font=('arial',14,'bold'),text='First name',bd=7)
        self.lbl_first_name.grid(row=0,column=0,sticky=W)#sticky specifies widget to move west 

        self.txt_first_name=Entry(cust_name,font=('arial',14,'bold'),text='First name',textvariable=firstname,bd=7,insertwidth=2,justify=RIGHT)
        self.txt_first_name.grid(row=0,column=1)#entry provides a single line text box to enter text

        self.lbl_last_name=Label(cust_name,font=('arial',14,'bold'),text='Last name',bd=7)
        self.lbl_last_name.grid(row=1,column=0,sticky=W)

        self.txt_last_name=Entry(cust_name,font=('arial',14,'bold'),text='Last name',textvariable=lastname,bd=7,insertwidth=2,justify=RIGHT)
        self.txt_last_name.grid(row=1,column=1)

        self.lbl_address=Label(cust_name,font=('arial',14,'bold'),text='Address',bd=7)
        self.lbl_address.grid(row=2,column=0,sticky=W)

        self.txt_address=Entry(cust_name,font=('arial',14,'bold'),text='Address',textvariable=address,bd=7,insertwidth=2,justify=RIGHT)
        self.txt_address.grid(row=2,column=1)

        self.lbl_mobile=Label(cust_name,font=('arial',14,'bold'),text='Mobile No.',bd=7)
        self.lbl_mobile.grid(row=3,column=0,sticky=W)

        self.txt_mobile=Entry(cust_name,font=('arial',14,'bold'),text='Mobile No.',textvariable=mobile,bd=7,insertwidth=2,justify=RIGHT)
        self.txt_mobile.grid(row=3,column=1)

        self.lbl_email=Label(cust_name,font=('arial',14,'bold'),text='Email-ID',bd=7)
        self.lbl_email.grid(row=4,column=0,sticky=W)

        self.txt_email=Entry(cust_name,font=('arial',14,'bold'),text='Email-ID',textvariable=email,bd=7,insertwidth=2,justify=RIGHT)
        self.txt_email.grid(row=4,column=1)

        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Travel Info xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

              

        self.lbl_departure=Label(travel_frame,font=('arial',14,'bold'),text='Departure :',bd=7)
        self.lbl_departure.grid(row=0,column=0,sticky=W)

        self.cb_departure=ttk.Combobox(travel_frame,textvariable=var1,state='readonly',font=('arial',14,'bold'),width=14)
        self.cb_departure['value']=('','Bangalore','Chennai','Hyderabad','Mumbai','Delhi','Kolkata','Pune','Ahmedabad')
        self.cb_departure.current(0)
        self.cb_departure.grid(row=0,column=1)


        self.lbl_destination=Label(travel_frame,font=('arial',14,'bold'),text='Destination :',bd=7)
        self.lbl_destination.grid(row=1,column=0,sticky=W)

        self.cb_destination=ttk.Combobox(travel_frame,textvariable=var2,state='readonly',font=('arial',14,'bold'),width=14)
        self.cb_destination['value']=('','Bangalore','Chennai','Hyderabad','Mumbai','Delhi','Kolkata','Pune','Ahmedabad','New York',
                                      'Los Angeles','Rome','Paris','Dubai')
        self.cb_destination.current(0)
        self.cb_destination.grid(row=1,column=1)

        self.lbl_class1=Label(travel_frame,font=('arial',14,'bold'),text='class:',bd=7)
        self.lbl_class1.grid(row=2,column=0,sticky=W)

        self.cb_class1=ttk.Combobox(travel_frame,textvariable=class1,state='readonly',font=('arial',14,'bold'),width=14)
        self.cb_class1['value']=('','Economy class','First class','Business class')
        self.cb_class1.current(0)
        self.cb_class1.grid(row=2,column=1)



        self.lbl_passengers=Label(travel_frame,font=('arial',14,'bold'),text='No. of passengers :',bd=7)
        self.lbl_passengers.grid(row=3,column=0,sticky=W)

        self.txt_passengers=Entry(travel_frame,font=('arial',14,'bold'),text='No. of passengers :',textvariable=var3,bd=7,insertwidth=2,justify=RIGHT)
        self.txt_passengers.grid(row=3,column=1)

        self.lbl_tax=Label(travel_frame,font=('arial',14,'bold'),text='Tax :',bd=7)
        self.lbl_tax.grid(row=4,column=0,sticky=W)

        self.lbl_tax=Label(travel_frame,font=('arial',14,'bold'),textvariable=tax,bd=7,width=10,justify=RIGHT)#it shows the tax
        self.lbl_tax.grid(row=4,column=1)

        
        self.lbl_subtotal=Label(travel_frame,font=('arial',14,'bold'),text='Sub-Total :',bd=7)
        self.lbl_subtotal.grid(row=5,column=0,sticky=W)

        self.lbl_subtotal=Label(travel_frame,font=('arial',14,'bold'),textvariable=subtotal,bd=7,width=10,justify=RIGHT)
        self.lbl_subtotal.grid(row=5,column=1)


        self.lbl_total=Label(travel_frame,font=('arial',14,'bold'),text='Total :',bd=7)
        self.lbl_total.grid(row=6,column=0,sticky=W)

        self.lbl_total=Label(travel_frame,font=('arial',14,'bold'),textvariable=total,bd=7,width=10,justify=RIGHT)
        self.lbl_total.grid(row=6,column=1)
        
      
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx receipt_frame xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        
        self.txtreceipt=Text(receipt_frame,width=60,height=21,font=('arial',10,'bold'))
        self.txtreceipt.grid(row=0,column=0)
        
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx buttons_frame xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        
        self.btnTotal=Button(button_frame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Total',command=Total).grid(row=0,column=0)
        self.btnreceipt=Button(button_frame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Receipt',command=receipt1).grid(row=0,column=1)
        self.btnreset=Button(button_frame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Reset',command=reset).grid(row=0,column=2)
        self.btnexit=Button(button_frame,padx=18,bd=7,font=('arial',16,'bold'),width=4,
                             text='Exit',command=iexit).grid(row=0,column=3)

        
        


        
        


  
    
if __name__=='__main__':#for src file to be executed as main prog

    root=Tk()
    apply=Travel_Agency(root)
    root.mainloop()#it executes prog till condition is satisfied(then terminates)
