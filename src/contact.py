#   Vitaly Osipenkov
#   ID: 324716448

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

    #   This is the 3rd short non-pythonic way to avoid duplications (in the diamond problem)
    #   __str__ in the parent class simply prints all existing attributes in the received object.
    def __str__(self):
        myStr = ""
        for field in self.__dict__.keys():
            if field != 'contactNumber':
                myStr += field.title() + ": " + getattr(self, field, '') + ", "
        return myStr

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

            cellphone = receiveValue(ValueType.phoneValue, "Cell Phone (" + getattr(olderContact, 'cellphone', "") + "):", True)
            if not cellphone:
                if getattr(olderContact, 'cellphone', None):
                    self.cellphone = olderContact.cellphone
            else:
                self.cellphone = cellphone
                if (self.cellphone is "x"):
                    del self.cellphone

    def Match(self, matchStr):
        for field in self.__dict__.keys():
            if str(getattr(self, field, '')).find(matchStr) != -1:
                return True
        return False


class FriendContact (Contact):

    def __init__(self, olderContact=None):
        super(FriendContact, self).__init__(olderContact)

    def __str__(self):
        return super(FriendContact, self).__str__()

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
            homephone = receiveValue(ValueType.phoneValue, "Home Phone (" + getattr(olderContact, 'homephone', "") + "):", True)
            if not homephone:
                if getattr(olderContact, 'homephone', None):
                    self.homephone = olderContact.homephone
            else:
                self.homephone = homephone
                if (self.homephone is "x"):
                    del self.homephone

            personalEmail = receiveValue(ValueType.emailValue, "Personal e-mail (" + getattr(olderContact, 'personalEmail', "") + "):", True)
            if not personalEmail:
                if getattr(olderContact, 'personalEmail', None):
                    self.personalEmail = olderContact.personalEmail
            else:
                self.personalEmail = personalEmail
                if (self.personalEmail is "x"):
                    del self.personalEmail

    def __lt__(self, other):
        return super().__lt__(other)

    def Match(self, matchStr):
        return super(FriendContact, self).Match(matchStr)


class ProfessionalContact (Contact):

    def __init__(self, olderContact = None):
        super(ProfessionalContact, self).__init__(olderContact)

    def __str__(self):
        return super(ProfessionalContact, self).__str__()

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
            workphone = receiveValue(ValueType.phoneValue, "Work Phone (" + getattr(olderContact, 'workphone', "") + "):", True)
            if not workphone:
                if getattr(olderContact, 'workphone', None):
                    self.workphone = olderContact.workphone
            else:
                self.workphone = workphone
                if (self.workphone is "x"):
                    del self.workphone

            workEmail = receiveValue(ValueType.emailValue, "Work e-mail (" + getattr(olderContact, 'workEmail', "") + "):", True)
            if not workEmail:
                if getattr(olderContact, 'workEmail', None):
                    self.workEmail = olderContact.workEmail
            else:
                self.workEmail = workEmail
                if (self.workEmail is "x"):
                    del self.workEmail

    def Match(self, matchStr):
        return super(ProfessionalContact, self).Match(matchStr)


class ProfessionalFriendContact (ProfessionalContact, FriendContact):

    def __init__(self, olderContact = None):
        super(ProfessionalFriendContact, self).__init__(olderContact)

    #   This is the 3rd short non-pythonic way to avoid duplications (in the diamond problem)
    #   __str__ in the parent class simply prints all existing attributes in the given object.
    def __str__(self):
        return super(ProfessionalFriendContact, self).__str__()

    def __lt__(self, other):
        return super().__lt__(other)

    def ReadValues(self, olderContact):
        super(ProfessionalFriendContact, self).ReadValues(olderContact)

    def Match(self, matchStr):
        return super(ProfessionalFriendContact, self).Match(matchStr)


#   The function receives values from user, by type of data.
#   The values pass validation.
def receiveValue(typeVal, inputStr, updateExisting = False):
    value = input(inputStr)

    if typeVal == ValueType.phoneValue:
        while not cellPhonePattern.match(value) and value:
            if updateExisting and value is "x":
                return value
            else:
                print(PHONE_ERROR)
                value = input(inputStr)

    elif typeVal == ValueType.emailValue:
        while not eMailPattern.match(value) and value:
            if updateExisting and value is "x":
                return value
            else:
                print(EMAIL_ERROR)
                value = input(inputStr)
    else:
        if not updateExisting:
            while not value:
                print(NAME_ERROR)
                value = input(inputStr)
    return value
