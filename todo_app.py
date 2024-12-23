import tkinter as tk

# Function to add a task to the list
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)  # Clear the entry box

# Function to remove a selected task
def remove_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except IndexError:
        pass  # No task selected

# Create the main window
window = tk.Tk()
window.title("To-Do List App")

# Create an entry widget to type tasks
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Create buttons to add and remove tasks
add_button = tk.Button(window, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(window, text="Remove Task", width=20, command=remove_task)
remove_button.pack(pady=5)

# Create a listbox to display tasks
listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)

# Run the application
window.mainloop()
