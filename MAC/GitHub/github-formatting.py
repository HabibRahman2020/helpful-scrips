import tkinter as tk
from tkinter import ttk


def generate_table():
    # Get user input
    ticket = ticket_entry.get()
    reason = reason_entry.get()
    approve = approve_entry.get()
    email = email_entry.get()
    image = image_entry.get()

    # Generate table
    table = f"| Ticket | Reason | Approve | Email | Image |\n"\
            f"|--------|--------|---------|-------|-------|\n"\
            f"| {ticket} | {reason} | {approve} | {email} | {image} |"

    # Save table to file
    file_path = "github_table.txt"  # Removed the "~" character from the file path
    with open(file_path, "w") as file:
        file.write(table)

    result_label.config(text="Table generated and saved to file.")


# Create the main window
window = tk.Tk()
window.title("GitHub Table Generator")
window.geometry("400x300")  # Set window size

# Center the window on the screen
window.eval('tk::PlaceWindow . center')

# Create a frame for better organization
frame = ttk.Frame(window)
frame.pack(pady=20)

# Create labels and entries for user input
ticket_label = ttk.Label(frame, text="Ticket:")
ticket_label.grid(row=0, column=0, padx=5, pady=5)
ticket_entry = ttk.Entry(frame)
ticket_entry.grid(row=0, column=1, padx=5, pady=5)

reason_label = ttk.Label(frame, text="Reason:")
reason_label.grid(row=1, column=0, padx=5, pady=5)
reason_entry = ttk.Entry(frame)
reason_entry.grid(row=1, column=1, padx=5, pady=5)

approve_label = ttk.Label(frame, text="Approve:")
approve_label.grid(row=2, column=0, padx=5, pady=5)
approve_entry = ttk.Entry(frame)
approve_entry.grid(row=2, column=1, padx=5, pady=5)

email_label = ttk.Label(frame, text="Email:")
email_label.grid(row=3, column=0, padx=5, pady=5)
email_entry = ttk.Entry(frame)
email_entry.grid(row=3, column=1, padx=5, pady=5)

image_label = ttk.Label(frame, text="Image:")
image_label.grid(row=4, column=0, padx=5, pady=5)
image_entry = ttk.Entry(frame)
image_entry.grid(row=4, column=1, padx=5, pady=5)

# Create a button to generate the table
generate_button = ttk.Button(
    window, text="Generate Table", command=generate_table)
generate_button.pack(pady=10)

# Create a label to display the result
result_label = ttk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
