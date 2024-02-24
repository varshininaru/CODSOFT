import tkinter as tk
from tkinter import messagebox

class Person:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Manager:
    def __init__(self):
        self.people = []
        
    def add_person(self, person):
        self.people.append(person)
    
    def delete_person(self, person):
        self.people.remove(person)
    
    def search_person(self, keyword):
        results = []
        for person in self.people:
            if keyword.lower() in person.name.lower() or keyword in person.phone:
                results.append(person)
        return results

class ContactApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contacts")
        
        self.manager = Manager()
        
        self.lbl_name = tk.Label(master, text="Name:")
        self.lbl_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.lbl_phone = tk.Label(master, text="Phone:")
        self.lbl_phone.grid(row=1, column=0, padx=10, pady=5)
        self.entry_phone = tk.Entry(master)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        self.lbl_email = tk.Label(master, text="Email:")
        self.lbl_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.lbl_address = tk.Label(master, text="Address:")
        self.lbl_address.grid(row=3, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(master)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        self.btn_add = tk.Button(master, text="➕ Add", command=self.add_person)
        self.btn_add.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.entry_search = tk.Entry(master)
        self.entry_search.grid(row=5, column=0, padx=10, pady=5)
        self.btn_search = tk.Button(master, text="🔍 Search", command=self.search_person)
        self.btn_search.grid(row=5, column=1, padx=10, pady=5)

        self.listbox_contacts = tk.Listbox(master, width=40, height=10)
        self.listbox_contacts.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.btn_view = tk.Button(master, text="👀 View All", command=self.view_people)
        self.btn_view.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        self.btn_delete = tk.Button(master, text="❌ Delete", command=self.delete_person)
        self.btn_delete.grid(row=8, column=0, padx=10, pady=5)

    def add_person(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        if name and phone:
            person = Person(name, phone, email, address)
            self.manager.add_person(person)
            messagebox.showinfo("Success", "Person added!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and phone number required.")

    def search_person(self):
        keyword = self.entry_search.get()
        if keyword:
            results = self.manager.search_person(keyword)
            self.display_people(results)
        else:
            messagebox.showwarning("Warning", "Enter a search keyword.")

    def view_people(self):
        self.display_people(self.manager.people)

    def display_people(self, people):
        self.listbox_contacts.delete(0, tk.END)
        for person in people:
            self.listbox_contacts.insert(tk.END, f"{person.name} - {person.phone}")

    def delete_person(self):
        selected_index = self.listbox_contacts.curselection()
        if selected_index:
            person = self.manager.people[selected_index[0]]
            self.manager.delete_person(person)
            self.view_people()
            messagebox.showinfo("Success", "Person deleted.")
        else:
            messagebox.showwarning("Warning", "Select a person to delete.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
