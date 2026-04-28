import contacts
import export

def menu():
    print("\n1. Add")
    print("2. View")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Export")
    print("7. Exit")

def run():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            print(contacts.add_contact(name, phone, email, address))

        elif choice == "2":
            data = contacts.view_contacts()
            for name in data:
                print(name, "->", data[name])

        elif choice == "3":
            name = input("Search name: ")
            result = contacts.search_contact(name)
            print(result)

        elif choice == "4":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            print(contacts.update_contact(name, phone, email, address))

        elif choice == "5":
            name = input("Name: ")
            print(contacts.delete_contact(name))

        elif choice == "6":
            print(export.export_contacts())

        elif choice == "7":
            break

        else:
            print("Wrong choice")