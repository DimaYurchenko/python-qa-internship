# Write a program that will create a list of people with name, age, height, and weight
# Sort the list of people by age


class Person:
    
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    

person1 = Person('Lucinda', 23, 55, 160)        
person2 = Person('Garland', 27, 83, 190)        
person3 = Person('Antonetta', 43, 75, 173)        
person4 = Person('Cynthia', 19, 62, 167)        
person5 = Person('Rylan', 53, 79, 170)        

unsorted_list = [person1, person2, person3, person4, person5]

assert sorted(unsorted_list, key=lambda p: p.age) == [person4, person1, person2, person3, person5]