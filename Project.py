from tkinter import*
def click():
    print("You Clicked the Button")
window = Tk() # defines a window
logo =PhotoImage(file='logoicon.png')
window.geometry("520x420")
window.title("My App")
#text = Label(window,text="Hello World", font='bold', fg="white", bg="#434343",relief=FLAT,bd=5,padx=5,pady=5,image=logo,compound="top")# defines a label
#text.pack() # displays the label in the top center of the window
#text.place(x=210,y=0) # displays the label in a speicfic place in the window
button=Button(window,text="Click me", font='bold', fg="white", bg="#434343",relief=FLAT,bd=5,padx=5,pady=5, command=click)
button.pack()
icon = PhotoImage(file='logoicon.png')
window.iconphoto(True,icon)
window.config(background="#111010")
window.mainloop() # makes a window on screen and checks for events

