import os
import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    self.contacts.append(Contact(**item))

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()
        print("✅ Contact added.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. {contact}")

    def search_contact(self):
        key = input("Enter name to search: ").lower()
        found = False
        for contact in self.contacts:
            if key in contact.name.lower():
                print(contact)
                found = True
        if not found:
            print("❌ Contact not found.")

    def update_contact(self):
        self.display_contacts()
        try:
            index = int(input("Enter contact number to update: ")) - 1
            if 0 <= index < len(self.contacts):
                name = input("New name: ")
                phone = input("New phone: ")
                email = input("New email: ")
                self.contacts[index] = Contact(name, phone, email)
                self.save_contacts()
                print("✅ Contact updated.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input.")

    def delete_contact(self):
        self.display_contacts()
        try:
            index = int(input("Enter contact number to delete: ")) - 1
            if 0 <= index < len(self.contacts):
                del self.contacts[index]
                self.save_contacts()
                print("✅ Contact deleted.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input.")

def main():
    book = ContactBook()
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            book.add_contact()
        elif choice == '2':
            book.display_contacts()
        elif choice == '3':
            book.search_contact()
        elif choice == '4':
            book.update_contact()
        elif choice == '5':
            book.delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
