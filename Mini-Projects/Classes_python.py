# Classes in Python
# Author: Sospeter Wainaina
# Date: December 12, 2023

# Classes are a way of grouping functions and data together.
# Creating a class is as simple as using the keyword class.
# The first letter of the class name should be capitalized.
# Say we wanted to create a class called Employee that represents information about an employee.

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

# print(emp_1) #we can see that both of these instances were created at different locations in memory. #<__main__.Employee object at 0x00000256228419A0>
# print(emp_2) #<__main__.Employee object at 0x0000025622841B20>

emp_1.first = 'Sospeter'
emp_1.last = 'Wainaina'
emp_1.email = 'Sospeter.Wainaina@company.com'
emp_1.pay = 120000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)