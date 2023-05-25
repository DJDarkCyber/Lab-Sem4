import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL
    )
    '''
)

conn.commit()

def add_employee():
    name = name_entry.get()
    position = position_entry.get()
    if name and position:
        cursor.execute("INSERT INTO employees (name, position) VALUES(?, ?)", (name, position))
        conn.commit()
        messagebox.showinfo("Success", "Employee added successfully.")
        clear_entries()
        display_employees()
    else:
        messagebox.showwarning("Incomplete Information", "Please provide both name and position.")

def delete_employee():
    selected_item = employee_listbox.curselection()
    if selected_item:
        employee_id = employee_listbox.get(selected_item)[0]
        # Delete the selected employee from the database
        cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
        conn.commit()
        messagebox.showinfo("Success", "Employee deleted successfully.")
        display_employees()
    else:
        messagebox.showwarning("No Employee Selected", "Please select an employee to delete.")

def clear_entries():
    name_entry.delete(0, tk.END)
    position_entry.delete(0, tk.END)

def display_employees():
    # Clear the employee listbox
    employee_listbox.delete(0, tk.END)
    # Retrieve all employees from the database
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    for employee in employees:
        employee_listbox.insert(tk.END, employee)
# Create the main window
window = tk.Tk()
window.title("Employee Management System")

# Create and place the labels
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, sticky="E")
position_label = tk.Label(window, text="Position:")
position_label.grid(row=1, column=0, sticky="E")

# Create and place the entry fields
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)
position_entry = tk.Entry(window)
position_entry.grid(row=1, column=1)

# Create and place the buttons
add_button = tk.Button(window, text="Add Employee", command=add_employee)
add_button.grid(row=2, column=0, columnspan=2, pady=10)
delete_button = tk.Button(window, text="Delete Employee", command=delete_employee)
delete_button.grid(row=3, column=0, columnspan=2, pady=10)
clear_button = tk.Button(window, text="Clear Entries", command=clear_entries)
clear_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create and place the employee listbox
employee_listbox = tk.Listbox(window, width=40)
employee_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Display the employees in the listbox
display_employees()

# Start the Tkinter event loop
window.mainloop()

# Close the database connection when the window is closed
conn.close()
