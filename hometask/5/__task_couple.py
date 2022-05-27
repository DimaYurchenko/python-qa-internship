# Write a program that will find a couple.
# On the start program have to create a list of 10 random people male and female.
# Every person have three fields name, age, sex
# Program asks a user to enter a name and a desired age for search
# Matching rule
# Couple can match if users age difference not more than 5 years and both names has at least same two letters
# If match is found program should print - Congrats there is a matching pair Name1 + Name2!
# It no match - just print Sorry, no match! =(

#TODO: add Faker to reqs

from faker import Faker
from enum import Enum
import random

class Person:
    
    class Sex(Enum):
        MALE = 0
        FEMALE = 1
        
    def __init__(self, name: str, age: int, sex: Sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return f'{self.name} {self.age} {self.sex._name_}'

    def __repr__(self) -> str:
        return f'{self.name} {self.age} {self.sex._name_}'

def generate_people(ammount: int):
    i = 0
    fake = Faker()
    
    while i < ammount:
        sex = random.choice(list(Person.Sex))
        name = fake.name_male() if sex == Person.Sex.MALE else fake.name_female()
        age = random.randint(18, 45)

        yield Person(name, age, sex)
        i += 1
        
def match(p1: Person, p2: Person) -> bool:
    return (abs(p1.age - p2.age) <= 5 and 
            len(set(p1.name).intersection(p2.name)) >= 2 and
            p1.sex != p2.sex) #a really conservative line of code

def main():
    people = list(generate_people(10))
    print('Available people:\n')
    print(*people, sep='\n', end='\n\n')

    user_name = input('What is your name?\n')
    user_age = int(input('What is your desired age?\n'))
    user_sex_choise = input('What is your sex? m/f\n')

    while user_sex_choise.lower() not in ('m', 'f'):
        user_sex_choise = input('What is your sex? m/f\n')
    
    user_sex = Person.Sex.MALE if user_sex_choise == 'm' else Person.Sex.FEMALE

    user = Person(user_name, user_age, user_sex)
    match_found = False

    for person in people:
        if match(user, person):
            match_found = True
            print(f'Congrats there is a matching pair:\n{user} and {person}\n')

    if not match_found:
        print('Sorry, there is no match')


if __name__ == '__main__':
    main()