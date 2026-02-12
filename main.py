
import tkinter as tk

def check_fields():
    # Write your logic here to check whether all fields are filled
    pass

root = tk.Tk()
root.title("Student Information Form")

tk.Label(root, text="Student Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Student ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

submit_button = tk.Button(root, text="Submit")

# Initially hide the button
submit_button.pack_forget()

# You may bind key events to call check_fields()

root.mainloop()
