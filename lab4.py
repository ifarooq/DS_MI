# LAB 4: Lists in Python
# 1. Create a list of characters from a string which is stored in variable.
# 2. Create list of words stored in the following variable.
# s = "Earth is Round"
# 3. Find the length of list by using len() function.
# list_1 = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g',
# ['hh', 'ii'], 'j']
# 4. From the above list_1 remove the second item in list.
# 5. Add "hh" to the end of list_1 and store in list_3. Also print list_3.
# 6. Remove 'a' from list_1 and print the result

# 1. Create a list of characters from a string which is stored in variable.

str= 'Hello World'
list_of_char=list(str)

print(list_of_char)

# 2. Create list of words stored in the following variable.
# s = "Earth is Round"

s = "Earth is Round"
list_of_words=s.split()

print(list_of_words)


# 3. Find the length of list by using len() function.
# list_1 = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g',
# ['hh', 'ii'], 'j']

list_1 = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']

print(len(list_1)) #returns 5

# 4. From the above list_1 remove the second item in list.

del(list_1[1])
print(list_1)

# 5. Add "hh" to the end of list_1 and store in list_3. Also print list_3.

list_1.append('hh')
list_3=list_1
print(list_3)

# 6. Remove 'a' from list_1 and print the result

list_1.remove('a')
print(list_1)