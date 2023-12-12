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

emp_1 = Employee('Sospeter','Wainana',70000)
emp_2 = Employee('Ivy','Mwaniki',70000)

emp_1.raise_amount= 1.50 # this will only affect emp_1 and not emp_2
print(emp_1.__dict__) # we can see that raise_amount has been added to the instance variables
emp_1.apply_raise()
print(emp_1.pay)
print(emp_2.raise_amount)
print(Employee.num_of_emps)