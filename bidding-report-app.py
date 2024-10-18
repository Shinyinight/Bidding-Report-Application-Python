from tkinter import *
from datetime import datetime

def plus_count(index):
    value = entries[index].get()
    count = int(value)
    count += 1
    entries[index].delete(0, 'end')
    entries[index].insert(0, str(count))

    now = datetime.now()
    current_time= now.strftime("%Y-%m-%d %H:%M")  # Format: YYYY-MM-DD HH:MM
    updated_time_labels[index].config(text=current_time) 

def minus_count(index):
    value = entries[index].get()
    count = int(value)
    count -= 1
    entries[index].delete(0, 'end')
    entries[index].insert(0, str(count))

def update_current_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
    current_time_lebel.config(text=current_time)
    current_time_lebel.after(1000, update_current_time)  # Update the time every 1000 ms (1 second)

root = Tk()
root.title("Simple GUI")

# Label to display current date and time
current_time_lebel = Label(root, font=("Helvetica", 12))
current_time_lebel.grid(row=0, columnspan=4, pady=15)

categories = ["Upwork", "Indeed", "Wellfound", "Others"]
entries = []
updated_time_labels = []

for index, category in enumerate(categories):
    Label(root, text=category).grid(row=index + 1, padx=10, pady=15)  # Adjust row to start from 1
    entries.append(Entry(root))
    entries[index].grid(row=index + 1, column=1, padx=10)
    entries[index].insert(0, 0)
    plus_button = Button(root, text="+", width=20, command=lambda i=index: plus_count(i))
    plus_button.grid(row=index + 1, column=2, padx=10)
    minus_button = Button(root, text="-", width=20, command=lambda i=index: minus_count(i))
    minus_button.grid(row=index + 1, column=3, padx=10)
    updated_time_labels.append(Label(root, text="initial"))
    updated_time_labels[index].grid(row= index + 1, column=4, padx=10)

format_button = Button(root, text="Format", width=20)
output_button = Button(root, text="Output", width=20)
# Start updating the time
update_current_time()

root.mainloop()
