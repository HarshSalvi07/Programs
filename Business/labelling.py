#SQL connection
import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "Business",
)

cursor = conn.cursor()

#For insertion of records
def insert_records():
    try:
        sql = "INSERT INTO Records (Employee_ID,Name,DOJ,DOP,DOR,Material,Amount) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (
            int(entry_id.get()),
            entry_name.get(),
            entry_doj.get(),
            entry_dop.get(),
            entry_dor.get(),
            entry_material.get(),
            int(entry_amount.get())
        )

        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Successfully inserted records")
    except Exception as e:
        messagebox.showerror("Error while inserting records", str(e))

#Function for showing the records
def show_records():
    cursor.execute("SELECT * FROM Records")
    rows = cursor.fetchall()
    display_text = ""
    for row in rows:
        emp_id = row[0]
        name = row[1]
        doj = str(row[2])
        dop = str(row[3])
        dor = str(row[4])
        material = row[5]
        amount = row[6]
        display_text += str("------------------------------------------------------------------------------") + "\n"
        display_text += f"Employee ID = {emp_id}, Name = {name}, DOJ = {doj}, DOP = {dop}, DOR = {dor}, Material = {material}, Amount = {amount}" "\n"
    messagebox.showinfo("All Records", display_text)

#UI Setup
root = tk.Tk()
root.title("Business Records Manager")

#Fields
labels = ["Employee ID","Name","DOJ (YYYY-MM-DD)","DOP (YYYY-MM-DD)","DOR (YYYY-MM-DD)","Material","Amount (KG)"]
entries = []

for i,label in enumerate(labels):
    tk.Label(root, text = label).grid(row = i ,column = 0,pady=5)
    entry = tk.Entry(root)
    entry.grid(row = i, column = 1, pady = 5)
    entries.append(entry)

entry_id = entries[0]
entry_name = entries[1]
entry_doj = entries[2]
entry_dop = entries[3]
entry_dor = entries[4]
entry_material = entries[5]
entry_amount = entries[6]

#Buttons
tk.Button(root, text = "Insert Records", command = insert_records).grid(row = 7, column = 0 ,pady = 10)
tk.Button(root, text = "Show Records", command = show_records).grid(row = 7, column = 1, pady = 10)

root.mainloop()