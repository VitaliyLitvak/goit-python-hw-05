from collections import UserDict
import re

STOP_LIST = ("good bye", "close", "exit")


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдений."
        except (IndexError, AttributeError):
            return "Не вірна команда."
        except ValueError:
            return "Введені данні некоректні."
    return inner
          

class Record:
    def __init__(self, name, phone=''):
        self.name = str(name)
        self.phone = str(phone)
    
    def add_phone(self, phone):
        self.phone += str(f'{phone}')
    
    def delete_phone(self, phone):
        self.phone = self.phone.replace(str(phone), '').rstrip()
        
    def edit_phone(self, old_phone, new_phone):
        self.phone = self.phone.replace(str(old_phone), str(new_phone))

    def __str__(self):
        return f"{self.name}:{self.phone}"
    
    def __repr__(self):
        return str(self)
        
class Field:
    def __init__(self, value=None):
        self.value = value
        
    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value=None):
        self.name = value
        super().__init__(value=value)


class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value=value)
        
                  
class AddressBook(UserDict):
    def add_record(self, record):
        key, value = str(record).split(":")
        if key not in self.data.keys():
            self.data[key] = value
        elif value not in self.data[key]:
            self.data[key] += f' {value}'
            
    def update_record(self, record):
        key, value = str(record).split(":")
        self.data[key] = value
        


address_book = AddressBook()   

def user_input_split(user_input):
    matches = re.match(r'\w+\s+(\D+)\s([+]?\d{7,15})', user_input)
    if matches:
        name = Name(matches.group(1))
        phone = Phone(matches.group(2))
        return name, phone
    else:
        return "Данні відсутні."
    

def handle_hello():
    return "How can I help you?"


input_error    
def handle_add(user_input):
    name, phone = user_input_split(user_input)
    record = Record(name, phone)
    address_book.add_record(record)
    return f"Контакт {name} був збережений з номером телефону {phone}.\n"


@input_error
def handle_change(user_input):
    matches = re.match(r'\w+\s+(\D+)\s([+]?\d{7,15})\s([+]?\d{7,15})', user_input)
    name, old_phone, new_phone = matches.group(1), matches.group(2), matches.group(3)
    if name in address_book.data.keys():
        record = Record(name, address_book.data[name])
        record.edit_phone(old_phone, new_phone)
        print(record)
        address_book.update_record(record)
        return f"Контакт {name} був змінений. Новий номер телефону {new_phone}.\n"
    else:
        raise KeyError
 
    
@input_error
def handle_delete(user_input):
    name, phone = user_input_split(user_input)
    name = str(name)
    phone = str(phone)
    if name in address_book.data.keys():
        record = Record(name, address_book[str(name)])
        record.delete_phone(phone)
        address_book.update_record(record)  
        return f"Контакт {name} був змінений. Номер телефону {phone} видалений.\n"
    else:
        return f"У контакта {name} номер телефона {phone} не знайдений.\n"

    
@input_error    
def handle_phone(user_input):
    name = re.match(r'\w+\s+(\D+)', user_input).group(1)
    if name in address_book.data.keys():
        return f"Контакт {name}: {address_book.data[name]}\n"
    else:
        raise KeyError

    
def handle_showall():
    if not address_book.data:
        return "Книга контактів порожня"
    else:
        return address_book.data


def commands(user_input):
        if user_input.lower() == "hello":
            response = handle_hello()
        elif re.search(r"^add ", user_input, re.IGNORECASE):
            response = handle_add(user_input)
        elif re.search(r"^change ", user_input, re.IGNORECASE):
            response = handle_change(user_input)
        elif re.search(r"^delete ", user_input, re.IGNORECASE):
            response = handle_delete(user_input)    
        elif re.search(r"^phone ", user_input, re.IGNORECASE):
            response = handle_phone(user_input)
        elif user_input.lower() == "show all":
            response = handle_showall() 
        else:
            response = "Не вірна команда."
        print(response)    


def main():
    while True:
        user_input = input("Введіть будь-ласка команду: ")
        if user_input in STOP_LIST:
            print("Good bye!")
            break
        else:
            commands(user_input)

      
if __name__ == "__main__":
        main()