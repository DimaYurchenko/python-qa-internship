import json
from typing import List
from Contact import Contact

class ContactList:
    
    def __init__(self) -> None:
        self.__contacts = list()

    def add(self, contact: Contact):
        self.__contacts.append(contact)
        
    def find(self, name: str) -> List[Contact]:
        return list(
            filter(
                lambda contact: name in contact.name+contact.surname,
                   self.__contacts)
        )

    def get_all(self) -> List[Contact]:
        return self.__contacts.copy()

    def serialize(self):
        with open('numbers.json', 'w') as output:
            res = json.dumps([number.dump() for number in self.__contacts])
            output.write(res)

    def deserialize(self):
        try:
           with open('numbers.json', 'r') as input:
            try:
               json_nums = json.loads(input.read()) 
            except:
                return

            for contact in json_nums:
                name = contact['Contact']['name']
                surname = contact['Contact']['surname']
                number = contact['Contact']['number']

                self.add(Contact(name, surname, number))
        except:
            return
 


