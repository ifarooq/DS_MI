#  Lab 3: Mathematics in Python and Printing
# 1. Create a variable x and assign value of 10. Add 5 to x and store it in another variable and
# display the output of both variables using print() function.
# 2. Assign "Hello" to a variable and print it three times using multiplication operator.
# 3. Check if "Python" is in the following lists
# l = ["C", "C++", "Ruby on Rails", "PHP"]
# a = [4, "Red", "Python", "Tiger"]
# 4. Find Remainder of 9 divided by 3 using modulus operator.
# 5. Create two string variables and concatenate both string using + operator and store it in third
# variable.
# 6. Check if 5 is greater than 3 and 9 divided 3 is 0 is 'True' or 'False'.
# 7. Find quotient of 11 divided 2 using Floor Division. 

x=5
x=x+5
print (x)

str="Hello"   
print(str*3)

l = ["C", "C++", "Ruby on Rails", "PHP"]
a = [4, "Red", "Python", "Tiger"]


if( 'Python' in l):

    print ('Exits in list one')
else:
    print ('not exists in list one')



a = [4, "Red", "Python", "Tiger"]


if( 'Python' in a):

    print ('Exits in list two')
else:
    print ('not exists in list two')


# 4. Find Remainder of 9 divided by 3 using modulus operator.

print (9%3)

# 5. Create two string variables and concatenate both string using + operator and store it in third

# variable.

str1= "stirng 1 "
str2= "string 2 "
str3=str1+str2
print(str3)

# 6. Check if 5 is greater than 3 and 9 divided 3 is 0 is 'True' or 'False'.

if(5>4 and 9/3==0):
    print ('True')
else:
    print('False')

    # 7. Find quotient of 11 divided 2 using Floor Division. 
print(11//2)