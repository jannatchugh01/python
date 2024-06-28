# Lambda functions
# Anonymous functions: small user-defined function codes that do not have a name
# you do not use def keyword to create a lambda function
# rather we use lambda keyword and colon: operator

# Syntax
'''
variable= lambda argument(s) : expression statement or calculations
# to call a lambda function
variable()
'''

# use lambda function for printing a message

'''message= lambda : print("Hello user!! First message!!")

# calling a lambda function
message()

# use arguments in lambda
message= lambda username : print(f"Hello user {username} !! First message!!")

# calling a lambda function
username=input("Enter username: ")
message(username)

# join lambda functions with map() and filter() method

# from a list of numbers we want to filter out only odd numbers and create a new list

list1=[1,2,3,4,56,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# syntax for filter method -> filter(any function to be used as filter ex.lambda, iterable)
odd_list= list(filter(lambda num: (num%2!=0),list1))
print("The new odd list created: ",odd_list)

result= lambda num1,num2 : num1 if (num1>num2) else num2

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
print("The maximum number is: ",result(num1,num2))

# Check for age>=60 in alist and filter out those employees in seperate list
age_list=[23,45,67,89,24,77,89,79,74,80]
seniorAge_list= list(filter(lambda age: (age>=60),age_list))
print("Senior age list:",seniorAge_list)

# map() -> helps to apply a lambda function's calculation mapped to each element of iterable
# map(lambda...,iterable)
list_salary=[1000,5000,15000,2000,6500,8900,3600]

bonus_list=list(map(lambda sal:(sal+500),list_salary))
print("The bonus list of employees: ",bonus_list)

name_list=['jannat','mona','sona','kitu']
upper_list=list(map(lambda name:(name.upper()),name_list))
print("The names of employee: ",upper_list)


# file: A storage space where you can save data on permanent basis
# how data can be persisted in python? -> File handling
# Types -> .csv(comma delimited file), .xls or .xlsxfile(Excel), .json(object file)
# .csv files
# 2 ways of working with csv file:
# 1. csv module
# 2. pandas module

# csv module
import csv
# Create a simple file and use it for writing
# a file can have in general two mode -> 'w' for writing and 'r' for reading

with open('firstFile.csv','w',newline='')as file:
    writer =csv.writer(file)
    writer.writerow(["EmpID","EmpName","Salary","Department"])
    writer.writerow([100,"Aman",10000,"Mkt"])
    writer.writerow([101,"Pooja",12000,"Prod"])
    writer.writerow([102,"Reena",15000,"Mkt"])
    writer.writerow([103,"Mann",16000,"Prod"])

import csv
data_list=[
    ["EmpID","EmpName","Salary","Department"],
    [100,"Aman",10000,"Mkt"],
    [101,"Pooja",12000,"Prod"],
    [102,"Reena",15000,"Mkt"],
    [103,"Mann",16000,"Prod"]
]
with open('fivefile.csv','w',newline='')as file:
    writer=csv.writer(file,delimiter=';',quotechar='"',quoting=csv.QUOTE_ALL)
    writer.writerows(data_list)'''

'''import csv
with open("file.csv",'r') as file:
    reader=csv.reader(file,skipinitialspace=True)
    for row in reader:
        print(row)'''

import csv
data_list=[
    ["EmpID","EmpName","Salary","Department"],
    [100,"Aman",10000,"Mkt"],
    [101,"Pooja",12000,"Prod"],
    [102,"Reena",15000,"Mkt"],
    [103,"Mann",16000,"Prod"]
]
with open('fivefile.csv','a',newline='')as file:
    writer=csv.writer(file,delimiter=';',quotechar='"',quoting=csv.QUOTE_ALL)
    writer.writerows(data_list)

