# Function demo

'''def printOutput(str1):
    #function statements
    print("The parameter given to function: ",str1)
    return

# To call this function for execution
input1=input("Enter user name: ")
printOutput(input1)

# User enter username --> assigned to input1 --> input1 assigned to str1 on function call --> executed
# input1 is actual parameter because it is the real value sent to the function
# str1 is known as formal parameter as it is a formality of copying value of actual parameter to
# formal parameter

# without parameter

def print_output():
    input1=input("Enter a username: ")
    print("The parameter given to function: ",input1)
    return

print_output()

def func1(mylist):
    print("Values inside the function before change: ",mylist)
    mylist[2] =60
    print("Values inside function after change: ",mylist)
    

mylist=[10,20,40]
func1(mylist)
print("Values outside the function: ",mylist)'''

'''def add(a,b):
    sum=a+b
    print("Value of a: ",a)
    print("Value of b: ",b)
    print("Sum : ",sum)
    return sum  # return statement return value outside the function

n1=int(input("Enter a: "))
n2=int(input("Enter b: "))
result=add(n1,n2)
print("Sum of number: ",result)'''

# default argument
# in case user fails to give necessary argument default values of argument will be taken

'''def add(a,b=6): # we can give default argument right to left
    sum=a+b
    print("Value of a: ",a)
    print("Value of b: ",b)
    print("Sum : ",sum)
    return sum  # return statement return value outside the function


result=add(8,7)
print("Sum of number: ",result)'''

# dynamically passing any number of arguments **args
'''def func1(**args):  # **args will by default act as a dictionary with key value pairs
    for key,value in args.items():
        print("The key is: ",key," The value is: ",value)

func1(name="Jannat", age=20, salary=10000, degree=["MBA","MCA","BCA"])'''

# dynamically give many simple arguments
# *args
def func1(*val):
    total=0
    for i in val:
        total=total+i
    print("The sum is: ",total)

# call the function
func1(1,2)
func1(1,2,3,4)
func1(1,2,3,4,5,6,7,8,986)








