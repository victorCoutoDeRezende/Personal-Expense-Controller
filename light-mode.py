#=======================================================================================================================
#--------------------------------------------------- IMPORTING LIBS ----------------------------------------------------
#=======================================================================================================================
# _-_- TKINTER -_-_-_
from tkinter import *
from tkinter import Tk, ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox

# _-_-_-_-_- PILLOW _-_-_-_-_-
from PIL import Image, ImageTk

# _-_-_-_-_-_-_-_-_-_- MATPLOTLIB -_-_-_-_-_-_-_-_-_-_-_-_-_-_
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# _-_-_-_- DATETIME -_-_-_-_-
from datetime import date

# _-_-_-_-_- VIEW _-_-_-_-_-
from view import *

#=======================================================================================================================
#-------------------------------------------------------- COLORS -------------------------------------------------------
#=======================================================================================================================

colors = ["#007fff", "#ff2222", "#00ff7f", "#d48748"]
light_background = ["default", "#ffffff", "#333333", "#5da6f0"]


#=======================================================================================================================
#--------------------------------------------------- CREATING WINDOW ---------------------------------------------------
#=======================================================================================================================

root = Tk()
root.title("Monthly Expense Controller")
root.geometry("900x700")
root.call("source", "./assets/Azure-ttk-theme-main/azure.tcl")
root.call("set_theme", "light")
root.resizable(width=FALSE, height=FALSE)
style = ttk.Style(root)

# Images--------------------
img_logo = Image.open("assets/images/logo.png")
img_logo = img_logo.resize((45,45))
img_logo = ImageTk.PhotoImage(img_logo)

img_insert = Image.open("assets/images/add.png")
img_insert = img_insert.resize((15, 15))
img_insert = ImageTk.PhotoImage(img_insert)

img_delete = Image.open("assets/images/delete.png")
img_delete = img_delete.resize((15, 15))
img_delete = ImageTk.PhotoImage(img_delete)

#=======================================================================================================================
#----------------------------------------------- CREATING DIVISION FRAMES ----------------------------------------------
#=======================================================================================================================
upperframe = Frame(root, width=1043, height=50, relief="flat")
upperframe.grid(row=0, column=0)

midframe = Frame(root, width=1043, height=361, pady=20, relief="raised")
midframe.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

bottomframe = Frame(root, width=1043, height=300, relief="flat")
bottomframe.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

#=======================================================================================================================
#------------------------------------------------------ FUNCTIONS ------------------------------------------------------
#=======================================================================================================================

def update():
    show_treeview()
    percent()
    pie_graphic(light_background)
    graphic_bar(light_background)
    resume(light_background, 52, "Total Montly Income   ", 0)
    resume(light_background, 132, "Total Montly Expenses ", 1)
    resume(light_background, 212, "Total Remaining           ", 2)

def create_category():
    # Adding the category to the database with the view.py functions
    name = entry_new_category.get()
    list_insert = [name]

    for i in list_insert: # shows an error if the entry is empty
        if i == '':
            messagebox.showerror("Error", "Fill In All Fields")
            return

    insert_category(list_insert)
    messagebox.showinfo("Sucess", "The Data Has Been Entered Successfully")
    entry_new_category.delete(0, 'end')

    #getting the values of the category
    function_categories = visualize_category()
    categories = []

    for i in function_categories:
        categories.append(i[1])

    # Updating the categories list in the combobox
    combo_category_expenses['values'] = (categories)

def create_income():
    name = 'Income'
    date = entry_calendar_incomes.get()
    value = entry_value_incomes.get()
    list_insert = [name, date, value]

    for i in list_insert: # shows an error if the entry is empty
        if i == '':
            messagebox.showerror("Error", "Fill In All Fields")
            return

    insert_income(list_insert)
    messagebox.showinfo("Sucess", "The Data Has Been Entered Successfully")
    entry_calendar_incomes.delete(0, 'end')
    entry_value_incomes.delete(0, 'end')

    # Updating Data
    update()

