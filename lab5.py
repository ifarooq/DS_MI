# LAB 5: Tuples in Python.
# 1. Create a tuple my_info which contains your name, age, gender.
# 2. Convert a string to tuple using tuple() function.
# 3. Create a nested tuple and store in in variable t_1.
# 4. In the following tuple:
# a = (1, (1, 2), (1, 2, 3, (1, 2)), 2, 3, 1, (1, 2))
# 1. Find the count of 1 using count method.
# 2. Find the count of (1, 2) using count method.
# 3. Find the index of (1, 2) using index method.

# 1. Create a tuple my_info which contains your name, age, gender.

my_info= ("Imran", 38 , "M")
print(my_info)

# 2. Convert a string to tuple using tuple() function.

tople_my=tuple("Hell World")

print(tople_my)

# 3. Create a nested tuple and store in in variable t_1.
t_1= ('imran','21',(34,23,45))
print (t_1)

# 4. In the following tuple:
# a = (1, (1, 2), (1, 2, 3, (1, 2)), 2, 3, 1, (1, 2))

a = (1, (1, 2), (1, 2, 3, (1, 2)), 2, 3, 1, (1, 2))

# 1. Find the count of 1 using count method.

print(a.count(1))

# 2. Find the count of (1, 2) using count method.
print(a.count((1,2)))

# 3. Find the index of (1, 2) using index method.

print("index of (1,2) ", a.index((1,2)))