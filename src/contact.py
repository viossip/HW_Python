import re
from enum import Enum

#   Regexes for validate phone numbers and e-mails.
cellPhonePattern = re.compile("^[0-9]{3,9}$")
eMailPattern = re.compile("^[_.0-9a-z-]+@([0-9a-z][0-9a-z-]+.)+[a-z]{2,4}$")

#   Error messages
NAME_ERROR = "The name can not be empty!"
EMAIL_ERROR = "You are trying to insert invalid e-mail address! Try again..."
PHONE_ERROR = "The phone number must contain between 3-9 digits! Try again..."


#   Enum defines the type of user's input
class ValueType(Enum):
    phoneValue = 1
    emailValue = 2
    nameValue = 3


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
        #   return "contact number " + self.contactNumber.__str__() + ": Name: " + self.name + ",
        #   Cell Phone: " + self.cellphone.__str__()

    def __lt__(self, other):
        if isinstance(other, Contact):
            return self.name < other.name
        else:
            return False

    def ReadValues(self, olderContact):

        if not olderContact:
            self.name = receiveValue(ValueType.nameValue, "Name: ")
            cellphone = receiveValue(ValueType.phoneValue, "Cell Phone: ")
            if cellphone:
                self.cellphone = cellphone
        else:
            name = receiveValue(ValueType.nameValue, "Name (" + olderContact.name + "):", True)
            self.name = name if name else olderContact.name
            cellphone = receiveValue(ValueType.phoneValue, "Cell Phone (" + olderContact.cellphone + "):")
            self.cellphone = cellphone if cellphone else olderContact.cellphone

class FriendContact (Contact):

    def __init__(self, olderContact=None):
        super(FriendContact, self).__init__(olderContact)

    def __str__(self):
        return super(FriendContact, self).__str__()
        """return super(FriendContact, self).__str__() +\
               ", Home Phone: " + self.homephone.__str__() + ", Personal e-mail: " + self.personalEmail"""

    def ReadValues(self, olderContact):
        super(FriendContact, self).ReadValues(olderContact)

        if not olderContact:
            homephone = receiveValue(ValueType.phoneValue, "Home Phone: ")
            if homephone:
                self.homephone = homephone
            personalEmail = receiveValue(ValueType.emailValue, "Personal e-mail: ")
            if personalEmail:
                self.personalEmail = personalEmail
        else:
            homephone = receiveValue(ValueType.phoneValue, "Home Phone (" + getattr(olderContact, 'homephone', "") + "):")
            if not homephone:
                if getattr(olderContact, 'homephone', None):
                    self.homephone = olderContact.homephone
            else:
                self.homephone = homephone

            personalEmail = receiveValue(ValueType.emailValue, "Personal e-mail (" + getattr(olderContact, 'personalEmail', "") + "):")
            if not personalEmail:
                if getattr(olderContact, 'personalEmail', None):
                    self.personalEmail = olderContact.personalEmail
            else:
                self.personalEmail = personalEmail

    def __lt__(self, other):
        return super().__lt__(other)


class ProfessionalContact (Contact):

    def __init__(self, olderContact = None):
        super(ProfessionalContact, self).__init__(olderContact)

    def __str__(self):
        return super(ProfessionalContact, self).__str__()
        """return super(ProfessionalContact, self).__str__() + \
               ", Work Phone: " + self.workphone.__str__() + ", Work e-mail: " + self.workEmail"""

    def __lt__(self, other):
        return super().__lt__(other)

    def ReadValues(self, olderContact):
        super(ProfessionalContact, self).ReadValues(olderContact)

        if not olderContact:
            workphone = receiveValue(ValueType.phoneValue, "Work Phone: ")
            if workphone:
                self.workphone = workphone

            workEmail = receiveValue(ValueType.emailValue, "Work e-mail: ")
            if workEmail:
                self.workEmail = workEmail
        else:
            workphone = receiveValue(ValueType.phoneValue, "Work Phone (" + getattr(olderContact, 'workphone', "") + "):")
            if not workphone:
                if getattr(olderContact, 'workphone', None):
                    self.workphone = olderContact.workphone
            else:
                self.workphone = workphone

            workEmail = receiveValue(ValueType.emailValue, "Work e-mail (" + getattr(olderContact, 'workEmail', "") + "):")
            if not workEmail:
                if getattr(olderContact, 'workEmail', None):
                    self.workEmail = olderContact.workEmail
            else:
                self.workEmail = workEmail


class ProfessionalFriendContact (ProfessionalContact, FriendContact):

    def __init__(self, olderContact = None):
        super(ProfessionalFriendContact, self).__init__(olderContact)

    def __str__(self):
        return super(ProfessionalContact, self).__str__()

    def __lt__(self, other):
        return super().__lt__(other)

    def ReadValues(self, olderContact):
        super(ProfessionalFriendContact, self).ReadValues(olderContact)


#   The function receives value from user, by type of data.
def receiveValue(typeVal, inputStr, enableEmptyName = False):
    value = input(inputStr)
    if typeVal == ValueType.phoneValue:
        while not cellPhonePattern.match(value) and value:
            print(PHONE_ERROR)
            value = input(inputStr)
    elif typeVal == ValueType.emailValue:
        while not eMailPattern.match(value) and value:
            print(EMAIL_ERROR)
            value = input(inputStr)
    else:
        if not enableEmptyName:
            while not value:
                print(NAME_ERROR)
                value = input(inputStr)

    return value
