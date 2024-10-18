from tkinter import *

# def greet():
#     label.config(text="Hello, World!")

root = Tk()
root.title("Simple GUI")


Label(root, text="Upwork").grid(row=0, padx=20, pady=20)
Label(root, text="Indeed").grid(row=1, padx=20, pady=20)
Label(root, text="Wellfound").grid(row=2, padx=20, pady=20)
Label(root, text="Others").grid(row=3, padx=20, pady=20)

entry_upwork = Entry(root)
entry_indeed = Entry(root)
entry_wellfound = Entry(root)
entry_others = Entry(root)

entry_upwork.grid(row=0, column=1)
entry_indeed.grid(row=1, column=1)
entry_wellfound.grid(row=2, column=1)
entry_others.grid(row=3, column=1)

# button = tk.Button(root, text="Greet", width=100, command=greet)
# button.pack(pady=10)

root.mainloop()
