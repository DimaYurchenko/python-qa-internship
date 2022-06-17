from contact_list.view.console import *
from contact_list.models.ContactList import ContactList


class App(object):

    def __init__(self):
        self.contacts = ContactList()
        self.is_running = False

    def run(self):
        self.is_running = True

        while self.is_running:
            action = prompt_action()

            if action == Choice.ADD:
                self.contacts.add(prompt_contact())

            elif action == Choice.FIND:
                key = prompt_search()
                display_search_result(key, self.contacts.find(key))

            elif action == Choice.DELETE:
                self.contacts.delete(prompt_remove())

            elif action == Choice.PRINT_ALL:
                display_all_records(self.contacts.get_all())

            elif action == Choice.EXIT:
                self.is_running = False
