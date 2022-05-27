import phonenumbers

class Contact:

    def __init__(self, 
                 name: str,
                 surname: str,
                 number: str
                 ) -> None:

        self.__name = name
        self.__surname = surname
        self.__number = number
        
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, new_number: str):
        if not Contact.valid_number(new_number):
            raise ValueError('Invalid phone number')
        self.__number = new_number
    
    @staticmethod
    def valid_number(number: str) -> bool:
        try:
            num = phonenumbers.parse(number)
            return phonenumbers.is_valid_number(num)
        except:
            return False
    
    def __str__(self) -> str:
        return f'{self.__name} {self.__surname}: {self.__number}'

    def __repr__(self) -> str:
        return f'{self.__name} {self.__surname}: {self.__number}'

    def dump(self):
        return {"Contact": {'name': self.__name,
                            'surname': self.__surname,
                            'number': self.__number}}
