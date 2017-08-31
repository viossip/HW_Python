#import contact
from contact import Contact, ProfessionalContact, FriendContact, ProfessionalFriendContact

contacts = []

def addContact():
    print("Should this contact be Simple (S), Friend (F), Professional (P) or Both (B)?\n"
          "press (x) to exit.")
    while True:
        choice = input("--> ")
        if choice.lower() == 's':
            contacts.append(Contact())
        elif choice.lower() == 'f':
            contacts.append(FriendContact())
        elif choice.lower() == 'p':
            contacts.append(ProfessionalContact())
        elif choice.lower() == 'b':
            contacts.append(ProfessionalFriendContact())
        elif choice.lower() == 'x':
            return
        else:
            errorMessage()
        contacts.sort()
        return


def showContacts():
    if contacts:
        """for index, c in enumerate(contacts):
            print("contact number " + (index+1).__str__() + ": ", end='')
            print(c)"""
        for c in contacts:
            print("contact number " + str(c.contactNumber) + ": " + str(c))
    else:
        print("There is no contacts in the phoneBook!\n")


def editContact():
    print("Enter a valid number of the contact you wish to edit:")
    while True:
        try:
            choice = int(input("--> "))
            break
        except ValueError:
            errorMessage()

    contactReplace = next((contact for contact in contacts if contact.contactNumber == choice), None)

    if contactReplace:
        print("Should this contact be Simple (S), Friend (F), Professional (P) or Both (B)? (x) for exit")
        while True:
            choice = input("--> ")
            print("For the following fields click enter if there's no change,"
                  "a new value if you want to replace the field,"
                  "or x if you want to delete the field (the name field cannot be deleted).")
            if choice.lower() == 's':
                contacts[contacts.index(contactReplace)] = Contact(contactReplace)
            elif choice.lower() == 'f':
                contacts[contacts.index(contactReplace)] = FriendContact(contactReplace)
            elif choice.lower() == 'p':
                contacts[contacts.index(contactReplace)] = ProfessionalContact(contactReplace)
            elif choice.lower() == 'b':
                contacts[contacts.index(contactReplace)] = ProfessionalFriendContact(contactReplace)
            elif choice.lower() == 'x':
                return
            else:
                errorMessage()
            return
    else:
        print("There is no contact with id: " + choice + " in the phonebook!")


def start():
    print("Welcome to the Phone Book!")
    while True:
        choice = menu()
        try:
            choice = int(choice)
            if choice == 1:
                addContact()
            elif choice == 2:
                showContacts()
            elif choice == 3:
                editContact()
            elif choice == 4:
                print(4)
            elif choice == 5:
                print(5)
            elif choice == 6:
                print("\nGoodbye!")
                quit(0)
            else:
                errorMessage()
        except ValueError:
            errorMessage()

def menu():
    print("What would you like to do?\n"
          "1 - Add a new contact\n"
          "2 - Show all contacts\n"
          "3 - Edit a contact\n"
          "4 - Find a contact\n"
          "5 - Delete a contact\n"
          "6 - Exit")
    choice = input("--> ")
    return choice

def errorMessage():
    print("That is not a valid entry. Please try again.\n")

start()