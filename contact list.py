
contacts = {}

def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists!")
    else:
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        contacts[name] = phone
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()