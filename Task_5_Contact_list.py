import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x400")
        self.contacts = []

        
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)

        self.gradient_frame = tk.Frame(root, bg="#E0C3FC")
        self.gradient_frame.place(relwidth=1, relheight=1)

        
        self.title_label = tk.Label(self.gradient_frame, text="Contact Book", font=("Helvetica", 18, "bold"), bg="#E0C3FC")
        self.title_label.pack(pady=10)

        
        self.button_frame = tk.Frame(self.gradient_frame, bg="#E0C3FC")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact_window, bg="#C9A3E8", font=("Helvetica", 12), width=15)
        self.add_button.grid(row=0, column=0, padx=5)

        self.view_button = tk.Button(self.button_frame, text="View Contacts", command=self.view_contacts, bg="#C9A3E8", font=("Helvetica", 12), width=15)
        self.view_button.grid(row=0, column=1, padx=5)

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact_window, bg="#C9A3E8", font=("Helvetica", 12), width=15)
        self.search_button.grid(row=0, column=2, padx=5)

    def add_contact_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Contact")
        add_window.geometry("400x300")

        tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(add_window, width=30)
        name_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Phone:").grid(row=1, column=0, padx=10, pady=10)
        phone_entry = tk.Entry(add_window, width=30)
        phone_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Email:").grid(row=2, column=0, padx=10, pady=10)
        email_entry = tk.Entry(add_window, width=30)
        email_entry.grid(row=2, column=1)

        tk.Label(add_window, text="Address:").grid(row=3, column=0, padx=10, pady=10)
        address_entry = tk.Entry(add_window, width=30)
        address_entry.grid(row=3, column=1)

        def save_contact():
            name = name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            address = address_entry.get()
            if name and phone:
                self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
                messagebox.showinfo("Success", "Contact added successfully")
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Name and Phone are required")

        save_button = tk.Button(add_window, text="Save", command=save_contact, bg="#C9A3E8", font=("Helvetica", 12), width=10)
        save_button.grid(row=4, column=1, pady=10)

    def view_contacts(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Contacts")
        view_window.geometry("500x400")

        for index, contact in enumerate(self.contacts):
            frame = tk.Frame(view_window)
            frame.pack(anchor="w", pady=5, padx=10)

            tk.Label(frame, text=f"{index+1}. {contact['name']} - {contact['phone']}", font=("Helvetica", 12)).pack(side="left")

            edit_button = tk.Button(frame, text="Edit", command=lambda i=index: self.edit_contact_window(i), bg="#C9A3E8", font=("Helvetica", 10), width=5)
            edit_button.pack(side="left", padx=5)

            delete_button = tk.Button(frame, text="Delete", command=lambda i=index: self.delete_contact(i), bg="#FF6F61", font=("Helvetica", 10), width=7)
            delete_button.pack(side="left", padx=5)

    def edit_contact_window(self, index):
        contact = self.contacts[index]

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Contact")
        edit_window.geometry("400x300")

        tk.Label(edit_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(edit_window, width=30)
        name_entry.grid(row=0, column=1)
        name_entry.insert(0, contact["name"])

        tk.Label(edit_window, text="Phone:").grid(row=1, column=0, padx=10, pady=10)
        phone_entry = tk.Entry(edit_window, width=30)
        phone_entry.grid(row=1, column=1)
        phone_entry.insert(0, contact["phone"])

        tk.Label(edit_window, text="Email:").grid(row=2, column=0, padx=10, pady=10)
        email_entry = tk.Entry(edit_window, width=30)
        email_entry.grid(row=2, column=1)
        email_entry.insert(0, contact["email"])

        tk.Label(edit_window, text="Address:").grid(row=3, column=0, padx=10, pady=10)
        address_entry = tk.Entry(edit_window, width=30)
        address_entry.grid(row=3, column=1)
        address_entry.insert(0, contact["address"])

        def save_changes():
            self.contacts[index] = {
                "name": name_entry.get(),
                "phone": phone_entry.get(),
                "email": email_entry.get(),
                "address": address_entry.get(),
            }
            messagebox.showinfo("Success", "Contact updated successfully")
            edit_window.destroy()

        save_button = tk.Button(edit_window, text="Save", command=save_changes, bg="#C9A3E8", font=("Helvetica", 12), width=10)
        save_button.grid(row=4, column=1, pady=10)

    def delete_contact(self, index):
        confirm = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
        if confirm:
            del self.contacts[index]
            messagebox.showinfo("Success", "Contact deleted successfully")
            self.view_contacts()

    def search_contact_window(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Contact")
        search_window.geometry("400x200")

        tk.Label(search_window, text="Search by Name or Phone:").grid(row=0, column=0, padx=10, pady=10)
        search_entry = tk.Entry(search_window, width=30)
        search_entry.grid(row=0, column=1)

        def search():
            query = search_entry.get()
            results = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
            if results:
                result_window = tk.Toplevel(self.root)
                result_window.title("Search Results")
                result_window.geometry("400x300")
                for contact in results:
                    tk.Label(result_window, text=f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}", font=("Helvetica", 12)).pack(anchor="w", padx=10, pady=5)
            else:
                messagebox.showinfo("No Results", "No contacts found")

        search_button = tk.Button(search_window, text="Search", command=search, bg="#C9A3E8", font=("Helvetica", 12), width=10)
        search_button.grid(row=1, column=1, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
