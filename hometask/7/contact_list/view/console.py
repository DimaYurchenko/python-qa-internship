from typing import List
from enum import Enum
import os
from contact_list.validation.validators import valid_phone_number, valid_email, valid_name
from contact_list.models.Contact import Contact
from tabulate import tabulate


class Choice(Enum):
    ADD = 1
    FIND = 2
    DELETE = 3
    PRINT_ALL = 4
    EXIT = 5


def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')


def prepare_list(lst: List[Contact]):
    table = [[c.name, c.number, c.email] for c in lst]
    return tabulate(table, headers=['Name', 'Number', 'Email'])


def prompt_action() -> Choice:
    
    print('\n\tChoose what you want to do\n')
    print('''
                 1. Add contact
                 2. Find contact
                 3. Delete contact
                 4. Print all
                 5. Exit
                 ''')
    
    choice = int(input())
    while choice not in (1, 2, 3, 4, 5):
        choice = int(input('\tNo such option\n'))

    return Choice(choice)


def prompt_contact() -> Contact:
    name = None
    while name is None:
        try:
            inp = input('\tProvide name\n')
            valid_name(inp)
            name = inp
        except ValueError as e:
            print(str(e))

    number = input('\tProvide phone number\n')
    while not valid_phone_number(number):

        number = input('\tInvalid phone number, try again\n')

    email = input('\tProvide email\n')
    while not valid_email(email):
        email = input('\tInvalid email, try again\n')

    return Contact(name, number, email)


def prompt_search() -> str:
    return input('\tProvide name, email or phone number\n')


def prompt_remove() -> str:
    return input('Provide a name of contact you wish to be removed')


def display_search_result(search_key: str, occurrences: List[Contact]):
    if not occurrences:
        print('\tNo results found\n')
        return

    print(f'\t{len(occurrences)} matching records:\n')
    print(prepare_list(occurrences))


def display_all_records(contacts: List[Contact]):
    if not contacts:
        print('\tYour contact book is empty\n')
        return

    print(f'\tYou have {len(contacts)} records:\n')
    print(prepare_list(contacts))






