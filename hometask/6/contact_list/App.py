from .view import console
from .models import ContactList


class App(object):

    def __init__(self):
        self.contacts = ContactList()
        self.is_running = False

    def run(self):
        self.is_running = True

        while self.is_running:
            action = console.prompt_action()

            if action == console.Choice.ADD:
                self.contacts.add(console.prompt_contact())

            elif action == console.Choice.FIND:
                key = console.prompt_search()
                console.display_search_result(key, self.contacts.find(key))

            elif action == console.Choice.DELETE:
                self.contacts.delete(console.prompt_remove())

            elif action == console.Choice.PRINT_ALL:
                console.display_all_records(self.contacts.get_all())

            elif action == console.Choice.EXIT:
                self.is_running = False
