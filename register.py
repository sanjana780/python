from tkinter import *
from tkinter import messagebox
#create the main window
root = Tk()

def chksubmission():
    #print(f"{namevar.get(),gendervar.get(),emergencyvar.get(),paymentmodevar.get(),chktermsvar.get()}")
    print(f"{namevar.get(),phonevar.get(),gendervar.get(),emergencyvar.get(),paymentmodevar.get(),chktermsvar.get()}")
    with open("record.txt","a") as f:
        f.write(f"{namevar.get(),phonevar.get(),gendervar.get(),emergencyvar.get(),paymentmodevar.get(),chktermsvar.get()}")

root.title("registration form")
width,height = 800,400

d = str(width) + "x" + str(height)
root.geometry(d)
#root.geometry("800x400+410+100")
root.configure(bg="#55a3a3")

Label(root,text="welcome on registration page".upper(),font="montserrat 16",bg="#55a3a3",fg="#fff").grid(row=0,column=3)

#declare labels
lblName=Label(root,text="name".upper(),font="montserrat 13",bg="#55a3a3",fg="#2c3e50").grid(row=1,column=2)
lblPhone=Label(root,text="phone".upper(),font="montserrat 13",bg="#55a3a3",fg="#2c3e50").grid(row=2,column=2)
lblGender=Label(root,text="gender".upper(),font="montserrat 13",bg="#55a3a3",fg="#2c3e50").grid(row=3,column=2)
lblEmergency=Label(root,text="emergency".upper(),font="montserrat 13",bg="#55a3a3",fg="#2c3e50").grid(row=4,column=2)
lblPaymentmode=Label(root,text="payment mode".upper(),font="montserrat 13",bg="#55a3a3",fg="#2c3e50").grid(row=5,column=2)

#declare variables
namevar = StringVar()
phonevar = StringVar()
gendervar =StringVar()
emergencyvar = StringVar()
paymentmodevar = StringVar()
chktermsvar = IntVar()

#allot variables to textbox/controls
txtNameEntry = Entry(root,textvariable=namevar,width=40,bg="#55a3a3",fg="#000",justify="center").grid(row=1,column=3)
txtPhoneEntry = Entry(root,textvariable=phonevar,width=40,bg="#55a3a3",fg="#000",justify="center").grid(row=2,column=3)
txtGenderEntry = Entry(root,textvariable=gendervar,width=40,bg="#55a3a3",fg="#000",justify="center").grid(row=3,column=3)
txtEmergencyEntry = Entry(root,textvariable=emergencyvar,width=40,bg="#55a3a3",fg="#000",justify="center").grid(row=4,column=3)
txtPaymentmodeEntry = Entry(root,textvariable=paymentmodevar,width=40,bg="#55a3a3",fg="#000",justify="center").grid(row=5,column=3)
chkterms=Checkbutton(text="agree terms and conditions?",variable=chktermsvar,bg="#55a3a3",fg="#000").grid(row=6,column=3)
Button(text="submit",command=chksubmission,bg="#000",fg="#fff",border=0,padx=20,pady=4).grid(row=10,column=3)

root.bind('<Escape>',lambda e:root.quit())
root.mainloop()