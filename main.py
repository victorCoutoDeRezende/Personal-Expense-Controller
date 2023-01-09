from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import time

#--------------------COLORS--------------------
colors = ["#007fff", "#ff2222", "#00ff7f", "#5da6f0"]

dark_background = ["dark_background","#333333", "#ffffff"]
light_background = ["default","#ffffff", "#333333"]
#--------------------CREATING WINDOW--------------------
root = Tk()
root.title("Monthly Expense Controller")
root.geometry('900x650')
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
# LOGO
img = Image.open("assets/images/logo.png")
img = img.resize((45,45))
img = ImageTk.PhotoImage(img)

logo = Label(upperframe, image=img, text=" Personal Budget", width=900, compound=LEFT, relief=RAISED, padx=5, anchor=NW, font='Verdana 20 bold')
logo.place(x=0, y=0)

# CHANGE THEME BUTTON LOGO
moon = Image.open("assets/images/moon_stroke.png")
moon = moon.resize((15,15))
moon = ImageTk.PhotoImage(moon)


#--------------------WORKING ON MID FRAME--------------------
list_values = [92006, 30036, 61970]
list_categories = ['Income', 'Expenses', 'Balance']
def percent():
    l_name = ttk.Label(midframe, text="Percentage Of Income Spent", anchor=NW, font='Verdana 12')
    l_name.place(x= 7, y= 5)

    income_spent =(list_values[1]/list_values[0])*100
    bar = ttk.Progressbar(midframe, length= 180)
    bar.place(x= 10, y= 41)
    bar['value'] = income_spent

    l_percent = ttk.Label(midframe, text="{:,.2f}%".format(income_spent), anchor=NW, font='Verdana 12')
    l_percent.place(x=200, y=35)

def graphic_bar(theme):

    figure = plt.Figure(figsize=(4, 3.45), dpi=60, facecolor=theme[1])
    plt.style.use(theme[0])
    ax = figure.add_subplot(111)

    ax.bar(list_categories, list_values,color= colors, width=0.7)

    c = 0

    for i in ax.patches:
        ax.text(i.get_x() - .001, i.get_height() + .5,
                str("{:,.0f}".format(list_values[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom',
                color=theme[2])
        c += 1

    ax.set_xticks([0,1,2])
    ax.set_xticklabels(list_categories, fontsize=16, color= theme[2])

    ax.patch.set_facecolor(theme[1])
    ax.spines['bottom'].set_color(theme[2])
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['right'].set_linewidth(1)
    ax.spines['top'].set_linewidth(1)
    ax.spines['left'].set_color(theme[2])
    ax.spines['left'].set_linewidth(2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(bottom=False, left=False, color=theme[2])
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color=theme[2])
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figure, midframe)
    canva.get_tk_widget().place(x=10, y=70)

def resume(theme, y, message, list_index):
    l_line = Label(midframe, text="", width=215, height=1, anchor=NW, font=("Arial 1"), bg=theme[2])
    l_line.place(x= 309, y= y)

    l_summary = Label(midframe, text=message.upper(), anchor=NW, font=("Verdana 12"), fg=colors[3])
    l_summary.place(x=309, y= y - 17)


    l_summary = Label(midframe, text="U$ {:.2f}  ".format(list_values[list_index]), anchor=NW, font=("Arial 17"), fg=theme[2])
    l_summary.place(x= 309, y= y + 18)

def pie_graphic(theme):
    frame_pie = Frame(midframe, width=580, height=250, bg=theme[1])
    frame_pie.place(x=415, y=5)

    figure = plt.Figure(figsize=(5, 3), dpi=90, facecolor=theme[1])
    ax = figure.add_subplot(111)

    lista_values_pie = [345, 225, 534]

    explode = []
    for i in list_categories:
        explode.append(0.05)

    ax.pie(lista_values_pie, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors, shadow=True,
           startangle=90)
    ax.legend(list_categories, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_category = FigureCanvasTkAgg(figure, frame_pie)
    canva_category.get_tk_widget().grid(row=0, column=0)

#--------------------CHANGE THEME BUTTON--------------------

def change_theme():
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
        graphic_bar(light_background)
        pie_graphic(light_background)
        resume(light_background, 52, "Total Montly Income   ", 0)
        resume(light_background, 132,"Total Montly Expenses ", 1)
        resume(light_background, 212,"Total Remaining           ", 2)
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")
        graphic_bar(dark_background)
        pie_graphic(dark_background)
        resume(dark_background, 52, "Total Montly Income   ", 0)
        resume(dark_background, 132,"Total Montly Expenses ", 1)
        resume(dark_background, 212,"Total Remaining           ", 2)

button = ttk.Button(upperframe, command=change_theme, image=moon)
button.place(relx=0.8, rely= 0.2, width=47, height=30)

graphic_bar(dark_background)
percent()
pie_graphic(dark_background)
resume(dark_background, 52, "Total Montly Income   ", 0)
resume(dark_background, 132,"Total Montly Expenses ", 1)
resume(dark_background, 212,"Total Remaining           ", 2)
root.mainloop()
