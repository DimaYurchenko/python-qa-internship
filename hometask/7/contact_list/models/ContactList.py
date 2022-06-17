from typing import List
from contact_list.models.Contact import Contact


class ContactList(object):

    def __init__(self):
        self.__contacts: List[Contact] = list()

    def add(self, contact: Contact):
        self.__contacts.append(contact)

    def find(self, keyword: str) -> List[Contact]:
        return sorted(
            list(
                filter(
                    lambda contact: keyword in contact.name
                                    or keyword in contact.number
                                    or keyword in contact.email,
                    self.__contacts
                )
            ),
            key=lambda x: x.name
        )

    def delete(self, name: str):
        self.__contacts = list(filter(lambda c: c.name != name, self.__contacts))

    def get_all(self) -> List[Contact]:
        self.__contacts.sort(key=lambda x: x.name)
        return self.__contacts

    def set_contacts(self, contacts: List[Contact]):
        self.__contacts = contacts.copy()
