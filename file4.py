# Example of if-elif-else block
# Where we need to check if number is positive, negative or 0
'''
number=int(input("Enter any number in range -ve to +ve: "))

#decision making conditional statement
if number>0:
    print("The number : ",number,"is a posistive number.")
elif number<0:
    print("The number : ",number,"is a negative number.")
else:
    print("The number is 0 .")

#Nested if
num = int(input("Enter any number......"))

#Outer or main if condition
if num>0:
    # first inner if
    if num==0:
        print("The number is 0!!")
    else:
        print("The number is positive ")
# outer elif
elif num<0:
    print("The number is negative")
else:
    print("It is not the desired input")

# for loop
# number of iterations or repetition is known.....

list1=[1,2,3,"hello",True]
for i in list1:
    print("The value in list is: ",i)

# range() -> it generates numbers in a given range
# syntax: range(start, stop , steps)

# use for loop to print a range of numbers

values= range(10)  # a stop parameter only till 10
for i in values:
    print("The generated value is: ",i)

values=range(1,11,2)
list1=list(values)
for i in list1:
    print("The list value: ",i)
print("list= ",list1)'''

# In python we can accompany for loop with else

'''
for iter in seq:
    #statements
else:
    #message orcomputation'''
'''
list1=['Ajay','Raman','Mona','Siya']
count=0
for i in list1:
    print("The name of employee: ",i)
    count=count + 1   # no. of employee
else:
    print("The total number of employee in company: ",count)
    print("No more employees to display!!!!")


# testing for loop
list1=[1,2,3,4]
for _ in list1:
    print("loop working is successful!!!")

# Nested for loop
for i in range(2):
    # inner for loop nested loop
    for j in range(5):  # for each i the j will work for 2 times
        print("The value of i: ",i,"The value of j: ",j)'''

# Examples of while loop

# The EXAMPLE checks if the user has entered correct password for login
# else the user is asked to retry login
# The scenerio says the user can try infinite times

'''while True:
    user_name=input("Enter your user name....")
    password_input=input("Enter your password....")

    # using decision statements
    if password_input=="Password":
        print(user_name,"!! You are welcome in the system")
        break #It exits or break the loop without continuing further
    elif password_input=="Quit":
        print("You are exiting the system!!!")
        break
    else:
        print("Either username or password is incorrect!!")
'''


# calculate the sum of numbers in user enter 'Quit'

'''num1=int(input("Enter the number: "))
choice=input("You want to Continue or Quit: ")
sum=num1

# taking input of other values to add to number or enter'Quit'
while True:
    if (choice=="Quit"):
        print("You Quit!!")
        break
    elif choice.upper()=="YES" or choice.upper()=="Y":
        num2=int(input("Enter second number to add: "))
        sum=sum+num2
        print("The final sum of numbers is: ",sum)
        choice=input("You want to continue or Quit: ")
    else:
        print("Enter a relevant choice!!")
        choice=input("You want to continue or Quit: ")'''

'''for i in range(10):
    if i==7:
        print("Limit reached 7!!")
        break
    else:
        print("The value is: ",i)

print("Out of for loop!!")

for i in range(10):
    if i==7:
        print("Limit reached 7!!")
        continue
    else:
        print("The value is: ",i)

print("Out of for loop!!")'''
        
for i in range(10):
    if i==7:
        print("Limit reached 7!!")
        break
    elif i==5:
        print("Limit to 5 reached!! Warning!! ")
        pass # do nothing
    else:
        print("The value of i is: ",i)

print("Out of for loop!!")
