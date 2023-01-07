import sqlite3 as lite
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

def insert_spending(x):
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

def delete_spending(x):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Spending WHERE ID=?"
        cur.execute(query, x)

#------------------------VISUALIZATION FUNCTIONS------------------------
itens_list = []
def visualize_category():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Category")
        row = cur.fetchall()
        for i in row:
            itens_list.append(i)

    return itens_list

def visualize_income():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Income")
        row = cur.fetchall()
        for i in row:
            itens_list.append(i)

    return itens_list

def visualize_spending():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Spending")
        row = cur.fetchall()
        for i in row:
            itens_list.append(i)

    return itens_list
