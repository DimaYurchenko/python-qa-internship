# Write a Python program to check if two given sets have no elements in common.

x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}

def have_common_elements(a: set, b: set) -> bool:
    return len(a.intersection(b)) != 0

assert have_common_elements(x, y) == True
assert have_common_elements(x, z) == False
assert have_common_elements(y, z) == False

# Write a Python program to remove the intersection of a 2nd set from the 1st set.

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}

result = sn1 - sn2 
assert result == {1, 2, 3}