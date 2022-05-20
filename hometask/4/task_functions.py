# 1. Fill the missing pieces of the count_even_numbers function
# Fill ____ pieces of the count_even_numbers implemention in order to pass the assertions. You can assume that numbers argument is a list of integers.

from operator import le


def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1 
    return count

assert count_even_numbers([1, 2, 3, 4, 5, 6]) == 3
assert count_even_numbers([1, 3, 5, 7]) == 0
assert count_even_numbers([-2, 2, -10, 8]) == 4

# 2. Searching for wanted people
# Implement find_wanted_people function which takes a list of names (strings) as argument. The function should return a list of names which are present both in WANTED_PEOPLE and in the name list given as argument to the function.

WANTED_PEOPLE = ['John Doe', 'Clint Eastwood', 'Chuck Norris']
# Your implementation here
def find_wanted_people(people):
    return list(set(WANTED_PEOPLE).intersection(people))
    
people_to_check1 = ['Donald Duck', 'Clint Eastwood', 'John Doe', 'Barack Obama']
wanted1 = find_wanted_people(people_to_check1)
assert len(wanted1) == 2
assert 'John Doe' in wanted1
assert 'Clint Eastwood'in wanted1

people_to_check2 = ['Donald Duck', 'Mickey Mouse', 'Zorro', 'Superman', 'Robin Hood']
wanted2 = find_wanted_people(people_to_check2)
assert wanted2 == []

# 3. Counting average length of words in a sentence
# Create a function average_length_of_words which takes a string as an argument and returns the average length of the words in the string. You can assume that there is a single space between each word and that the input does not have punctuation. The result should be rounded to one decimal place (hint: see round).
def average_length_of_words(string):
    if len(string) == 0:
        return 0
    words = string.split()
    return round(sum([len(word) for word in words]) / len(words), 1)
    
    
# Your implementation here
assert average_length_of_words('only four lett erwo rdss') == 4
assert average_length_of_words('one two three') == 3.7
assert average_length_of_words('one two three four') == 3.8
assert average_length_of_words('') == 0