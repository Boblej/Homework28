class Contact():

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


    def display(self):
        print(f'name: {self.name}, phone: {self.phone}')

class BusinessContact(Contact):

    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company

    def display(self):
        return super().display()
        print(f'Компания: {self.company}')

class PhoneBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contact(self):
        for contact in self.contacts:
            contact.display()

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def delete_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
        else:
            print(f"Контакт с именем {name} не найден")

    def edit_contact(self, name, **kwargs):
        contact = self.search_contact(name)
        if contact:
            for key, value in kwargs.items():
                setattr(contact, key, value)
        else:
            print(f"Контакт с именем {name} не найден")

phone_book = PhoneBook()

contact1 = Contact('artyom', 88005553535)
businesscontact = BusinessContact('dmitry nagiev', 87777777777, 'mtc')
phone_book.add_contact(contact1)
phone_book.add_contact(businesscontact)
phone_book.display_contact()

phone_book.edit_contact('artyom', phone=99999999999)
phone_book.display_contact()

phone_book.delete_contact('dmitry nagiev')
phone_book.display_contact()
