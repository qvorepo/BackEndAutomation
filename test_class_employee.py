class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Karla', 'Sheuline', 80000)
print(emp_1.email)

emp_2 = Employee('Colleen', 'Brown', 110000)
print(emp_2.email)

print(emp_1.fullname())