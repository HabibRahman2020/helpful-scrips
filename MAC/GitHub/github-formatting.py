import tkinter as tk


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

# Create labels and entries for user input
ticket_label = tk.Label(window, text="Ticket:")
ticket_label.grid(row=0, column=0)
ticket_entry = tk.Entry(window)
ticket_entry.grid(row=0, column=1)

reason_label = tk.Label(window, text="Reason:")
reason_label.grid(row=1, column=0)
reason_entry = tk.Entry(window)
reason_entry.grid(row=1, column=1)

approve_label = tk.Label(window, text="Approve:")
approve_label.grid(row=2, column=0)
approve_entry = tk.Entry(window)
approve_entry.grid(row=2, column=1)

email_label = tk.Label(window, text="Email:")
email_label.grid(row=3, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=3, column=1)

image_label = tk.Label(window, text="Image:")
image_label.grid(row=4, column=0)
image_entry = tk.Entry(window)
image_entry.grid(row=4, column=1)

# Create a button to generate the table
generate_button = tk.Button(
    window, text="Generate Table", command=generate_table)
generate_button.grid(row=5, columnspan=2)

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.grid(row=6, columnspan=2)

# Start the GUI event loop
window.mainloop()
