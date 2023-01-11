#--------------------IMPORTING LIBS--------------------
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from tkcalendar import Calendar, DateEntry
from datetime import date

#--------------------COLORS--------------------
colors = ["#007fff", "#ff2222", "#00ff7f", "#5da6f0"]
dark_background = ["dark_background","#333333", "#ffffff"]


#--------------------CREATING WINDOW--------------------
root = Tk()
root.title("Monthly Expense Controller")
root.geometry("900x700")
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

logo = Label(upperframe, image=img, text=" Personal Budget", width=900, compound=LEFT, relief="raised", padx=5, anchor="nw", font="Verdana 20 bold")
logo.place(x=0, y=0)


#--------------------WORKING ON MID FRAME--------------------
list_values = [92006, 30036, 61970]
list_categories = ["Income", "Expenses", "Balance"]
def percent():
    label_name = ttk.Label(midframe, text="Percentage Of Income Spent", anchor=NW, font="Verdana 12")
    label_name.place(x= 7, y= 5)

    income_spent =(list_values[1]/list_values[0])*100
    bar = ttk.Progressbar(midframe, length= 180)
    bar.place(x= 10, y= 41)
    bar["value"] = income_spent

    label_percent = ttk.Label(midframe, text="{:,.2f}%".format(income_spent), anchor=NW, font="Verdana 12")
    label_percent.place(x=200, y=35)
percent()

def graphic_bar(theme):

    figure = plt.Figure(figsize=(4, 3.45), dpi=60, facecolor=theme[1])
    plt.style.use(theme[0])
    ax = figure.add_subplot(111)

    ax.bar(list_categories, list_values,color= colors, width=0.7)

    c = 0

    for i in ax.patches:
        ax.text(i.get_x() - .001, i.get_height() + .5,
                str("{:,.0f}".format(list_values[c])), fontsize=17, fontstyle="italic", verticalalignment="bottom",
                color=theme[2])
        c += 1

    ax.set_xticks([0,1,2])
    ax.set_xticklabels(list_categories, fontsize=16, color= theme[2])

    ax.patch.set_facecolor(theme[1])
    ax.spines["bottom"].set_color(theme[2])
    ax.spines["bottom"].set_linewidth(2)
    ax.spines["right"].set_linewidth(1)
    ax.spines["top"].set_linewidth(1)
    ax.spines["left"].set_color(theme[2])
    ax.spines["left"].set_linewidth(2)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(bottom=False, left=False, color=theme[2])
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color=theme[2])
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figure, midframe)
    canva.get_tk_widget().place(x=10, y=70)
graphic_bar(dark_background)

def pie_graphic(theme):
    frame_pie = Frame(midframe, width=580, height=250, bg=theme[1])
    frame_pie.place(x=415, y=5)

    figure = plt.Figure(figsize=(5, 3), dpi=90, facecolor=theme[1])
    ax = figure.add_subplot(111)

    lista_values_pie = [345, 225, 534]

    explode = []
    for i in list_categories:
        explode.append(0.05)

    ax.pie(lista_values_pie, explode=explode, wedgeprops=dict(width=0.2), autopct="%1.1f%%", colors=colors, shadow=True,
           startangle=90)
    ax.legend(list_categories, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_category = FigureCanvasTkAgg(figure, frame_pie)
    canva_category.get_tk_widget().grid(row=0, column=0)
pie_graphic(dark_background)

def resume(theme, y, message, list_index):
    label_line = Label(midframe, text="", width=215, height=1, anchor=NW, font=("Arial 1"), bg=theme[2])
    label_line.place(x= 309, y= y)

    label_summary = Label(midframe, text=message.upper(), anchor=NW, font=("Verdana 12"), fg=colors[3])
    label_summary.place(x=309, y= y - 17)


    label_summary = Label(midframe, text="U$ {:.2f}  ".format(list_values[list_index]), anchor=NW, font=("Arial 17"), fg=theme[2])
    label_summary.place(x= 309, y= y + 18)
resume(dark_background, 52, "Total Montly Income   ", 0)
resume(dark_background, 132,"Total Montly Expenses ", 1)
resume(dark_background, 212,"Total Remaining           ", 2)

income_label = Label(midframe, text="Table Income and Expenses", anchor="nw", font="Verdana 12")
income_label.place(x=5, y=309)


#--------------------WORKING ON BOTTOM FRAME--------------------
# Frames for content--------------------
income_frame = Frame(bottomframe, width=300, height=250, relief="flat")
income_frame.grid(row= 0, column=0, padx=10)

frame_operations = ttk.LabelFrame(bottomframe,text=" Operations ", width=220, height=250, relief="flat")
frame_operations.grid(row=0, column=1, padx=5)

frame_configuration = Frame(bottomframe, width=220, height=250, relief="flat")
frame_configuration.grid(row=0, column=2, padx=5)


# Treeview--------------------
def show_treeview():
    # creating a treeview with dual scrollbars
    table_head = ["#Id", "Category", "Date", "Value"]

    itens_list = [[0, 2, 3, 4], [0, 2, 3, 4], [0, 2, 3, 4], [0, 2, 3, 4]]

    global tree

    tree = ttk.Treeview(income_frame, selectmode="extended", columns=table_head, show="headings")

    vertical_scrollbar = ttk.Scrollbar(income_frame, orient="vertical", command=tree.yview)

    horizontal_scrollbar = ttk.Scrollbar(income_frame, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

    tree.grid(column=0, row=0, sticky="nsew")
    vertical_scrollbar.grid(column=1, row=0, sticky="ns")
    horizontal_scrollbar.grid(column=0, row=1, sticky="ew")

    h = [30, 100, 100, 100]
    n = 0

    for col in table_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column"s width to the header string
        tree.column(col, width=h[n], anchor="center")
        n += 1

    for item in itens_list:
        tree.insert("", "end", values=item)
show_treeview()


label_info = Label(frame_operations, text="Enter New Expenses", anchor="nw", font="Verdana 10 bold")
label_info.place(x=10, y=5)

# Category Combobox--------------------
label_category = Label(frame_operations, text="Category", anchor="nw", font="Ivy 10 bold")
label_category.place(x=10, y=36)

category_function = ["Travel", "Food"]
category = []

for i in category_function:
    category.append(i[1])

combo_category_expenses = ttk.Combobox(frame_operations, width=10, font="Ivy 10")
combo_category_expenses["values"] = (category)
combo_category_expenses.place(x=110, y=36)

# Calendar--------------------
label_calendar = Label(frame_operations, text="Date", anchor="nw", font="Ivy 10 bold")
label_calendar.place(x=10, y=73)
entry_calendar = DateEntry(frame_operations, width=10, borderwidth=2, year=2023)
entry_calendar.place(x=110, y=73)

# Value--------------------
label_value_expenses = Label(frame_operations, text="Total Value", font="Ivy 10 bold")
label_value_expenses.place(x=10, y=111)
entry_value_expenses = ttk.Entry(frame_operations, width=10, justify="left")
entry_value_expenses.place(x=110, y=111)

# Insert Button--------------------
img_insert = Image.open("assets/images/add.png")
img_insert = img_insert.resize((15,10))
img_insert = ImageTk.PhotoImage(img_insert)

btn_insert_expenses = ttk.Button(frame_operations, image=img_insert, text="Add".upper(), width=6, compound=LEFT)
btn_insert_expenses.place(x=110, y=150)


root.mainloop()
