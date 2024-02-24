import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        self.tasks = []
        
        # Entry for adding tasks
        self.task_entry = tk.Entry(master, width=40, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task Button
        self.add_button = tk.Button(master, text="➕ Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
        self.add_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Task Listbox
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=40, height=10, font=("Helvetica", 12))
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Delete Task Button
        self.delete_button = tk.Button(master, text="🗑️ Delete Task", command=self.delete_task, bg="#f44336", fg="white", font=("Helvetica", 10, "bold"))
        self.delete_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Update Task Button
        self.update_button = tk.Button(master, text="🔄 Update Task", command=self.update_task, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"))
        self.update_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    def add_task(self):
        task = self.task_entry.get()
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if task:
            self.tasks.append((task, time))
            self.task_listbox.insert(tk.END, f"{task} - Saved at: {time}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            updated_task = simpledialog.askstring("Input", "Update task:", parent=self.master)
            if updated_task:
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.tasks[selected_task_index[0]] = (updated_task, time)
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index[0], f"{updated_task} - Saved at: {time}")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
