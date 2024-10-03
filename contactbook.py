
def show_menu():
    print("\nContact Book Menu:")
    print("1. View Contact List")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} | Phone: {contact['phone']}")


def add_contact(contacts):
    name = input("\nEnter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"Contact '{name}' added successfully.")

def search_contact(contacts):
    search_term = input("\nEnter the contact name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
    else:
        print(f"No contacts found for '{search_term}'.")

def update_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            contact_num = int(input("\nEnter the contact number to update: "))
            if 1 <= contact_num <= len(contacts):
                contact = contacts[contact_num - 1]
                print(f"Updating contact: {contact['name']}")
                contact['name'] = input(f"Enter new name (or press Enter to keep '{contact['name']}'): ") or contact['name']
                contact['phone'] = input(f"Enter new phone number (or press Enter to keep '{contact['phone']}'): ") or contact['phone']
                contact['email'] = input(f"Enter new email (or press Enter to keep '{contact['email']}'): ") or contact['email']
                contact['address'] = input(f"Enter new address (or press Enter to keep '{contact['address']}'): ") or contact['address']
                print("Contact updated successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input.")


def delete_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            contact_num = int(input("\nEnter the contact number to delete: "))
            if 1 <= contact_num <= len(contacts):
                removed_contact = contacts.pop(contact_num - 1)
                print(f"Contact '{removed_contact['name']}' deleted successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input.")

def contact_book():
    contacts = []
    while True:
        show_menu()
        choice = input("\nChoose an option (1-6): ")

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    contact_book()
