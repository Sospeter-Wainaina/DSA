# class variables are shared among all instances of a class
# instance variables are unique to each instance of a class

class Employee:
    # class variables
    raise_amount = 1.04
    # number of employees
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first #these are instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' +last + '@company.com'
        Employee.num_of_emps += 1
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount) # here we are using self.raise_amount instead of Employee.raise_amount because we anticipate that the raise amount might change in the future and affect employees differently.

    @classmethod # this is a decorator
    def set_raise_amount(clscls,amount):
        Employee.raise_amount = amount

    @classmethod
    def emp_from_string(cls,emp_str):
        '''This is an alternative constructor that takes in a string separated with hyphens and creates an employee from it'''
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    # static methods do not take in the instance or the class as the first argument
    # they behave just like normal functions except that we include them in our classes because they have some logical connection with the class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False # this is a weekend
        return True

emp_1 = Employee('Sospeter','Wainaina',70000)
emp_2 = Employee('Ivy','Mwaniki',70000)

# Employee.set_raise_amount(1.05) # this will affect all employees
Employee.set_raise_amount(1.05)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# we can also use the class method as an alternative constructor
# say we have employee information in a string separated by hyphens
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
emp_str_4 = 'Mary-Jane-100000'

#we can use the split method to separate the string into a list
first,last,pay = emp_str_1.split('-')
emp_3 = Employee(first,last,pay)
print(emp_3.email)
emp_4 = Employee.emp_from_string(emp_str_4)
print(emp_4.email)

# static methods
import datetime
my_date = datetime.date(2023,12,12)
print(Employee.is_workday(my_date))