from classes import Record, Field, Name, Phone, AddressBook
import re


STOP_LIST = ("good bye", "close", "exit")
address_book = AddressBook()


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


@input_error
def handle_add(user_input):
    user_input = user_input.split(" ")
    name = Name(user_input[1])
    phones = Phone(user_input[2:])
    record = Record(name, phones)
    if str(name) not in address_book.data.keys():
        address_book.add_record(record)
    else:
        record = Record(name, address_book.data[str(record.name)])
        record.add_phone(phones)
        address_book.add_record(record)
    return f"Контакт {name} був збережений з номером телефону {phones}.\n"


@input_error
def handle_change(user_input):
    matches = re.match(r'\w+\s+(\D+)\s([+]?\d{7,15})\s([+]?\d{7,15})', user_input)
    name, old_phone, new_phone = Name(matches.group(1)), Phone(matches.group(2)), Phone(matches.group(3))
    if str(name) in address_book.data.keys():
        record = Record(name, address_book.data[str(name)])
        record.change_phone(old_phone, new_phone)
        address_book.add_record(record)
        return f"Контакт {name} був змінений. Новий номер телефону {new_phone}.\n"
    else:
        raise KeyError
 
    
@input_error
def handle_delete(user_input):
    name, phone = user_input_split(user_input)
    if str(name) in address_book.data.keys():
        record = Record(name, address_book[str(name)])
        record.delete_phone(phone)
        if record.phone:
            address_book.add_record(record)
        else:
            del address_book.data[str(name)]
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