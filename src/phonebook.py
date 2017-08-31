#import contact
from contact import Contact, ProfessionalContact, FriendContact, ProfessionalFriendContact

contacts = []


def addContact():
    while True:
        print("Should this contact be Simple (S), Friend (F), Professional (P) or Both (B)?\n"
              "press (x) to exit.")
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
            continue
        contacts.sort()
        return


def showContacts(formFindMatches = None):
    if not formFindMatches:
        if contacts:
            for c in contacts:
                print("contact number " + str(c.contactNumber) + ": " + str(c))
        else:
            print("There is no contacts in the phoneBook!\n")
    else:
        for c in formFindMatches:
                print("contact number " + str(c.contactNumber) + ": " + str(c))


def editContact():
    if contacts:
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
                contacts.sort()
                return
        else:
            print("There is no contact with id: " + str(choice) + " in the phonebook!")
    else:
        print("There is no contacts in the phoneBook!\n")


def findContact():
    print("Type contact details (name, phone, email):")
    inputs = input("--> ").split(',')
    for element in inputs:
        matchContacts = [x for i, x in enumerate(contacts) if x.Match(element.strip())]
        if matchContacts:
            showContacts(matchContacts)
        else:
            print("There is no matches in the phone book!")


def deleteContact():
    if contacts:
        while True:
            print("Enter a valid number of the contact you wish to delete:")
            try:
                contactID = int(input("--> "))
                break
            except ValueError:
                errorMessage()

        contactDelete = next((contact for contact in contacts if contact.contactNumber == contactID), None)
        if contactDelete:
            contacts.remove(contactDelete)
        else:
            print("There is no contact with id: " + str(contactID) + " in the phonebook!")
    else:
        print("There is no contacts in the phoneBook!\n")


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
                findContact()
            elif choice == 5:
                deleteContact()
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