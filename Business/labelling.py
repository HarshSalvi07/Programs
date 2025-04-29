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
        sql = "INSERT INTO Records (Sr_No,DOE,Employee_ID,Name,DOP,DOR,Material,Amount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            int(entry_sr_no.get()),
            entry_doe.get(),
            int(entry_id.get()),
            entry_name.get(),
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
    try:
        cursor.execute("SELECT * FROM Records")
        rows = cursor.fetchall()

        record_display.delete(1.0, tk.END)

        if not rows:
            record_display.insert(tk.END, "No Records found \n")
            return
        
        for row in rows:
            line = f"|Sr No:{row[0]}|  |DOE:{row[1]}|  |Name:{row[2]}|  |ID:{row[3]}|  |DOP:{row[4]}|  |DOR:{row[5]}|  |Material:{row[6]}|  |Amount:{row[7]}KG| \n"
            record_display.insert(tk.END, line)
            record_display.insert(tk.END, "-"*120 + "\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))
    

def delete_record():
    try:
        sr_no_to_delete = int(delete_sr_no_entry.get())

        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete Record {sr_no_to_delete}?")

        if not confirm:
            return

        cursor.execute("DELETE FROM Records WHERE Sr_No = %s", (sr_no_to_delete,))
        conn.commit()
        messagebox.showinfo("Success", f"Record with Sr_No {sr_no_to_delete} has been deleted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def records_retireve():
    try:
        employee_id = int(entry_retrieve_id.get())  
        sql = "SELECT * FROM Records WHERE Employee_ID = %s"      
        cursor.execute(sql,(employee_id,))
        row = cursor.fetchone()

        record_display.delete(1.0, tk.END)

        if row:
            line = f"|Sr No:{row[0]}|  |DOE:{row[1]}|  |Name:{row[2]}|  |ID:{row[3]}|  |DOP:{row[4]}|  |DOR:{row[5]}|  |Material:{row[6]}|  |Amount:{row[7]}KG|\n"
            record_display.insert(tk.END, line)
        else:
            record_display.insert(tk.END, "No record found for that Employee ID.\n")
        
    except Exception as e:
        messagebox.showerror("Error",str(e))


def update_record():
    try:
        sr_no_str = entry_update_sr_no.get()
        
        if sr_no_str.strip() == "":
            messagebox.showerror("Error", "Please enter a Serial Number.")
            return 
        
        try:
            sr_no = int(sr_no_str)
        except ValueError:
            messagebox.showerror("Error", "Serial Number must be an integer.")
            return  
        
        sr_no = entry_sr_no.get()
        doe = entry_doe.get()
        emp_id_str = entry_id.get() 
        name = entry_name.get()
        dop = entry_dop.get()
        dor = entry_dor.get()
        material = entry_material.get()
        amount_str = entry_amount.get()  


        if not doe or not emp_id_str or not name or not dop or not dor or not material or not amount_str:
            messagebox.showerror("Error", "All fields must be filled out.")
            return 

        try:
            emp_id = int(emp_id_str)
            amount = int(amount_str)
        except ValueError:
            messagebox.showerror("Error", "Employee ID and Amount must be integers.")
            return 

        sql = "UPDATE Records SET DOE=%s, Employee_ID=%s, Name=%s, DOP=%s, DOR=%s, Material=%s, Amount=%s WHERE Sr_No=%s"
        values = (
            doe,
            emp_id,
            name,
            dop,
            dor,
            material,
            amount,
            sr_no
        )
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showwarning("Update Failed", f"No record found with Sr_No {sr_no}.")
        else:
            messagebox.showinfo("Success", f"Record {sr_no} updated successfully.")
    
    except Exception as e:
        messagebox.showerror("Error while updating record", str(e))

#UI Setup
root = tk.Tk()
root.title("Business Records Manager")

root.configure(bg='#ddffe1')

#Heading 

heading_frame = tk.Frame(root, bd=5, relief="solid",bg='#e3e3e3')
heading_frame.grid(row=0, column=0, columnspan=2, padx = 150,pady=15,sticky='w')

heading_label = tk.Label(heading_frame, text = "Records Manager", font = ("sans-serif",30,"bold"),bg='#e3e3e3')
heading_label.grid(row = 0, column = 0, columnspan = 2, padx = 150, pady=15,sticky='w')

#Fields

labels = ["• SR NO","• DOE (YYYY-MM-DD)","• Name","• Employee ID ", "• DOP (YYYY-MM-DD)","• DOR (YYYY-MM-DD)","• Material","• Amount (KG)"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text, anchor="w")
    label.grid(row=i+1, column=0, padx=50, pady=6, sticky="w")

    entry = tk.Entry(root)
    entry.grid(row=i+1, column=0, padx=200, pady=6, sticky="w")
    entries.append(entry)

entry_sr_no = entries[0]
entry_doe = entries[1]
entry_name = entries[2]
entry_id = entries[3]
entry_dop = entries[4]
entry_dor = entries[5]
entry_material = entries[6]
entry_amount = entries[7]

label_delete = tk.Label(root, text ="• Enter Serial Number to Delete Record", bg="#ffffff")
label_delete.grid(row=7, column=0, padx=400, pady=8, sticky="w")

delete_sr_no_entry = tk.Entry(root)
delete_sr_no_entry.grid(row=8, column=0, padx=510, pady=8, sticky="w")


label_retrieve = tk.Label(root, text = "• Enter Employee ID to Retrieve Record", bg="#ffffff")
label_retrieve.grid(row=4, column=0, padx=400, pady=8, sticky="w")

entry_retrieve_id = tk.Entry(root)
entry_retrieve_id.grid(row=5, column=0, padx=510, pady=8, sticky="w")


label_update = tk.Label(root, text="• Enter Serial Number to Update Record", bg="#ffffff")
label_update.grid(row=1, column=0, padx=400, pady=8, sticky="w")

entry_update_sr_no = tk.Entry(root)
entry_update_sr_no.grid(row=2, column=0, padx=510, pady=8, sticky="w")

#Buttons
tk.Button(root, text = "Insert Records", command = insert_records,bg= '#b5ff6c',activebackground='#9eff3f').grid(row = 9, column=0, padx=50, pady=8, sticky="w")
tk.Button(root, text = "Show Records", command = show_records,bg= '#b5ff6c',activebackground='#9eff3f').grid(row = 9, column=0, padx=200, pady=8, sticky="w")

record_display = tk.Text(root, width = 120, height = 15)
record_display.grid(row = 10, column = 0, columnspan = 2, pady = 10, sticky='w', padx = 50)


tk.Button(root, text="Delete Record", command=delete_record, bg='#ff7c7c', activebackground='#ff4c4c', width = 12).grid(row=8, column=0, padx=400, pady=8, sticky="w")

tk.Button(root, text="Retrieve Record", command=records_retireve, bg='#b5ff6c', activebackground='#9eff3f', width = 12).grid(row=5, column=0, padx=400, pady=8, sticky="w")

tk.Button(root,text="Update Record", command=update_record, bg='#b5ff6c', activebackground='#9eff3f', width = 12).grid(row=2, column=0, padx=400, pady=8, sticky="w")


root.mainloop()