'''# Create a simple list
list1=[1,2,3,4,"abc","hello",True,False,11.89,4+5j]
print("the list is :",list1)

# Create ablank list
list2=[] #Empty list
print(list2)

#List here in python is also a class. A list object can be also instantiate constructor by invoking list()

str1="Hello All!!"
#to convery this string directly to list we can invoke list()
New_list=list(str1)
print("The newly formed list is : ",New_list)

# Properties of List:
# 1. Ordered
# 2. Mutable
# 3. Allows repeated values i.e. duplicates

# 1. Ordered
#Each element of list has an index position attached
list1=[1,2,3,4,"abc","hello",True,False,11.89,4+5j]
# Start access from left to right
print("First element: ",list1[0])
print("Second element: ",list1[1])
print("Fifth element: ",list1[4])
print("last element: ",list1[-1])
print("second last element: ",list1[-2])

# Slice and negative slice a list
print("Slice from index 1 to 6: ",list1[1:7])
print("Negative slice from last position to second element:",list1[1:-1])
print("Negative slice from second last position to second element:",list1[-10:-1])
print("reverse of list :",list1[::-1])

# 2. Mutable

list1=[1,2,3,"Hello","Bye",3+7j,11.4]
print("Original list :",list1)
# To add a element at the end of list append()
list1.append("New Value")
print("The appended list: ",list1)
#To add new element at a specific position in list insert()
list1.insert(3,20)
print("Updated list: ",list1)

# You can add a new value from another list into original list extend()

list1=[1,2,3,"Hello","Bye",3+7j,11.4]
print("Original list: ",list1)
list2=[7,8,9,"hi"]
list1.extend(list2)
print("Updated list: ",list1)
print("list 2 values: ",list2)
print("List concatenation : ",list1+list2)
# List repeatition
list1=[1,2,3,"Hello","Bye",3+7j,11.4]
print("List repeat: ",list1*3)

# Operators common for sequences: +,*,[ : ]

#Make modifications in list
# We can change a particular list element 
list1=[1,2,3,"Hello","Bye",3+7j,11.4]
print("Original list: ",list1)
# update the third element of list 
list1[2]=30
print("Updated list : ",list1)
list1[2:5]=[30,"hello","bye all"]
print("Updated list: ",list1)
list1[2:5]=[30,"hello","bye all",11]
print("Updated list : ",list1)

#Remove elements from list
list1=[1,2,3,"Hello","Bye",3+7j,11.4,"Hello","Hello"]
print("Original list: ",list1)
# Remove a particular element of value "Hello"
# remove()
list1.remove("Hello")
print("Updated list : ",list1)
list1.remove("Hello")
print("Updated list : ",list1)
list1.remove("Hello")
print("Updated list : ",list1)

#Count occurence of elements
list1=[1,2,3,"Hello","Bye",3+7j,11.4,"Hello","Hello"]
print("The count of occurence of'Hello': ",list1.count("Hello"))

#Sort a list
list1=[3,6,9,7,8,10,77,88,1,10,10]
list1.sort() # sorting in ascending order
print("The sorted list: ",list1)
#Sort in descending or reverse order
list1.sort(reverse=True)
print("Reverse sorted list: ",list1)

# Create a copy of list using copy()
list1=[1,2,3,"Hello","Bye",3+7j,11.4,"Hello","Hello"]
print("Original list: ",list1)
new_list=list1.copy()
print("THE new list: ",new_list)
#To check if both are equal or not
print(list1==new_list)

#Tuple
# Create a tuple
tup1=(1,2,3,"Hello","Bye",11.3)
print("The original tuple: ",tup1)
#We have a tuple constructor tuple()
new_tuple=tuple(('Hello','Bye',1,2,3,'Go',22.5))
print("New tuple: ",new_tuple)
list1=['Hello','Bye',4,5]
new_tuple=tuple(list1)
print("New tuple: ",new_tuple)
# we can make a list from tuple and a tuple from string

# Empty or blank tuple
tup1=()
print("The tup1 is: ",tup1,"Type of tup1: ",type(tup1))

#Create a tuple with only single value
#Singleton tuples
tup1=("Hello")
print("The tup1 is: ",tup1,"Type of tup1: ",type(tup1))# type=str
tup1=(24)
print("The tup1 is: ",tup1,"Type of tup1: ",type(tup1))#type=int
tup1=("Hello",)
print("The tup1 is: ",tup1,"Type of tup1: ",type(tup1))#type=tuple

#Default structure
values=1,5,8,'hello','bye'
print("The values are: ",values,"Types of values: ",type(values))

#Properties of tuple
# 1. Ordered
# 2. Immutable
# 3. Allows duplicate values

# 1. Ordered
tup1=(1,2,3,"Hello","Bye",11.3)
print("The original tuple: ",tup1)
print("First element: ",tup1[0])
print("Second element: ",tup1[1])
print("Second last element: ",tup1[-2])
print("Last element: ",tup1[-1])
print("Slice of element[1:6]: ",tup1[1:6])
print("Slice of element with 2 jumps: ",tup1[0:6:2])
print("negative slice of element: ",tup1[-6:])
print("reverse of element: ",tup1[::-1])

# 2.Immutable
list1=[1,2,3,"Hello","Bye",11.3]
print("Original list: ",list1)
tup1=(1,2,3,"Hello","Bye",11.3)
print("Original tuple: ",tup1)
#Try to modify 3-->30 in both list1 and tup1
list1[2]=30
#tup1[2]=30
print("Updated list: ",list1)
print("Updated tuple: ",tup1)
# To find length of tuple
print("The length of tuple: ",len(tup1))
#Check for membership in tuple in and not in
print('"Hello" in tup1',"Hello"in tup1)
print('"hello" not in tup1',"hello"not in tup1)

#No direct removal of element allowed in tuple
# However you can remove entire tuple in one go
# del property
del tup1
print(tup1)

# Two method in tuple:
# 1. count(): count the number of times of element
# 2. index():search and find index of element or throughtup1=(1,2,3,"Hello","Bye",11.3)
tup1=(1,2,3,"Hello","Bye",11.3,"Hello")
print("The original tuple: ",tup1)
print("Count of Hello: ",tup1.count("Hello"))
print("Find if Hello is present: ",tup1.index("Hello"))

#SET 
#1. Set begin with{} braces
#2. It does not allow duplicates
#3. constructor call set()
#4.Unordered

set1={1,2,3,'Hello','Bye',True,33.4,1,2,3,4,2,}
print(set1)

#Empty set using set()
set2=set()
print("Empty set is: ",set2,"Type of set is: ",type(set2))# type is set
set3={}
print("Empty set is: ",set3,"Type of set is: ",type(set3)) # type is dict

# Set is mutable
# To add new element in set use add()
set1={1,2,3,5,7,33.4,1,2,3,4,2,}
print("Original set: ",set1)
set1.add(55)
print("Updated set: ",set1)

#Update() -> to add elements from another list of tuple in a set

set1={1,2,3,4,5,6,7,8,9}
print("Original set: ",set1)
list1=[10,11,12,13,14,3]
set1.update(list1)
print("Updated set: ",set1)
tup1=(333,555,678)
set1.update(tup1)
print("Updated set: ",set1)
set2={890,4444}
set1.update(set2)
print("Updated set: ",set1)

#Remove values from set
# remove() removes a particular value from set
#discard() does not show error
set1={1,2,3,4,5,6,7,8,9,5}
print("Original set: ",set1)
set1.remove(5)
print("Updated set: ",set1)
set1.discard(5)
print("Updated set: ",set1)
set1.discard(5)
print("Updated set: ",set1)
set1.discard(5)
print("Updated set: ",set1)

#Built in methods
# all() -> checks for the true set of boolean values(AND Gate)

set1={True,True,True,1,1}
res=all(set1)
print("The result is: ",res)
list1=[True,True,True,1,1]
res=all(list1)
print("The result is: ",res)

# any() -> it return True if atleast 1 value in an iterable is True(OR Gate)
set1={1,1,0}
res=any(set1)
print("The result is: ",res)

#len() method to check for length of a set
set1={2,7,8,1,1}
res=len(set1)
print("The result is: ",res)

# max() and min()
set1={4,66,89,49,73,1,1}
res=max(set1)
print("The result is: ",res)
set1={4,66,89,49,73,1,1,-6}
res=min(set1)
print("The result is: ",res)

# sum()
set1={4,66,89,49,73,1,1}
res=sum(set1)
print("The sum result is: ",res)

# Mathematical operations
# Union,Intersection, symmetric difference, subtraction
# Union -> combines unique element from setA and B
# union() and |

set1={4,66,89,49,73,1,1}
set2={3,6,8,9,4}
print("The union of set1 and set2..........")
print("using union(): ",set1.union(set2))
print("using | operator : ",set1 | set2)

# Intersection : takes only common elements present in both set
# intersection() and & operator
set1={4,66,89,49,73,1,1}
set2={3,6,8,9,4}
print("The intersection of set1 and set2..........")
print("using intersection(): ",set1.intersection(set2))
print("using & operator : ",set1 & set2)

# difference() A-B: The elements of A subtraction tne common element of B
# The result must contain those elements of A  which are not present in B
# difference() and - operator

set1={4,66,89,49,73,1,1}
set2={3,6,8,9,4}
print("The difference of set1 and set2..........")
print("using difference(): ",set1.difference(set2))
print("using - operator : ",set1 - set2)

# In-place update set operations
# intersection_update(), union_update(), difference_update()

set1={4,66,89,49,73,1,1}
set2={3,6,8,9,4}
print("Original set1: ",set1)
print("Original set2: ",set2)
set1.intersection_update(set2)
print("The updated set1: ", set1)
print("The updated set2: ",set2)

#...........difference_update......
set1={4,66,89,49,73,1,1}
set2={3,6,8,9,4}
print("Original set1: ",set1)
print("Original set2: ",set2)
set1.difference_update(set2)
print("The updated set1: ", set1)
print("The updated set2: ",set2)

# update()
set1={4,66,89,49,73,1,1}
set2={3,6,8,9,4}
print("Original set1: ",set1)
print("Original set2: ",set2)
set1.update(set2)
print("The updated set1: ", set1)
print("The updated set2: ",set2)

# Symmetric_difference()
#This method return all the values present in given set data structures except
# The common values between them
set1={4,66,89,49,73,1,1}
set2={3,6,8,9,4}
print("Original set1: ",set1)
print("Original set2: ",set2)
print("The result of symmetric difference: ",set1.symmetric_difference(set2))
print("The updated set1: ", set1)
print("The updated set2: ",set2)
#symmetric_difference_update()
set1={4,66,89,49,73,1,1}
set2={3,6,8,9,4}
print("Original set1: ",set1)
print("Original set2: ",set2)
print("The result of symmetric difference update: ",set1.symmetric_difference_update(set2))
print("The updated set1: ", set1)
print("The updated set2: ",set2)

# issuperset(),issubset(),isdisjoint()
set1={1,2,3,4}
set2={1,2,3,4,5,6,7,8,9,10}
#check for subset and superset
print("If set1 is a subset of set2: ",set1.issubset(set2))
print("If set1 is a superset of set2: ",set1.issuperset(set2))
print("If set2 is a subset of set1: ",set2.issubset(set1))
print("If set2 is a superset of set1: ",set2.issuperset(set1))
print("If set1 and set2 are dijoint: ",set1.isdisjoint(set2))

# pop() -> randomly removes values from set
set1={9,15,'abc',6,11.2,8}
print("The removed value is: ",set1.pop())
print("Original set: ",set1)
print("The removed value is: ",set1.pop())
print("Original set: ",set1)'''

