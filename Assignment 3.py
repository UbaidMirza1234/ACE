# 1. Lambda function to merge two lists into a dictionary
merge_lists = lambda keys, values: {keys[i]: values[i] for i in range(len(keys))}

keys = ['a', 'b', 'c']
values = [1, 2, 3]

result = merge_lists(keys, values)
print(result)# 1. Lambda function to merge two lists into a dictionary
merge_lists = lambda keys, values: {keys[i]: values[i] for i in range(len(keys))}

keys = ['a', 'b', 'c']
values = [1, 2, 3]

result = merge_lists(keys, values)
print(result)


# 2. Class Product with discount calculation
class Product:
    discount_rate = 0.1  # Class variable
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def discounted_price(self):
        return self.price * (1 - Product.discount_rate)

product = Product("Laptop", 1000)
print(product.discounted_price()) 



# 3. Shape class with derived Circle and Rectangle classes
import math

class Shape:
    def area(self):
        pass  # Abstract method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
print(circle.area())  # Output: 78.54
print(rectangle.area())  # Output: 24



# 4. Multiple Inheritance with Person, Employee, and Manager
class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

class Manager(Person, Employee):
    def __init__(self, name, emp_id, department):
        Person.__init__(self, name)
        Employee.__init__(self, emp_id)
        self.department = department

manager = Manager("Alice", "M123", "HR")
print(manager.name, manager.emp_id, manager.department)  # Output: Alice M123 HR



class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

def play_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()
cow = Cow()
play_sound(dog)  # Output: Woof!
play_sound(cat)  # Output: Meow!
play_sound(cow)  # Output: Moo!




# 6. Car Rental System using OOP
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, seats):
        super().__init__(brand, model, year)
        self.seats = seats

    def display_info(self):
        return super().display_info() + f", Seats: {self.seats}"

class Bike(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type  # Type can be "Sports" or "Cruiser"

    def display_info(self):
        return super().display_info() + f", Type: {self.type}"

car = Car("Toyota", "Corolla", 2022, 5)
bike = Bike("Yamaha", "R15", 2021, "Sports")
print(car.display_info())  # Output: 2022 Toyota Corolla, Seats: 5
print(bike.display_info())  # Output: 2021 Yamaha R15, Type: Sports
