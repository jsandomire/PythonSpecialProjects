from tkinter import * #imports ktinker library
window = Tk() #creates window for application

label= Label(window,text = "TO-DO-LIST") #labels the window
label.pack()
#below is what is written on notepad
list = Listbox(window,bg = 'Green')# changed color of background
list.insert(1,'Pay Employees')
list.insert(2,'Create Tkinter App')
list.insert(3,'Choreography App') #added new 'to-do's
list.insert(4,'Refill coffee')
list.insert(5,'Write dictionary')
list.insert(6,'Blog social media')

list.pack()
#below describes the color of the window and the font
window.config(bg='black')
window.geometry("250x300") #changed size of window
window.title('LIST')
window.mainloop()