# Dictionary

# key:value pair 
# {} braces
# both set and dictionary are collection types so,they are unordered
#Empty dictionary specified by{} and empty set denoted by set()

'''dict1={}
print("the dict1 values: ",dict1,"type is: ",type(dict1))
dict1={"name":"ajay", "age":20, "salary":10000}
print("the dict values are: ",dict1)

# Access elements in dict
# with help of keys
dict1={"name":"ajay", "age":20, "salary":10000}
print("the emp name: ",dict1['name'])
print("the salary is: ",dict1['salary']) '''

# Dictionary is also mutable 
# Add new values to dict

'''dict1={"name":"ajay", "age":20, "salary":10000}
dict1['Degree']=['BCA','M.tech','MBA']
print("The dict1 is: ",dict1)

# To update the existing value
dict1["age"]=22
print("The dict1 is: ",dict1)'''

#Remove Salary
# use del property
# do not store backup
'''dict1={"name":"ajay", "age":20, "salary":10000}
print("The original dict1 is: ",dict1)
del dict1["salary"]
print("The updated dict1 is: ",dict1)

res=dict1.pop("age")  # store backup
print("The updated dict1 is: ",dict1)
print("The popped value is: ",res)'''

dict1={"name":"ajay", "age":20, "salary":10000}
print("The length of dict1 is: ",len(dict1))
print("The keys of dict1 is: ",dict1.keys())
print("The values of dict1 is: ",dict1.values())
print("The items of dict1 is: ",dict1.items())
# get() to get value corresponding to a key
print("The value of age is: ",dict1.get("age"))








