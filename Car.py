# Car Class Program
# Written By Wesley Greer on 4/10/2026


# Write a class named Car that has the following data attributes:
# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.
# These values should be assigned to the object's __year_model and __make data attributes.
class Car:
    def __init__(self, __year_model, __make, __speed):
        self.__year_model = __year_model
        self.__make = __make
        self.__speed = __speed

    # The class should also have the following methods:

    # The accelerate method should add 5 to the speed data attribute each time it it called.
    # The brake method should subtract 5 from the speed data attribute each time it is called.
    # The get_speed method should return the current speed.
    def accelerate(self):
        self.__speed += 5
        return self.__speed
    def brake(self):
        self.__speed -= 5
        return self.__speed
    def get_speed(self):
        print(self.__speed)
        
# Next, design a program that creates a Car object then calls the accelerate method five times.
# After each call to the accelerate method, get the current speed of the car and display it.  
# Then call the brake method.  After each call to the brake method, get the current speed of the car and display it.

car1 = Car("2014 Equinox", "Chevrolet", 0)

for n in range(5):
    car1.accelerate()
    car1.get_speed()

for n in range(5):
    car1.brake()
    car1.get_speed()

