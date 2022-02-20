tup = 'Hello'
print(len(tup))
print(type(tup))

tup = 'Hello',
print(len(tup))
print(type(tup))

# Q: what is going on here? Can you explain the output?
# A: the first 'tup' variable is string, so the len function gives the length of the string, i.e. the number of characters
# A: the second 'tup' variable has a trailing comma hence is a tuple. So the len output is 1 as it's giving the length of the tuple, i.e. one element. 