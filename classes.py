from collections import UserDict


class Record:
    def __init__(self, name, phone=''):
        self.name = name
        self.phone = phone
    
    def add_phone(self, phones):
        if isinstance(self.phone, str):
            self.phone += f"{phones}"
        elif isinstance(self.phone.phone, Record):
            self.phone = self.phone.phone.phone + [p for p in phones.value]
        elif isinstance(self.phone.phone, Phone):
            self.phone = self.phone.phone.value + [p for p in phones.value]
        elif isinstance(self.phone.phone, list):
            self.phone = self.phone.phone + [p for p in phones.value]
            
    def delete_phone(self, phone):
        if isinstance(self.phone.phone, Record):
            self.phone = [p for p in self.phone.phone.phone if p != phone.value]
        elif isinstance(self.phone.phone, Phone):
            self.phone = [p for p in self.phone.phone.value if p != phone.value]
        elif isinstance(self.phone.phone, list):
            self.phone = [p for p in self.phone.phone if p != phone.value]
        
    def change_phone(self, old_phone, new_phone):
        if isinstance(self.phone, str):
            self.phone.replace(old_phone.phone, new_phone.phone)
        if isinstance(self.phone.phone, Record):
            index = self.phone.phone.value.index(old_phone.phone)
            self.phone.phone.value[index] = new_phone.phone
        elif isinstance(self.phone.phone, Phone):
            index = self.phone.phone.value.index(old_phone.phone)
            self.phone.phone.value[index] = new_phone.phone
        elif isinstance(self.phone.phone, list):
            index = self.phone.phone.index(old_phone.phone)
            self.phone.phone[index] = new_phone.phone

    def __str__(self):
        return f"{self.phone}"
    
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
    def __init__(self, value=None):
        self.phone = value
        super().__init__(value=value)
        
        
                  
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
