import secrets
import string
import tkinter as tk
from tkinter import messagebox


def create_pw(pw_length=16):
    letters = string.ascii_letters.translate(str.maketrans('', '', 'oO'))
    digits = string.digits.translate(str.maketrans('', '', '0'))
    special_chars = string.punctuation.translate(str.maketrans('', '', '\'"'))

    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(pw_length))

        if (
            any(char in special_chars for char in pwd) and
            sum(char in digits for char in pwd) >= 2
        ):
            pw_strong = True

    return pwd


def show_password():
    password = create_pw()
    password_label.config(text="Here is your {} character password:\n\n{}".format(
        len(password), password))
    ok_button.grid(row=2, column=0, pady=10)  # Display the "OK" button
    root.update_idletasks()  # Update the window layout
    # Minimum width of 400 or adjust based on label width
    width = max(400, password_label.winfo_reqwidth() + 20)
    height = ok_button.winfo_height() + password_label.winfo_reqheight() + \
        120  # Adjust height based on label and button
    root.geometry("{}x{}".format(width, height))  # Set the window dimensions


def close_prompt():
    root.quit()


root = tk.Tk()
root.title("Password Generator")

# Create a grid layout with flexible row and column weights
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

button = tk.Button(root, text="Generate Password", command=show_password)
# Place the "Generate Password" button in row 0, column 0
button.grid(row=0, column=0, pady=20)

password_label = tk.Label(root, text="", wraplength=300)
# Place the password label in row 1, column 0
password_label.grid(row=1, column=0, pady=10)

ok_button = tk.Button(root, text="OK", command=close_prompt)
# Place the "OK" button in row 2, column 0
ok_button.grid(row=2, column=0, pady=10)
ok_button.grid_remove()  # Initially hide the "OK" button

root.mainloop()
