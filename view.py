import sqlite3 as lite
import pandas as pd
con = lite.connect('data.db')

#------------------------INSERT FUNCTIONS------------------------
def insert_category(x):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Category(name) VALUES (?)"
        cur.execute(query, x)

def insert_income(x):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Income(category,added_in,value) VALUES (?,?,?)"
        cur.execute(query, x)

def insert_expenses(x):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Spending(category,spent_in,value) VALUES (?,?,?)"
        cur.execute(query, x)

#------------------------DELETE FUNCTIONS------------------------
def delete_income(x):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Income WHERE ID=?"
        cur.execute(query, x)

def delete_expenses(x):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Spending WHERE ID=?"
        cur.execute(query, x)

#------------------------VISUALIZATION FUNCTIONS------------------------

def visualize_category():
    itens_list = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Category")
        row = cur.fetchall()
        for i in row:
            itens_list.append(i)

    return itens_list

def visualize_income():
    itens_list = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Income")
        row = cur.fetchall()
        for i in row:
            itens_list.append(i)

    return itens_list

def visualize_expenses():
    itens_list = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Spending")
        row = cur.fetchall()
        for i in row:
            itens_list.append(i)

    return itens_list

def table():
    expenses = visualize_expenses()
    incomes = visualize_income()

    table_list = []

    for i in expenses:
        table_list.append(i)
    for i in incomes:
        table_list.append(i)

    return table_list

def bar_values():
    # Total Income ----------------
    income = visualize_income()
    incomes_list = []
    for i in income:
        incomes_list.append(i[3])
    total_income = sum(incomes_list)
    if total_income == 0:
        total_income += 1

    # Total Expenses ----------------
    expense = visualize_expenses()
    expenses_list = []
    for i in expense:
        expenses_list.append(i[3])
    total_expense = sum(expenses_list)

    # Total Balance ----------------
    total_balance = total_income - total_expense
    return [total_income, total_expense, total_balance]

def pie_values():
    expenses = visualize_expenses()
    table_list = []
    for i in expenses:
        table_list.append(i)

    dataframe = pd.DataFrame(table_list, columns= ['id', 'category', 'date', 'value'])
    dataframe = dataframe.groupby('category')['value'].sum()

    list = dataframe.values.tolist()
    list_category = []
    for i in dataframe.index:
        list_category.append(i)

    return ([list_category, list])
