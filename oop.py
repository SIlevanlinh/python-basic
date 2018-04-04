class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

		Employee.num_of_emps += 1

	@property	
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('Delete Name!')
		self.first = None
		self.last = None

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True	

	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)	
	
	def __str__(self):
		return '{} - {}'.format(self.fullname, self.email)	

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname)

class Developer(Employee):

	raise_amount = 1.10

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
			print('-->', emp.fullname)

emp = Employee('Linh', 'LeVan', 20000)
print(emp)
print(emp.fullname)

print(emp.pay)
emp.apply_raise()
print(emp.pay)

emp1 = Employee('Cube', 'LeVan', 50000)
print(Employee.raise_amount)
print(emp.raise_amount)
print(emp1.raise_amount)

print(emp.__dict__)
print(Employee.__dict__)
print(Employee.num_of_emps)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)

emp_str_messi = 'Leonel-Messi-200000'
messi_emp = Employee.from_string(emp_str_messi)
print(messi_emp.email)

import datetime
my_date = datetime.date(2018, 4, 8)

print(Employee.is_workday(my_date))
print(my_date.weekday())

dev_1 = Developer('Cube', 'LeVan', 50000, 'Python')
dev_2 = Developer('Suarez', 'Luiz', 70000, 'Java')
print(dev_1.email)
print(dev_1.prog_lang)
# print(help(Developer))

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Employee))
print(issubclass(Developer, Employee))

print(emp)
print(emp.__repr__())
print(emp.__str__())

print(emp + dev_1)

print(len(emp))

print(dev_1.fullname)
dev_1.fullname = "Le VanLinh"
print(dev_1.fullname)
del dev_1.fullname
print(dev_1)