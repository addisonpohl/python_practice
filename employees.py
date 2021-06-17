class Employee():
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay
    # run within the init method since it is run each time an instance is created
        Employee.num_of_emp += 1

    def __repr__(self):
        return f"Employee( '{self.first}', '{self.last}', '{self.email}', '{self.pay}')"

    def __str__(self):
        return f"Name: {self.first} {self.last}, Email: {self.email}, Pay: {self.pay}"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    # allows you to make changes at the class level. 'cls' is used as the first param instead of 'self'
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    # alternative constructor: returns a new instance without having to parse through a string each time "john-doe-50000"
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    # a method related to a class but does not rely on an instance or class variable
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # allows Employee case handle the first three params
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
            print("-> ", emp.fullname())


# import datetime
# my_date = datetime.date(2021,6, 13)
# print(Employee.is_work_day(my_date))

emp_1 = Employee("John", "Adams", 50000)
dev_2 = Developer("Andrew", "Johnson", 75000, "Python")
mgr_1 = Manager("George", "Stevens", [dev_2])

print(isinstance(mgr_1, Developer))  # Returns False since Developer is not inherited during class creation
print(issubclass(Developer, Employee))  # Returns true, since Devloper is inherited from Employee.
