# Employee Class Program
# Written By Wesley Greer on 4/9/2026

# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.
class Employee:
    def __init__(self, name, id, department, title):
        self.name = name
        self.id = id
        self.department = department
        self.title = title
# Once you have written the class, write a program that creates three Employee objects to hold the following data.
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones",39119,"IT","Programmer")
employee3 = Employee("Joy Rogers",81774,"Manufacturing","Engineer")
# The program should store the data in the three objects, then display the data for each employee on the screen.
print("Name:", employee1.name, "  ID:", employee1.id, "  Department:", employee1.department, "  Title:", employee1.title)
print("Name:", employee2.name, "  ID:", employee2.id, "  Department:", employee2.department, "  Title:", employee2.title)
print("Name:", employee3.name, "  ID:", employee3.id, "  Department:", employee3.department, "  Title:", employee3.title)
