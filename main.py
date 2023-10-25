import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Initialize an empty dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    email = email_entry.get()

    if name and number:
        contacts[name] = {'Number': number, 'Email': email}
        name_entry.delete(0, 'end')
        number_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        messagebox.showinfo("Contact Management", f"Contact {name} added successfully!")
    else:
        messagebox.showerror("Contact Management", "Name and Phone Number are required!")

# Function to view a contact
def view_contact():
    name = name_entry.get()
    if name in contacts:
        info = contacts[name]
        messagebox.showinfo("Contact Information", f"Name: {name}\nPhone Number: {info['Number']}\nEmail: {info['Email']}")
    else:
        messagebox.showerror("Contact Management", f"Contact {name} not found!")

# Function to delete a contact
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        name_entry.delete(0, 'end')
        number_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        messagebox.showinfo("Contact Management", f"Contact {name} deleted successfully!")
    else:
        messagebox.showerror("Contact Management", f"Contact {name} not found!")

# Create the main window
window = tk.Tk()
window.title("Contact Management System")
window.geometry("400x300")

# Create labels and entry fields for name, number, and email
name_label = ttk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = ttk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

number_label = ttk.Label(window, text="Phone Number:")
number_label.grid(row=1, column=0, padx=10, pady=10)
number_entry = ttk.Entry(window)
number_entry.grid(row=1, column=1, padx=10, pady=10)

email_label = ttk.Label(window, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=10)
email_entry = ttk.Entry(window)
email_entry.grid(row=2, column=1, padx=10, pady=10)

# Create buttons for Add, View, and Delete
add_button = ttk.Button(window, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, padx=10, pady=10)

view_button = ttk.Button(window, text="View Contact", command=view_contact)
view_button.grid(row=3, column=1, padx=10, pady=10)

delete_button = ttk.Button(window, text="Delete Contact", command=delete_contact)
delete_button.grid(row=3, column=2, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
