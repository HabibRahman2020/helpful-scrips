import random
import string
import paperclip
import tkinter as tk

def generate_password():
    length = int(length_entry.get())
    exclude = ['0', 'i', 'l']
    chars = ''.join([char for char in string.ascii_letters + string.digits if char not in exclude])
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")

length_label = tk.Label(root, text="Length")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()

password_entry = tk.Entry(root)
password_entry.pack()

copy_button = tk.Button(root, text="Copy", command=lambda: pyperclip.copy(password_entry.get()))
copy_button.pack()

root.mainloop()