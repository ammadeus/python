# 1. Create add method to add two countries together. 
# This method should create another country object with the name of the two countries combined 
# and the population of the two countries added together

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
        
    def add(self, other_country):
        new_name = self.name + " and " + other_country.name
        new_population = self.population + other_country.population
        return Country(new_name, new_population)

antigua = Country('Antigua', 50_000)
barbuda = Country('Barbuda', 47_000)

antigua_and_barbuda = antigua.add(barbuda)
print(antigua_and_barbuda.name, antigua_and_barbuda.population)

# 2. Implement the previous method with a magic method

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
        
    def __add__(self, other_country):
        new_name = self.name + " and " + other_country.name
        new_population = self.population + other_country.population
        return Country(new_name, new_population)

antigua = Country('Antigua', 50_000)
barbuda = Country('Barbuda', 47_000)

antigua_and_barbuda = antigua + barbuda
print(antigua_and_barbuda.name, antigua_and_barbuda.population)

# 3. Create a Car class with the following attributes: brand, model, year, and speed.
# The Car class should have the following methods:accelerate, brake and display_speed.
# The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5. Remember that the speed cannot be negative.

class Auto:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        
    def accelerate(self, increase_speed):
        self.speed += increase_speed
        return f'Auto: {self.model} increase his speed {self.speed}'
    
    def brake(self, decrease_speed):
        self.speed -= decrease_speed
        if self.speed < 0:
            self.speed = 0
        return f'Auto: {self.model} decrease his speed {self.speed}'
    
    def display_speed(self):
        return self.speed

my_car = Auto("Fiat", "Punto", 2022, 0)

print(my_car.accelerate(5))
print(my_car.brake(5))

current_speed = my_car.display_speed()
print(f'The speed car is: {current_speed} km/h')