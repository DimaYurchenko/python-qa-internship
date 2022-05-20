from ContactList import ContactList
from Contact import Contact

def main():
    contacts = ContactList()
    contacts.deserialize()
    running = True
    
    while running:
        print('\n\tChoose what you want to do\n')
        print('''
              1. Add contact
              2. Find contact
              3. Print all
              4. Exit
              ''')
        choise = int(input())
        while choise not in (1, 2, 3, 4):
            choise = int(input('\tNo such option\n'))

        if choise == 1:
            name = input('\tProvide name\n')
            surname = input('\tProvide surname\n')
            phone = input('\tProvide phone number\n')
            
            while not Contact.valid_number(phone):
                phone = input('\tInvalid number, try again\n')

            contacts.add(Contact(name, surname, phone))

        elif choise == 2:
            name = input('\tProvide name of the contact\n')
            res = contacts.find(name)

            if res:
                print(f'\t{len(res)} mathing names found:\n')
                print(*res, sep='\n')
            else:
                print('\tNo contacts with such name\n')

        elif choise == 3:
            cons = contacts.get_all()
            if cons:
                print(f'\tYou have {len(cons)} contacts in yout list:\n')
                print(*cons, sep='\n')
            else:
                print('\tContact list is empty\n')
            
        elif choise == 4:
            running = False
            print('\tExiting\n')

        
    if contacts.get_all():
        contacts.serialize()

if __name__ == '__main__':
    main()