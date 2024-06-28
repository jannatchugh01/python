'''
#Here we want to see list of all keywords
import keyword
#keyword module is used to see all keywords in python version
print(keyword.kwlist)
print(len(keyword.kwlist))
value=input("Enter any value from keyboard...")
print(value)
print(type(value)) #OOPS concept--> every type in python is an object of a class
# By default input() function will only accept string value

#typecasting -> changing a datatype to another datatype
# methods -> int(),str(),float()....
value=int(input("Enter a number from keyboard..."))
print(value)
print(type(value))

#Demo for print()


# samplefile here is a file object open for writing
samplefile=open('D:/Coding/python/demo.txt/demo.txt','w')
print(7,8,9,10,sep='%',end='$$',file= samplefile)

#format
#print("Hello all {} people in class".format("10"))
str1=input("Enter number of audience in class")
print("Hello all {} people in class".format(str1))

str1="Hello"
str2="Welcome!"
str3=str1 + str2
print(str3)
# + operator is an overloaded operator that can combine two or more similar type of object

num1=10
print("The num is: ",num1,"The type is: ",type(num1))
num2=10.123
print("The num is: ",num2,"The type is: ",type(num2))
num3=10+5j
print("The num is: ",num3,"The type is: ",type(num3))

#Number System
#Integer base10
#Binary base 2 for using binary numbers -> Prefix 0b or 0B
print(0b101)
print(0B1011)
#octal base 8 -> 0o or 0O
print(0o156)
#Hexadecimal base 16 -> prefix 0x or 0X
print(0xAFB)# 0-9,A-10,B-11.....,F-15

#Typecasting in number is automatic or implicit
#At time we need to force typecasting there it will be explicit

# Implicit Typecasting -> Automatic smaller data will be converted to a bigger datatype

print(100+15.67) # Integer (small data) + Float (big data type) 
# Implicity int will be converted to big datatype 

#forced explicit typecast
#convert a bigger data into smaller data
num1= int(15.77)
print(num1)
val= int(-55.88)
print(val)

#Number based modules -> random and math modules
# Random module -> generate numbers randomly on the fly

import random
print(random.randrange(20,50))
print(random.random())
# Use random to pick a value randomly from any sequence

list1=["hello","bye","Hii","go","y","rt"]
print(random.choice(list1))
random.shuffle(list1)
print(list1)

#Math module

#Mathematical calculation
#Aliases means nick name
import math as mt # mt as alias name for math
print(mt.factorial(5))
print(mt.pi)
print(mt.log10(10000000))
print(mt.pow(2,3))

#Sequence Data -> List,String and tuple
#List -> very flexible sequence of data as it allow all sorts of modification
#[] brackets create list
#Data in list can be of different data types
# Data starts from index position 0
#Characteristics of list -> ordered by position,mutable can be modified,repeated or dupicate
# values are allowed
list1=[1,2,3,"hello","bye",12.77,True,False,'go']
#1 -> at position 0,2 ->position 1,3 -> position 2
# if we access list from left to right then index starts from 0 left---->right
#otherwise from left<------right i.e from backwards then index start from -1
#Access the first element of list
print("first element:",list1[0])
print("second element:",list1[1])
print("last element:",list1[-1])
print("sec last element:",list1[-2])

#Tuples
# Sequence of data having order or positions of elements but it is immutable i.e. we cannot change it
# () -> paranthesis are used to denote tuples
# index starts from 0 left to right and from -1 for right to left
# It may contain any type of data

tup1=(1,2,3,"hello","bye",12.77,True,False,'go')
print("First element :",tup1[0])
print("Second element :",tup1[1])
print("Last element :",tup1[-1])
print("Second last element :",tup1[-2])

list1=[1,2,3,"hello","bye",12.77,True,False,'go']
tup1=(1,2,3,"hello","bye",12.77,True,False,'go')
#Try to modify last element of list from 'go' to 'goNow'
print("Original list =",list1)
list1[-1]="goNow"
print("New list = ",list1)
# Python lists are mutable
tup1[-1] = 100
print(tup1) # Immutability

# Collections type data that do not have any index or position

# Dictionary
# Set'''

# Create a dictionary
# braces brackets
# values are in form of key:value pairs
# Each value is recognised by key
dict1={"Name":"Ajay", "Age":20, "Salary":10000.50}
print(dict1["Age"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1["Age"]=25
print(dict1)

#set
#Used with{}
# Unordered
#no dulpicates element allowed
set1={1,2,3,4,7,7,7,4,3}
print(set1)








