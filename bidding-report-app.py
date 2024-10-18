from tkinter import *
from datetime import datetime

def update_total_count():
    """Calculate and update the total count entry."""
    total_count = sum(int(entry.get()) for entry in entries)
    total_count_entry.delete(0, 'end')
    total_count_entry.insert(0, str(total_count))

def plus_count(index):
    value = entries[index].get()
    count = int(value)
    count += 1
    entries[index].delete(0, 'end')
    entries[index].insert(0, str(count))
    now = datetime.now()
    current_time= now.strftime("%Y-%m-%d %H:%M")  # Format: YYYY-MM-DD HH:MM
    updated_time_labels[index].config(text=current_time) 
    update_total_count()

def minus_count(index):
    value = entries[index].get()
    count = int(value)
    count -= 1
    entries[index].delete(0, 'end')
    entries[index].insert(0, str(count))
    update_total_count()


def update_current_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
    current_time_lebel.config(text=current_time)
    current_time_lebel.after(1000, update_current_time)  # Update the time every 1000 ms (1 second)

def write_to_file():
    with open("output.txt", "a") as file:  # Use 'a' to append to the file
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Current Date and Time: {current_time}\n")
        for category, entry in zip(categories, entries):
            file.write(f"{category}: {entry.get()}\n")
        file.write("\n")  # Add a newline for separation between entries
    print("Data written to output.txt")  # Confirmation in console

def format_entries():
    """Reset all entries to their initial state (0)."""
    for entry in entries:
        entry.delete(0, 'end')
        entry.insert(0, 0)  # Reset to zero
    update_total_count()  # Update the total count after reset


root = Tk()
root.title("Simple GUI")

# Label to display current date and time
current_time_lebel = Label(root, font=("Helvetica", 12))
current_time_lebel.grid(row=0, columnspan=4, pady=15)

categories = ["Upwork", "Indeed", "Wellfound", "Others"]
entries = []
updated_time_labels = []
now = datetime.now()

for index, category in enumerate(categories):
    Label(root, text=category).grid(row=index + 1, padx=10, pady=15)  # Adjust row to start from 1
    entries.append(Entry(root))
    entries[index].grid(row=index + 1, column=1, padx=10)
    entries[index].insert(0, 0)
    plus_button = Button(root, text="+", width=20, command=lambda i=index: plus_count(i))
    plus_button.grid(row=index + 1, column=2, padx=10)
    minus_button = Button(root, text="-", width=20, command=lambda i=index: minus_count(i))
    minus_button.grid(row=index + 1, column=3, padx=10)
    updated_time_labels.append(Label(root, font=("Helvetica", 10), text=now.strftime("%Y-%m-%d %H:%M") ))
    updated_time_labels[index].grid(row= index + 1, column=4, padx=10)

# Entry for total count
Label(root, text="Total").grid(row=len(categories)+1, column=0, padx=10)
total_count_entry = Entry(root, font=("Helvetica", 10))
total_count_entry.grid(row=len(categories) + 1, column=1, padx=10, pady=10)

format_button = Button(root, text="Format", width=20, command=format_entries)
output_button = Button(root, text="Output", width=20, command=write_to_file)
format_button.grid(row=len(categories)+2, column=0, padx=10, pady=10)
output_button.grid(row=len(categories)+2, column=1)
# Start updating the time
update_current_time()

root.mainloop()
