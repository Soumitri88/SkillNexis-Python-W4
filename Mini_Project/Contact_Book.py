#Build a Contact Book app using dictionary.

# Contact Book using Dictionary

contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found!")

def update_contact():
    name = input("Enter name to update: ").strip()

    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        contacts[name] = phone
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def display_contacts():
    if not contacts:
        print("Contact book is empty!")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"Name: {name} | Phone: {phone}")

# Main menu
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice! Please enter 1-6.")
