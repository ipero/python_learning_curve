# class inheritance demo
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    """Makes triangle"""
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

# override method in inherited class
class Employee(object):
    """employees class"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    """part-timer class"""
    def calculate_wage(self, hours):
        self.hours = hours
        return self.hours * 12

matt = PartTimeEmployee("Matt")
print matt.calculate_wage(28)
