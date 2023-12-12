# class variables are shared among all instances of a class
# instance variables are unique to each instance of a class

class Employee:
    # class variables
    raise_amount = 1.04
    # number of employees
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first  # these are instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = float(
            self.pay * self.raise_amount)  # here we are using self.raise_amount instead of Employee.raise_amount because we anticipate that the raise amount might change in the future and affect employees differently.

    @classmethod  # this is a decorator
    def set_raise_amount(clscls, amount):
        Employee.raise_amount = amount

    @classmethod
    def emp_from_string(cls, emp_str):
        '''This is an alternative constructor that takes in a string separated with hyphens and creates an employee from it'''
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static methods do not take in the instance or the class as the first argument
    # they behave just like normal functions except that we include them in our classes because they have some logical connection with the class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False  # this is a weekend
        return True

    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay


class Developer(
    Employee):  # this is a subclass of Employee and it inherits all the attributes and methods of the Employee class
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print(f"{emp} is already in the list of employees under this manager")

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print(f"{emp} is not in the list of employees under this manager")

    def list_employees(self):
        for emp in self.employees:
            print(f'--> {emp.fullname()}')


emp_1 = Employee('Sospeter', 'Wainaina', 70000)
emp_2 = Employee('Ivy', 'Mwaniki', 70000)

dev1 = Developer('Maina', 'Kingangi', 50000, 'Python')
dev2 = Developer('Efford', 'Mwirikia', 60000, 'PHP')

mgr_1 = Manager('Sue', 'Smith', 150000, [dev1, emp_1])

print(dev1)
print(dev1 + dev2)
print(dev1.prog_lang)
mgr_1.add_emp(dev2)
print(mgr_1.list_employees())
# print(help(Developer))
