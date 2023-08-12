# 1. Create a class Product with properties name, price, and quantity. 
# Create a child class Book that inherits from Product and adds
# a property author and a method called read that prints information about the book

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
         print(f"Title is: {self.name}, Price is: {self.price}, Quantity: {self.quantity}, Author is : {self.author}")
         
book = Book("Il Signore degli Anelli", 25.99, 100, "J.R.R. Tolkien")
book.read()

# 2. Create a class Restaurant with properties name, cuisine, and menu. The menu property should be a dictionary with
# keys being the dish name and values being the price. Create a child class FastFood that inherits from Restaurant and adds a property drive_thru
# (a boolean indicating whether the restaurant has a drive-thru or not) and a method called order which takes in the dish name
# and quantity and returns the total cost of the order. The method should also update the menu dictionary to subtract the ordered quantity from the available quantity. 
# If the dish is not available or if the requested quantity is greater than the available quantity, the method should return a message indicating that the order cannot be fulfilled.

class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu 
        
    def order(self, dish_name, quantity):
        if dish_name in self.menu and quantity <= self.menu[dish_name]:
            total_cost = self.menu[dish_name] * quantity
            self.menu[dish_name] -= quantity
            return total_cost
        else:
            return "Order is not avalible."    
        
class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru
        

restaurant = Restaurant("La Trattoria", "Italian", {"Pasta": 9.99, "Pizza": 9.99, "Salad": 8.99})
fast_food = FastFood("FastBites", "Burger", {"Burger": 4.99, "Fries": 2.99, "Soda": 1.99}, True)

fast_food_order = fast_food.order("Burger", 2)
print(f"Total cost of fast food order: ${fast_food_order}")

restaurant_order = restaurant.order("Pasta", 1)
print(f"Total cost of restaurant order: ${restaurant_order}")