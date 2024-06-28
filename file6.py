# Recursion in functions
# Re-currence of calling self by the function

# Syntax

'''def func1(arg1,arg2):
     #statement
     # statements
     func1(v1,v2)  # will self call itself
    # will move out
    '''

# Factorial calculation for a number without using recursion
# without using factorial
'''num=int(input("Enter the number: "))

fact=1
if num==0 or num==1:
    print(num,"! = 1")
elif num<0:
    print("Cannot calculate factorial for negative number")
else:
    while(num>0):
        fact=fact*num 
        num=num-1

print("The factorial of number: ",fact)'''

#with recursion

'''def calc_recur(num):
    if num==0 or num==1:
        return 1
    elif num<0:
        print("Cannot calculate factorial of negative number")
    else:
        return(num*calc_recur(num-1))
    # 5! = 5*calc_recur(4) -> 5*4*calc_recur(3) -> 5*4*3*calc_recur(2) -> 5*4*3*2*calc_recur(1) ->5*4*3*2*1

num=int(input("Enter the number: "))
result= calc_recur(num)
print(" The factorial of number {} is: ".format(num),result)'''

# Use recursion to calculate sum of n numbers
'''
def func_sum(num):
    if num<=1:
        return num
    else:
        return num+func_sum(num-1)

num=int(input("Enter the limit n of summ calcultion: "))
if num<=0:
    print("Cannot calculate sum of 0 or -ve limit")
else:
    print("Sum of {} +ve numbers is: ".format(num),func_sum(num))
'''

# variable scope: A variable scope is region or area where that variable can be accessed
# lifetime: lifetime of variable is the number of lines of code in which that variable is used

# According to scope we have 3 types of variable:
#1. Local variable
# 2. Global variable
#3. Non-local variable

# Local variable

'''def func1():
    result="Final message inside function"
    print("The result is:",result)
    # lifetime of variable is 2 lines 70-71

func1() # calling func outside
print("The result is: ",result)  # not accessed'''

# Global variables

'''result="Message outside any function scope"

# 1 usage
def func2():
    print("Calling result inside func2() is: ",result)

# come outside the func2
func2()
print("Calling result outside func2() is: ",result)'''


# Non-local variables
# are used in context of nested function such that these variables cannot be assumed be in local
# or global

'''def func_outer():
    result="Inside func_outer()"
    print("The result is: ",result) 
# Create a nested function
    def func_inner():
      nonlocal result
      result="Inside func_inner()"
      print("The result is: ",result) 

# COME outside inner()

    print("Calling inner func()")
    func_inner()
    print("the result inside outer_func()and outside inner_func():",result)

print("Calling outer_func()")
func_outer()'''

# Exception handling
# how to view all built-in exception

'''print(dir(locals()['__builtins__']))'''

# arithmetic error

'''
try:
    # statements
except Exception_Name1:
    # This will handle for only Exception_Name1
except Exception_Name2:
    # This will handle for only Exception_Name2
except:
    # This will be general except block for any exception
else:
    #This statement will be executed only if none of except statements are working
finally:
    #This block will work irrespective of the exception'''

# Arithmetic error -> num/0 =inf
'''try:
    num1= int(input("Enter numerator: "))
    num2=int(input("Enter denominator: "))
    result=num1/num2
    list1=[1,2,3,4,5]
    i=int(input("Enter the index value of list element for access: "))
    print("The result is: ",result)
    print("The last element in list: ",list1[i])
except ZeroDivisionError:
    print("Cannot divide by zero... Give inputs again")
except IndexError:
    print("Cannot access element beyond the length of list")
except:
    print("An exception occured....Please check inputs again!!")
else:
    print("No exception occured!! Successful execution!!")
finally:
    print("Inside finally block...")
    userName=input("Enter user name: ")
    print("Welcome to python program ",userName)

# Case1: When no exception occurs: try -> else -> finally blocks execute
# Case2: When first exception ZeroDivisionError occurs:
#                              try-> except ZeroDivisionError -> finally
#Case 3: When second exception IndexError occurs:
#                              try-> except IndexError -> finally
# Case4: When any other error occurs apart from above 2 errors
#                              try -> except -> finally '''


# User- Defined Exception
# Create a new user class which is derived from exception class
# Create exception for retired senior citizen candidates
class InvalidAgeException(Exception):
    pass

age=int(input("Enter a relevant age for retired employee: "))
try:
    if age<60:
        raise InvalidAgeException
    else:
        print("Valid age entered!!")
        print("The employee is eligible for pension")
except InvalidAgeException:
    print("Exception occured!!")
