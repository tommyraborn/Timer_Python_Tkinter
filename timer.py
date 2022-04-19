#Took a break from development on this on 4/19/22
#Everything seems to work, but I am currently stuck on getting it to not become unresponsive after entering a number in minutes, and hitting start.
# I can not seem to get it to be responsive afterwards.
#I will come back to it one of these days, I have more projects to work on. 
#If you have any fixes please feel free to jump in and help, I will update authors and contributors!

#----------------------------------------------------------------

#If it seems like it is all over the place, it is. I usually start working with the code and then at the end come back and polish it off.


#Imported modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from tkinter import *
from PIL import ImageTk, Image
#-------------------

root=Tk()
frame = ttk.Frame(root)


#Title of application
root.title('Timer Made by Thomas Ray | linkedin.com/in/tlraborn | github.com/tommyraborn')
root.geometry('800x400')
root.resizable(False, False)
#-------------------



#Finish working on image and then start working on buttons


#Entry for timer minute(s)
entryminutes = tk.StringVar()
e = tk.Entry(root, border=0)
e.grid(row=3, column=1)
e.place(width = 500, height = 100, x = 150, y = 100)
#-------------------

#Start Button
timer_text = tk.StringVar()
timer_btn = tk.Button(root, 
                      textvariable=timer_text, font="Ubuntu", 
                      bg="#C1DBB3",height=2,width=15, border=0, 
                      command=lambda:timer_start())
timer_text.set("Start")
timer_btn.place(x = 200, y = 210)
#-------------------




#Reset Button
reset_timer = tk.StringVar()
reset_btn = tk.Button(root, 
                      textvariable=reset_timer,height=2,
                      width=15, border=0, 
                      bg="#D3D3D3", font="Ubuntu", command=lambda:timer_reset())
reset_timer.set("Reset")
reset_btn.place(x = 460, y = 210)
#-------------------

#Timer Button Actions
def timer_start():
    checkentry = int(e.get()) #This works
    if checkentry == 0: #Works but needs to be changed
        messagebox.showerror('Invalid Number Input', 'Error Please Input a valid number.')
    elif checkentry > 0 : #This does not
        def countdown(m):
    
            transl = m * 60
            while transl > 0:
                time.sleep(1)
                transl -= 1
                countdownvalues = []
                transl_it = iter(countdownvalues)
                countdownvalues.append(transl)
        countdown(int(e.get()))
        # Fix printing issue and performance issues
#-------------------

#If entry is greater than 0, and the button is clicked replace label with a printed countdown of the timer

def timer_reset():
    print("working yes?")



root.mainloop()


