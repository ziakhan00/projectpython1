import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Zia Ur Rehman - SU-21-02-002-003")
root.geometry("300x200")

# Function to run when button is clicked
def on_button_click():
    messagebox.showinfo("Message", "Hello from Zia Ur Rehman!")

# Create a button
btn = tk.Button(root, text="Click Me", command=on_button_click)
btn.pack(pady=50)

# Run the application
root.mainloop()
