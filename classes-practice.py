class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.pay = pay
        self.email = f"{self.first_name.lower()}{self.last_name.lower()}@bogus.com"


emp1 = Employee("Corey", "Schafer", 50000)

print(emp1.first_name)
print(emp1.last_name)
print(emp1.email)