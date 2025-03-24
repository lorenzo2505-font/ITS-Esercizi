'''Exercise 4 (Folder 9 ex_4.py)

1. Write a new class called Food, it should have name, price and
description as attributes.

2. Instantiate at least three different foods you know and like.

3. Create a new class called Menu, it should have a list (of Foods) as attribute.
__init__ should take a list of Foods as optional parameters (default=[])

4. Create a addFood() and removeFood() for the Menu

5. Create a few new Food instances. Add each to the Menu using the respective
Method.

6. Add a method printPrices() that list all items on the Menu with their
prices.

7. Add a Menu method getAveragePrice() that returns the average Food
price of the Menu'''

class Food:
    def __init__ (self, name: str, price: float, des: str):
        self.name = name
        self.price = price
        self.des = des

carbonara = Food ("Pasta Alla Carbonara", 11.0, "cremosa")
diavola = Food ("Pizza Alla Diavola", 8.0, "piccante")
maritozzo = Food ("Maritozzo", 2.10, "dolce")

class Menu:
    foods_menu = []
    def __init__ (self, food_name: str, food_price: float):
        self.foods_menu = food_name
        self.foods_menu.append(food_price)
    
    def add_food(self):
        ''''''