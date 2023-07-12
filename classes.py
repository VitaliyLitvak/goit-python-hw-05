from collections import UserDict


class Record:
    def __init__(self, name, phones=None):
        self.name = name
        self.phones = phones if phones is not None else []
    
    def add_phone(self, phone):
        self.phones.append(phone)
                   
    def delete_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != str(phone)]
        
    def change_phone(self, old_phone, new_phone):
        index = [str(phone) for phone in self.phones].index(str(old_phone))
        self.phones[index] = new_phone

        
    def __str__(self):
        return f"{self.phones}"
    
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
    def __init__(self, value):
        self.name = value
        super().__init__(value=value)


class Phone(Field):
    def __init__(self, value=''):
        self.phone = value
        super().__init__(value=value)
        
        
                  
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def update_record(self, record):
        self.data[record.name.value].phones.extend(record.phones)
