import re
from enum import Enum

#   Regexes for validate phone numbers and e-mails.
cellPhonePattern = re.compile("^[0-9]{3,9}$")
eMailPattern = re.compile("^[_.0-9a-z-]+@([0-9a-z][0-9a-z-]+.)+[a-z]{2,4}$")

#   Error messages
NAME_ERROR = "The name con not be empty!"
EMAIL_ERROR = "You are trying to insert invalid e-mail address! Try again..."
PHONE_ERROR = "The phone number must contain between 3-9 digits! Try again..."


#   Enum defines the type of user's input
class valueType(Enum):
    phoneValue = 1
    emailValue = 2
    nameValue = 3


def receiveValue(typeVal, inputStr):
    value = input(inputStr)
    if typeVal == valueType.phoneValue:
        while not cellPhonePattern.match(value) and value:
            print(PHONE_ERROR)
            value = input(inputStr)
    elif typeVal == valueType.emailValue:
        while not eMailPattern.match(value) and value:
            print(EMAIL_ERROR)
            value = input(inputStr)
    else:
        while not value:
            print(NAME_ERROR)
            value = input(inputStr)
    return value


#   The main super class of contact.
class Contact:

    contactNumber = 0

    def __init__(self, olderContact = None):
        self.ReadValues(olderContact)
        if not olderContact:
            self.contactNumber = Contact.contactNumber = Contact.contactNumber + 1
        else:
            self.contactNumber = olderContact.contactNumber

    def __str__(self):
        str = ""
        for field in self.__dict__.keys():
            if field != 'contactNumber':
                str += field.title() + ": " + getattr(self, field, '') + ", "
        return str
        #return "contact number " + self.contactNumber.__str__() + ": Name: " + self.name + ", Cell Phone: " + self.cellphone.__str__()

    def __lt__(self, other):
        if isinstance(other, Contact):
            return self.name < other.name
        else:
            return False

    def ReadValues(self, olderContact):

        self.name = receiveValue(valueType.nameValue, "Name: ")
        self.cellphone = receiveValue(valueType.phoneValue, "Cell Phone: ")



class FriendContact (Contact):

    def __init__(self, olderContact=None):
        super(FriendContact, self).__init__()

    def __str__(self):
        return super(FriendContact, self).__str__()
        """return super(FriendContact, self).__str__() +\
               ", Home Phone: " + self.homephone.__str__() + ", Personal e-mail: " + self.personalEmail"""

    def ReadValues(self):
        super(FriendContact,self).ReadValues()

        homephone = input("Home Phone: ")
        while not cellPhonePattern.match(homephone) and homephone:
            print(PHONE_ERROR)
            homephone = input("Home Phone: ")
        self.homephone = homephone

        personalEmail = input("Personal e-mail: ")
        while not eMailPattern.match(personalEmail) and personalEmail:
            print(EMAIL_ERROR)
            personalEmail = input("Personal e-mail: ")
        self.personalEmail = personalEmail

    def __lt__(self, other):
        return super().__lt__(other)


class ProfessionalContact (Contact):

    def __init__(self, olderContact = None):
        super(ProfessionalContact, self).__init__()

    def __str__(self):
        return super(ProfessionalContact, self).__str__()
        """return super(ProfessionalContact, self).__str__() + \
               ", Work Phone: " + self.workphone.__str__() + ", Work e-mail: " + self.workEmail"""

    def __lt__(self, other):
        return super().__lt__(other)

    def ReadValues(self):
        super(ProfessionalContact,self).ReadValues()

        workphone = input("Work Phone: ")
        while not cellPhonePattern.match(workphone) and workphone:
            print(PHONE_ERROR)
            workphone = input("Work Phone: ")
        self.workphone = workphone

        workEmail = input("Work e-mail: ")
        while not eMailPattern.match(workEmail) and workEmail:
            print(EMAIL_ERROR)
            workEmail = input("Work e-mail: ")
        self.workEmail = workEmail


class ProfessionalFriendContact (ProfessionalContact, FriendContact):

    def __init__(self, olderContact = None):
        super(ProfessionalFriendContact, self).__init__()

    def __str__(self):
        return super(ProfessionalContact, self).__str__()

    def __lt__(self, other):
        return super().__lt__(other)

    def ReadValues(self):
        super(ProfessionalFriendContact,self).ReadValues()