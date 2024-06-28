# Class and instantiate the objects
# Define a new class user-defined class
# class keyword
'''
class Employee:
    # define variables or attributes or properties of class
    # define a constructor __init__() to initialise  an object and this constructor will be called everytime we create a new object itself. We do not call init()seperately
    def __init__(self,id,sal,nam):
     self.emp_id =id
     self.emp_sal =sal
     self.emp_name =nam

    # define methods of class
    # self parameter inside method suggests that this method can be only used with the current object of related class
    def emp_details(self):
        print(f" The employee: {self.emp_name}.The emp_id is: {self.emp_id} and salary is: {self.emp_sal}.")

    def input_details(self):
        self.emp_name=input("Enter the employee name: ")
        self.emp_id= int(input("Enter an employee id: "))
        self.emp_sal=int(input("Enter the salary of employee: "))


# out of class
# instantiate the class or create the object of class
print("Creating first employee object...")
emp_obj1= Employee(1,100,'User')
emp_obj1.emp_details() 
emp_obj1.input_details() # call method input_details
emp_obj1.emp_details() # call method emp_details to print
print("Creating second employee object...")
emp_obj2= Employee(2,100,'Guest')
emp_obj2.emp_details() 
emp_obj2.input_details() # call method input_details
emp_obj2.emp_details() # call method emp_details to print
print("Creating third employee object...")
emp_obj3= Employee(3,100,'Guest')
emp_obj3.emp_details() 
emp_obj3.input_details() # call method input_details
emp_obj3.emp_details() # call method emp_details to print
print("Creating fourth employee object...")
emp_obj4= Employee(4,100,'Guest')
emp_obj4.emp_details() 
emp_obj4.input_details() # call method input_details
emp_obj4.emp_details() # call method emp_details to print
print("Creating fifth employee object...")
emp_obj5= Employee(5,100,'Guest')
emp_obj5.emp_details() 
emp_obj5.input_details() # call method input_details
emp_obj5.emp_details() # call method emp_details to print
'''

class Sample:

    # public var
    var1="Public variable"

    # protected var
    _var2="Protected variable"

    # private var
    __var3="Private variable"

    def __init__(self):
       self.var1="Public variable in constr"
       self._var2="Protected variable in constr"
       self.__var3="Private variable in constr"

    def display(self):
        print("The public var is: ",self.var1)
        print("The protected var is: ",self._var2)
        print("The private var is: ",self.__var3)

obj1=Sample()
print("The public var initial val: ",obj1.var1)
obj1.var1="New value outside"
print("The public var new val: ",obj1.var1)
print("The initial protected var: ",obj1._var2)
obj1._var2="New protected value"
print("The new protected var: ",obj1._var2)
#print("The initial private var: ",obj1.__var3)
#obj1.__var3="New private value"
#print("The new private var: ",obj1.__var3)
obj1.display()
