from services.contact_service import *


def menu():
    while True:

        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")

            add_contact(name, phone, email, address)

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            keyword = input("Search: ")
            search_contact(keyword)

        elif choice == "4":
            cid = int(input("Contact ID: "))
            email = input("New Email: ")
            address = input("New Address: ")

            update_contact(cid, email, address)

        elif choice == "5":
            cid = int(input("Contact ID: "))
            delete_contact(cid)

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()