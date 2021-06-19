class Employee():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    # allows a method to be called as an attribute
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    # allows custom assignment of attributes of an instance. Ex: emp_1.fullname = "Jack Dorsey"
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    # specified attributes can be set to none
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"


emp_1 = Employee("John", "Smith")
emp_1.fullname = "Jack Dorsey"

print(emp_1.email)
print(emp_1.fullname)
del (emp_1.fullname)
print(emp_1.fullname)

