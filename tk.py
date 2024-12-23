from tkinter import *
#creating the main window
root =Tk()

#set the background colour
root.configure(bg="lightblue") 

#change the width and height
root.geometry('444x234')
root.minsize(444,234)
#root.minsize(444,134)
root.minsize(644,434)

label1=Label(root,text="enter username")
label1.pack(pady=80)

#run the application
root.mainloop()