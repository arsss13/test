import telebot
class PhoneContact():
        def __init__(self, name, contactNumber, note):
            self.name = name
            self.contactNumber = contactNumber
            self.contactNumber = note
        def output_all(self):
            print(self.name, self.contactNumber, self.contactNumber)


    user = PhoneContact(
        name = input ('Введите имя:'),
        contactNumber = input ('Введите контактный номер:'),
        note = input ('Введите записку:')
    )

PhoneContact.output_all(user)

class PhoneBook():
    def create_list_method(self):
        pass
