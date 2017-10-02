class Employee:
    raise_amount = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.pay = pay
        self.email = f"{self.first_name.lower()}{self.last_name.lower()}@bogus.com"

    def apply_raise(self):
        self.pay *= self.raise_amount


emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Jane", "Smith", 70000)

emps = [emp1, emp2]

for i in emps:
    print(i.first_name)
    print(i.last_name)
    print(i.email)
    print(i.pay)
    print()

print('{:,.2f}'.format(emp1.pay))
emp1.apply_raise()
print('{:,.2f}'.format(emp1.pay))

print()

print('{:,.2f}'.format(emp2.pay))
emp2.apply_raise()
print('{:,.2f}'.format(emp2.pay))

print()

Employee.raise_amount = 1.10

print('{:,.2f}'.format(emp1.pay))
emp1.apply_raise()
print('{:,.2f}'.format(emp1.pay))

print()

print('{:,.2f}'.format(emp2.pay))
emp2.apply_raise()
print('{:,.2f}'.format(emp2.pay))