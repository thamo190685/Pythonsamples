
class Employee:
    #Common base class for all employees#
    empCount = 0

    def __init__(self, name = "", salary = 0):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

emp = Employee("Thamotharan",45000)

emp1 = Employee("Sridevi",50000)

emp.displayEmployee();
emp1.displayEmployee();

print(Employee.empCount);
