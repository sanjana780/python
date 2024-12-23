from tkinter import *

def on_button_click():
    print("you clicked on me and i am button")

def checkcredentials():
    username = input("enter username\t")
    password = input("enter password\t")

    if(username=='sanjanakairo@gmail.com' and password=='12345'):
        print("login successfull")
    else:
        print("login failed")

#create the main window (initializes the main window and set its title)
root= Tk()
root.title("tkinter button example")

#create a button
#button=Button(root, text="click me",command=on_button_click)
button=Button(root, text="click me",command=checkcredentials)
button.pack(pady=20)

#run the application
root.mainloop()