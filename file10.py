# Simple single inheritance single parent class -> single child class

'''class Parent:
    value=10
    def __init__(self,num):
        self.value=num
        print("In parent class constructor the value is:",self.value)
        print("The num argument is:",num)
    def parentfunc1(self):
        print(f"This is a parent class method of parentfuc() and value is {Parent.value}")
    # Parent.value -> Create a temporary unnamed Parent obj that will call Parent value
    def func1(self):
        print("This is func1() of parent class")

class Child(Parent):
    value=30
    def __init__(self):
        print("Inside child class constructor")
        # we can call parent class constructor from here
        super().__init__(70)
    def childfunc1(self):
        print(f"This is child class method childfunc() and value is {self.value}")
    def func1(self):
         print("This is func1() of child class")
         super().func1() # this will call func1() of parent class
obj1=Child()
obj1.func1()
obj1.childfunc1()
obj1.parentfunc1()  # reusing the parent class method
# Variable and method overriding

#Check for subclass and superclass and object checking

print("Child is subclass of Parent: ",issubclass(Child,Parent)) # True
print("Parent is subclass of Child: ",issubclass(Parent,Child)) # False

# Object checking
print("obj1 is object of Child: ",isinstance(obj1,Child)) #True # instance is another name of object
print("obj1 is object of Parent: ",isinstance(obj1,Parent)) # True

#obj2=Parent()
#print("obj2 is object of Child: ",isinstance(obj2,Child)) #False # instance is another name of object
#print("obj2 is object of Parent: ",isinstance(obj2,Parent))# True

# super() -> super keyword is used to access the parent class constructor,method and variables from inside the child class

# in python the order of resolving the call to constructor and methods of inherited class
# MRO -> method resolution order
print("The MRO Order with __mro__ property is: ",Child.__mro__)
print("The MRO Order with mro() property is: ",Child.mro())'''

# 2.Multiple Inheritance
# 2 or more parent class and only 1 child class
#    Parent1, Parent2, Parent3.....Parent N
#         \       \       /          /
#                Inherited by 1 Child class
# 3. Multilevel Inheritance
#      Grandparent
#           |
#      Parent1     Parent2
#         \           /
#           Child1
'''class GrandParent:
    def __init__(self):
        print("Inside GrandParent class constructor")

class Parent1(GrandParent):
    def __init__(self):
        print("Inside Parent1 class constructor")
        super().__init__()

class Parent2():
    def __init__(self):
        print("Inside Parent2 class constructor")
        super().__init__()

class Child1(Parent2,Parent1):
    def __init__(self):
        print("Inside Child1 class constructor")
        super().__init__()

obj1=Child1()
print("The MRO Order with __mro__ property is: ",Child1.__mro__)
print("The MRO Order with mro() property is: ",Child1.mro())'''

# 4.Hierarchical Inheritance
#       Only 1 PARENT class
#          /     /     \       \
#      Child1   Child2  Child3 Child4
# opposite of multiple inheritance

'''class Parent1:
    def __init__(self):
        print("Inside PARENT 1 Constructor")

class Child1(Parent1):
    def __init__(self):
        print("Inside child 1 Constructor")
        super().__init__()

class Child2(Parent1):
    def __init__(self):
        print("Inside child 2 Constructor")
        super().__init__()

print("...................Creating child1 object....................")
obj1=Child1()
print("...................Creating child2 object....................")
obj1=Child2()
print("The MRO Order with __mro__ property is: ",Child1.__mro__)
print("The MRO Order with mro() property is: ",Child1.mro())
print("The MRO Order with __mro__ property is: ",Child2.__mro__)
print("The MRO Order with mro() property is: ",Child2.mro())'''

# Diamond problem

#       GrandParent
#           /   \
#     Parent1    Parent2
#       \          /
#        Child class

class GrandParent:
    def func1(self):
        print("Inside GrandParent class func1()")

class Parent1(GrandParent):
    def func1(self):
        print("Inside Parent1 class func1()")
        super().func1()

class Parent2(GrandParent):
    def func1(self):
        print("Inside Parent2 class func1()")
        super().func1()

class Child1(Parent1,Parent2):
    pass

obj1=Child1()
obj1.func1()
print("The MRO Order with __mro__ property is: ",Child1.__mro__)
print("The MRO Order with mro() property is: ",Child1.mro())
    