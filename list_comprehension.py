# This file is used as a refernce for list comprehenstion

# Append each chcarcter in a string to a list
print([letter for letter in "word"])

# Return the multiples of 2 to 20
print([x*2 for x in range(1, 11)])

# Generate a list contating integers devisible by 10 from 1 to 100
print([x for x in range(1, 101) if x % 10 == 0])