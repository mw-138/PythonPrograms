import json
import os


class Contact:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number


class ContactEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class ContactBook:
    def __init__(self):
        self.contacts = []
        self.file_name = "output/contact_book.txt"

    def __does_file_exist(self):
        return os.path.exists(self.file_name)

    def __encode_contact(self, contact):
        return json.dumps(contact, cls=ContactEncoder)

    def __decode_contact(self, contact) -> Contact:
        j = json.loads(contact)
        return Contact(**j)

    def __load(self):
        if self.__does_file_exist():
            with open(self.file_name, "r") as file:
                for line in file:
                    json_obj = line[:-1]
                    contact = self.__decode_contact(json_obj)
                    self.contacts.append(contact)
        else:
            self.__save()

    def __save(self):
        file_action = "w" if self.__does_file_exist() else "x"
        with open(self.file_name, file_action) as file:
            for contact in self.contacts:
                file.write(f"{self.__encode_contact(contact)}\n")

    def __add_contact(self, contact):
        self.contacts.append(contact)
        self.__save()

    def __remove_contact(self, index):
        self.contacts.pop(index)
        self.__save()

    def __list_contacts(self):
        contact_index = 0
        for contact in self.contacts:
            print("=" * 30)
            print(f""
                  f"Index: {contact_index}\n"
                  f"Name: {contact.first_name} {contact.last_name}\n"
                  f"Phone Number: {contact.phone_number}"
                  f"")
            print("=" * 30)
            contact_index += 1

    def start(self):
        self.__load()
        while True:
            user_input = input("Input action ('list', 'add', 'remove'): ")

            if user_input == "list":
                self.__list_contacts()
            elif user_input == "add":
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                phone_number = int(input("Enter phone number: "))
                self.__add_contact(Contact(first_name, last_name, phone_number))
            elif user_input == "remove":
                index = int(input("Enter index: "))
                self.__remove_contact(index)
            else:
                print("Invalid action")
