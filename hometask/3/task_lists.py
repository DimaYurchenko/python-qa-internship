# 1. Fill the missing pieces
# Fill the ____ parts of the code below.

# Let's create an empty list
my_list = []

# Let's add some values
my_list.append('Python')
my_list.append('is ok')
my_list.append('sometimes')

# Let's remove 'sometimes'
my_list.remove('sometimes')

# Let's change the second item
my_list[1] = 'is neat'
# Let's verify that it's correct
assert my_list == ['Python', 'is neat']

# 2. Create a new list without modifiying the original one

original = ['I', 'am', 'learning', 'hacking', 'in']
# Your implementation here
modified = original[:]
modified[-2] = 'lists'
modified.append('Python')
assert original == ['I', 'am', 'learning', 'hacking', 'in']
assert modified == ['I', 'am', 'learning', 'lists', 'in', 'Python']

# 3. Create a merged sorted list

list1 = [6, 12, 5]
list2 = [6.2, 0, 14, 1]
list3 = [0.9]
# Your implementation here
my_list =  sorted(list1 + list2 + list3, reverse=True)
assert my_list == [14, 12, 6.2, 6, 5, 1, 0.9, 0]