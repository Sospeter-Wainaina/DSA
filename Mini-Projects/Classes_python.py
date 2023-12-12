# Classes in Python
# Author: Sospeter Wainaina
# Date: December 12, 2023

# Classes are a way of grouping functions and data together.
# Creating a class is as simple as using the keyword class.
# The first letter of the class name should be capitalized.
# Say we wanted to create a class called Employee that represents information about an employee.

class Employee:
    def __init__(self, first, last, pay):
        self.first = first #these are instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' +last + '@company.com'
    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee('Sospeter','Wainana',120000)
emp_2 = Employee('Ivy','Mwaniki',120000)

# we can see that it was easier to create the instances of the class.
print(emp_1.email)
print(emp_2.email)

# We need to create methods which are functions inside a class that work with the object.
print(emp_1.fullname())
print(emp_2.fullname())

# we can also call the method using the class name.
print(Employee.fullname(emp_1))

# print(emp_1) #we can see that both of these instances were created at different locations in memory. #<__main__.Employee object at 0x00000256228419A0>
# print(emp_2) #<__main__.Employee object at 0x0000025622841B20>

# emp_1.first = 'Sospeter'
# emp_1.last = 'Wainaina'
# emp_1.email = 'Sospeter.Wainaina@company.com'
# emp_1.pay = 120000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000
#
# print(emp_1.email)
# print(emp_2.email)

# This is a lot of work to do for each employee.
# We can instead use a special method called __init__ (dunder init). which is a constructor.
#self is the instance of the class. It is used to access variables that belong to the class.
# A constructor is a special method that is run automatically when an instance of a class is created.
# It is used to initialize the object's state.
