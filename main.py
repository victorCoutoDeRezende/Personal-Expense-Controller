from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

#--------------------COLORS--------------------
colors_bar = ["#007fff", "#ff2222", "#00ff7f"]

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

# CHANGE THEME BUTTON
moon = Image.open("assets/images/moon_stroke.png")
moon = moon.resize((15,15))
moon = ImageTk.PhotoImage(moon)


#--------------------WORKING ON MID FRAME--------------------
def percent():
    l_name = ttk.Label(midframe, text="Percentage Of Income Spent", anchor=NW, font='Verdana 12')
    l_name.place(x= 7, y= 5)

    bar = ttk.Progressbar(midframe, length= 180)
    bar.place(x= 10, y= 41)
    bar['value'] = 50

    value = 50

    l_percent = ttk.Label(midframe, text="{:,.2f}%".format(value), anchor=NW, font='Verdana 12')
    l_percent.place(x=200, y=35)

def graphic_bar(theme):
    list_categories = ['Income', 'Expenses', 'Balance']
    list_values = [3000, 2000, 6236]

    figure = plt.Figure(figsize=(4, 3.45), dpi=60, facecolor=theme[1])
    plt.style.use(theme[0])
    ax = figure.add_subplot(111)

    ax.bar(list_categories, list_values,color= colors_bar, width=0.7)
    # create a list to collect the plt.patches data

    c = 0
    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
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

#--------------------CHANGE THEME BUTTON--------------------
def change_theme():
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
        graphic_bar(light_background)
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")
        graphic_bar(dark_background)
button = ttk.Button(upperframe, command=change_theme, image=moon)
button.place(relx=0.8, rely= 0.2, width=47, height=30)

graphic_bar(dark_background)
percent()
root.mainloop()
