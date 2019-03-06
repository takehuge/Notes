class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay=88888888):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def bigname(self):
        print("my pay is as high as $%s" %(self.pay * 16))
        return self.fullname.upper()

    @property
    def smallname(self):
        print("my tax is as high as $%s" %(self.pay * 0.16))
        return self.fullname.lower()

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted {} {}'.format(self.first, self.last))
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{:.2f}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname) #fullname is property without the need of parenthesis

    @classmethod
    def set_raise_amt(cls, amount):
        # cls.tax = cls.pay * 0.07
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

print(Employee.num_of_emps)

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 80000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# # mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(help(Developer))
# print(dev_2.email)
# print(dev_2.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 80000)

print(emp_1)
print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'David Starbridge'
print(emp_1.fullname)
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.pay)
bgname = emp_1.bigname()
print("BIG NAME: %s" %bgname)
sname = emp_1.smallname
print("small name: %s" %sname)

emp_2.fullname = 'Monica Lewinski'
del emp_2.fullname
print(emp_2.fullname)
print(emp_2.email)
print(emp_2.pay)

# print(1+2)
print(int.__add__(1, 2))

# print(emp_1 + emp_2)
# print(emp_1.__len__())

# print(Employee.num_of_emps)

# import datetime
# my_date = datetime.date(2016, 7, 28)
# print(Employee.is_workday(my_date))

# print(emp_1) #giving memory location
#
# emp_1.first = 'Corey'
# emp_1.pay = 50000
#
# print(emp_2.email)

# print(emp_1.fullname())
# print(Employee.fullname(emp_2))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.__dict__) # name space
# print(Employee.__dict__)

Employee.raise_amt = 1.05
emp_1.raise_amt = 1.07

print(emp_1.__dict__)
print(emp_1.raise_amt)

Employee.set_raise_amt(1.08)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# # first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