def create_expenses():
    name = combo_category_expenses.get()
    date = entry_calendar_expenses.get()
    value = entry_value_expenses.get()
    list_insert = [name, date, value]

    for i in list_insert: # shows an error if the entry is empty
        if i == '':
            messagebox.showerror("Error", "Fill In All Fields")
            return

    insert_expenses(list_insert)
    messagebox.showinfo("Sucess", "The Data Has Been Entered Successfully")

    combo_category_expenses.delete(0, 'end')
    entry_calendar_expenses.delete(0, 'end')
    entry_value_expenses.delete(0, 'end')

    # Updating Data
    update()

def delete_data():
    try:
        treev_data = tree.focus()
        treev_dict = tree.item(treev_data)
        treev_list = treev_dict['values']
        value = treev_list[0]
        name = treev_list[1]

        if name == 'Income':
            delete_income([value])
            messagebox.showinfo("Sucess", "The Data Has Been Deleted Successfully")
            update()
        else:
            delete_expenses([value])
            messagebox.showinfo("Sucess", "The Data Has Been Deleted Successfully")
            update()
    except IndexError:
        messagebox.showerror('Error', 'Select a valid data of the table')

#=======================================================================================================================
#------------------------------------------------ WORKING ON UPPER FRAME -----------------------------------------------
#=======================================================================================================================
# LOGO
logo = Label(upperframe, image=img_logo, text=" Personal Budget", width=900, compound=LEFT, relief="raised", padx=5, anchor="nw", font="Verdana 20 bold")
logo.place(x=0, y=0)


#=======================================================================================================================
#------------------------------------------------- WORKING ON MID FRAME ------------------------------------------------
#=======================================================================================================================


def percent():
    list_values = bar_values()

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
    list_values = bar_values()
    list_categories = ["Income", "Expenses", "Balance"]
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
graphic_bar(light_background)

