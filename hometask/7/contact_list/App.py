import sys
from contact_list.view.console import *
from contact_list.models.ContactList import ContactList
from contact_list.serializers.JSON import serialize, deserialize
from pathlib import Path
import atexit


class App(object):

    def __init__(self):

        current_dir = Path(__file__)
        project_dir = [p for p in current_dir.parents if p.parts[-1] == 'python-qa-internship'][0]
        storage_file_path = os.path.join(project_dir, 'storage', 'contacts.json')

        self.contacts = ContactList()
        self.contacts.set_contacts(deserialize(storage_file_path))
        atexit.register(serialize, self.contacts.get_all(), storage_file_path)
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
                sys.exit()
