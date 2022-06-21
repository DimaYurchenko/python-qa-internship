from contact_list.models.ContactList import Contact
from typing import List
import json
from json import JSONDecodeError


def serialize(contacts: List[Contact], file_path: str):
    with open(file_path, "w") as f:
        f.write(json.dumps([c.__dict__ for c in contacts]))


def deserialize(file_path: str) -> List[Contact]:
    contacts = []
    data = None

    try:
        with open(file_path, "r") as f:
            data = json.loads(f.read())
    except (FileNotFoundError, JSONDecodeError):
        return contacts

    for entry in data:
        contacts.append(Contact(entry["name"], entry["number"], entry["email"]))

    return contacts