def pie_graphic(theme):
    list_categories = pie_values()[0]
    lista_values_pie = pie_values()[1]

    frame_pie = Frame(midframe, width=580, height=250, bg=theme[1])
    frame_pie.place(x=415, y=5)

    figure = plt.Figure(figsize=(5, 3), dpi=90, facecolor=theme[1])
    ax = figure.add_subplot(111)

    explode = []
    for i in list_categories:
        explode.append(0.05)

    ax.pie(lista_values_pie, explode=explode, wedgeprops=dict(width=0.2), autopct="%1.1f%%", colors=colors, shadow=True,
           startangle=90)
    ax.legend(list_categories, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_category = FigureCanvasTkAgg(figure, frame_pie)
    canva_category.get_tk_widget().grid(row=0, column=0)
pie_graphic(light_background)

def resume(theme, y, message, list_index):
    list_values = bar_values()

    label_line = Label(midframe, text="", width=215, height=1, anchor=NW, font=("Arial 1"), bg=theme[2])
    label_line.place(x= 309, y= y)

    label_summary = Label(midframe, text=message.upper(), anchor=NW, font=("Verdana 12"), fg=light_background[3])
    label_summary.place(x=309, y= y - 17)


    label_summary = Label(midframe, text="U$ {:.2f}  ".format(list_values[list_index]), anchor=NW, font=("Arial 17"), fg=theme[2])
    label_summary.place(x= 309, y= y + 18)
resume(light_background, 52, "Total Montly Income   ", 0)
resume(light_background, 132,"Total Montly Expenses ", 1)
resume(light_background, 212,"Total Remaining           ", 2)

income_label = Label(midframe, text="Table Income and Expenses", anchor="nw", font="Verdana 12")
income_label.place(x=5, y=309)

#=======================================================================================================================
#----------------------------------------------- WORKING ON BOTTOM FRAME -----------------------------------------------
#=======================================================================================================================

# Frames for content--------------------
treeview_frame = Frame(bottomframe, width=300, height=250, relief="flat")
treeview_frame.grid(row= 0, column=0)

frame_operations = ttk.LabelFrame(bottomframe,text=" Operations ", width=220, height=250, relief="flat")
frame_operations.grid(row=0, column=1, padx=5)

frame_incomes = ttk.LabelFrame(bottomframe,text=" Incomes ", width=220, height=250, relief="flat")
frame_incomes.grid(row=0, column=2, padx=5)


# Treeview--------------------
def show_treeview():
    # creating a treeview with dual scrollbars
    table_head = ["#Id", "Category", "Date", "Value"]
    global tree

    itens_list = table()

    tree = ttk.Treeview(treeview_frame, selectmode="extended", columns=table_head, show="headings")

    vertical_scrollbar = ttk.Scrollbar(treeview_frame, orient="vertical", command=tree.yview)

    horizontal_scrollbar = ttk.Scrollbar(treeview_frame, orient="horizontal", command=tree.xview)

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

#-------------------------------------------WORKING ON OPERATIONS SECTION-------------------------------------------

label_info = Label(frame_operations, text="Enter New Expenses", anchor="nw", font="Verdana 10 bold")
label_info.place(x=10, y=5)

# Category Combobox--------------------
label_category = Label(frame_operations, text="Category", anchor="nw", font="Ivy 10 bold")
label_category.place(x=10, y=40)

category_function = visualize_category()
category = []

for i in category_function:
    category.append(i[1])

combo_category_expenses = ttk.Combobox(frame_operations, width=10, font="Ivy 10")
combo_category_expenses['values'] = (category)
combo_category_expenses.place(x=120, y=36)

# Calendar--------------------
label_calendar_operations = Label(frame_operations, text="Date", anchor="nw", font="Ivy 10 bold")
label_calendar_operations.place(x=10, y=76)
entry_calendar_expenses = DateEntry(frame_operations, width=10, borderwidth=2, year=2023)
entry_calendar_expenses.place(x=120, y=73)

# Value--------------------
label_value_expenses = Label(frame_operations, text="Total Value", font="Ivy 10 bold")
label_value_expenses.place(x=10, y=115)
entry_value_expenses = ttk.Entry(frame_operations, width=10, justify="left")
entry_value_expenses.place(x=120, y=111)

# Insert Expenses Button--------------------
btn_insert_expenses = ttk.Button(frame_operations, command= create_expenses, image=img_insert, text="Add".upper(), width=6, compound=LEFT)
btn_insert_expenses.place(x=120, y=150)

# Delete Button--------------------
label_delete = Label(frame_operations, text="Delete Action", font="Ivy 10 bold")
label_delete.place(x=10, y=195)
btn_delete = ttk.Button(frame_operations, command=delete_data, image=img_delete, text="Delete".upper(), width=6, compound=LEFT)
btn_delete.place(x=120, y=190)


#-------------------------------------------WORKING ON INCOMES SECTION------------------------------------------

label_info = Label(frame_incomes, text="Enter New Incomes", anchor="nw", font="Verdana 10 bold")
label_info.place(x=10, y=5)

# Calendar--------------------
label_calendar_incomes = Label(frame_incomes, text="Date", anchor="nw", font="Ivy 10 bold")
label_calendar_incomes.place(x=10, y=40)
entry_calendar_incomes = DateEntry(frame_incomes, width=10, borderwidth=2, year=2023)
entry_calendar_incomes.place(x=120, y=36)

# Value--------------------
label_value_incomes = Label(frame_incomes, text="Total Value", font="Ivy 10 bold")
label_value_incomes.place(x=10, y=76)
entry_value_incomes = ttk.Entry(frame_incomes, width=10, justify="left")
entry_value_incomes.place(x=120, y=73)

# Insert Button--------------------
btn_insert_incomes = ttk.Button(frame_incomes, command=create_income, image=img_insert, text="Add".upper(), width=6, compound=LEFT)
btn_insert_incomes.place(x=120, y=111)

# Operation New Category--------------------
label_new_category = Label(frame_incomes, text="New Category", font="Ivy 10 bold")
label_new_category.place(x=10, y=153)
entry_new_category = ttk.Entry(frame_incomes, width=10, justify="left")
entry_new_category.place(x=120, y=150)

# Insert Categories Button--------------------
btn_insert_category = ttk.Button(frame_incomes, command=create_category, image=img_insert, text="Add".upper(), width=6, compound=LEFT)
btn_insert_category.place(x=120, y=190)



root.mainloop()
