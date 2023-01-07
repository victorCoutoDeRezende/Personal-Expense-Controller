from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

#--------------------COLORS--------------------
black = "#2e2d2b"
white = "#feffff"
green = "#4fa882"
value = "#38576b"
letter = "#403d3d"
orange = "#e06636"
blue = "#038cfc"
light_green = "#3fbfb9" #almost blue
dark_blue = "#263238"
darker_white = "#e9edf5"

#--------------------CREATING WINDOW--------------------
if __name__ == "__main__":
    root = Tk()
    root.title("Monthly Expense Controller")
    root.geometry('900x650')
    big_frame = ttk.Frame(root)
    big_frame.place(relwidth=1, relheight=1)
    root.call("source", "./assets/Azure-ttk-theme-main/azure.tcl")
    root.call("set_theme", "dark")
    root.resizable(width=FALSE, height=FALSE)
    style = ttk.Style(root)


#--------------------CREATING DIVISION FRAMES--------------------
upperframe = Frame(root, width=1043, height=50, relief="flat")
upperframe.grid(row=0, column=0)

midframe = Frame(root, width=1043, height=361, pady=20, relief="raised")
midframe.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

bottomframe = Frame(root, width=1043, height=300, relief="flat")
bottomframe.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)
#--------------------WORKING ON UPPER FRAME--------------------
img = Image.open("assets/images/logo.png")
img = img.resize((45,45))
img = ImageTk.PhotoImage(img)

logo = Label(upperframe, image=img, text=" Personal Budget", width=900, compound=LEFT, relief=RAISED, padx=5, anchor=NW, font='Verdana 20 bold')
logo.place(x=0, y=0)

def change_theme():
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")

moon = Image.open("assets/images/moon_stroke.png")
moon = moon.resize((15,15))
moon = ImageTk.PhotoImage(moon)
button = ttk.Button(upperframe, command=change_theme, image=moon)
button.place(relx=0.8, rely= 0.2, width=47, height=30)





root.mainloop()
