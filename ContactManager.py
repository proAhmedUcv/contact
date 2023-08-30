class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' removed successfully.")
                return
        print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)
                print("--------------------")


# Create a ContactManager instance
contact_manager = ContactManager()

while True:
    print("Contact Manager Menu:")
    print("1. Add contact")
    print("2. Remove contact")
    print("3. Search contact")
    print("4. Display contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact = Contact(name, phone, email)
        contact_manager.add_contact(contact)
    elif choice == "2":
        name = input("Enter name: ")
        contact_manager.remove_contact(name)
    elif choice == "3":
        name = input("Enter name: ")
        result = contact_manager.search_contact(name)
        if result:
            print("\n*****************\nContact found:\n************************")
            print(result)
        else:
            print("\n*****************\nContact not found.\n*******************\n")
    elif choice == "4":
        contact_manager.display_contacts()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")







 
# 1. Start

# 1. Define the class Contact with attributes:

#    - name
#    - phone
#    - email

#    and methods:

#    - init(name, phone, email): Initialize the contact object with the provided name, phone, and email.
#    - str(): Return a string representation of the contact.

# 1. Define the class ContactManager with attributes:

#    - contacts (list): Initialize an empty list to store contacts.

#    and methods:

#    - add_contact(contact): Add the provided contact object to the contacts list.
#    - remove_contact(name): Remove the contact with the given name from the contacts list if it exists.
#    - search_contact(name): Search for a contact with the given name in the contacts list. If found, return the contact object; otherwise, return None.
#    - display_contacts(): Display all the contacts in the contacts list. If no contacts are found, print "No contacts found".

# 1. Create an instance of the ContactManager class called contact_manager.

# 1. Loop:

#    - Print the contact management menu:

#      - "1. Add contact"
#      - "2. Remove contact"
#      - "3. Search contact"
#      - "4. Display contacts"
#      - "5. Exit"

#    - Read the user's choice.

#    - If the choice is 1:

#      - Read the name, phone, and email from the user.
#      - Create a new Contact object with the provided information.
#      - Call the add_contact() method of contact_manager, passing the Contact object.

#    - If the choice is 2:

#      - Read the name of the contact to be removed from the user.
#      - Call the remove_contact() method of contact_manager, passing the name.

#    - If the choice is 3:

#      - Read the name of the contact to be searched from the user.
#      - Call the search_contact() method of contact_manager, passing the name.
#      - If a contact is found, print its details.
#      - If no contact is found, print "Contact not found".

#    - If the choice is 4:

#      - Call the display_contacts() method of contact_manager.

#    - If the choice is 5:

#      - Print "Exiting program."
#      - Break the loop.

#    - If the choice is invalid:

#      - Print "Invalid choice. Please try again."

# 1. End

 