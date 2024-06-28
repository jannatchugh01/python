'''#single line string
str1='Hello Welcome to session 3'
print(str1)
str2="Hello welcome to session 3"
print(str2)
#Multiline strings
#str3=''Hello WELCOME to my lecture''
#print(str3)

# Slicing syntax
# str[start_index_pos : end_index_pos : number_of_moves or jumps]
#slicing is from left to right
#strings are immutable ->no modification allowed in string character
str4= "Hello all"
print(str4[0:5])
print(str4[::-1]) # reverses the string
str="hello all"
print(str[1:7:1])
print(str[:5:2]) #hlo
# negative slicing
print(str[-5:-1])
print(str[-9:-2:2])

#String comparison

# >,<,== -> to check for equality

str1="hello"
str2="Hello"
print(str1==str2)
print(str1 > str2)
print(str1 < str2)

#Ascii codes
#A-Z = 65 to 90
# a-z = 97-122
# ord() -> gives ascii codes for character
# chr() -> gives corresponding characters for a given ascii code 

print(ord('H'))
print(ord('h'))
print(chr(65))
print(chr(97))

#String repeatation

# * operator to repeat strings multiple times

str1="Hello "
print(str1*2) #repeat str1 2 times

# Concatenation operator +

str1="Hello"
str2=" "
str3="all"
print(str1+str2+str3)

# find length or number of character in a string
print("Number of characters in string are: ",len(str1))

# Test if a particular character or sub-string is present inside string or not
# Membership test

str1="Hello dear friends, welcome to my class..."
# membership test is done by 'in' or 'not in' operator

print('friend' in str1)
print(','in str1)
print('....'not in str1)

#String methods
str1="hello all"
# To convert to upper case
print(str1.upper())
print(str1)
print(str1.lower())

# Replace a particular sub-string inside a string to create a new string

str1="Hello all students welcome here"
new_string= str1.replace('all','all the')
print("Original string: ",str1)
print("New string: ",new_string)

# How to find if a particular sub-str is present or not
# find() -> returns the starting index of sub-string if present else if the substring
# is not present then returns -1

print(str1.find('people'))
print(str1.find('students'))

#index() -> finds the index of substring. If the substring is absent then it will raise error

print(str1.index('students'))
print(str1.index('student in class'))
'''
# To slice or split or cut the string
#split()
str1="Hello all, students welcome, here"
print(str1.split()) # splits using seperator and default sep is ' '
print(str1.split(','))
print(str1.split(',',1))# To restrict 1 time spliting
# Syntax: split(seprator'',Max_number of splits)

#strip()
# To remove spaces from text string specific leading and trailing
str1="            HELLO           all,students   welcome,here               "
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())


