from typing import MutableMapping
from models.food import Food
from models.drink import Drink
from models.order import Order
from config.resturant_log import *
from databasemanager import Databasemanager

class Menu:
    def __init__(self) -> None:
        self.drink_list = []
        self.food_list = []

    def show_pizza(self):

        logger.info("Menu shown on console") ##################### logger

        for i in self.food_list:
            print(f"Pizza: {i}")

    def show_drink(self):
        for i in self.drink_list:
            print(f"Drink: {i}")
        


    def create_menu(self,database):
        self.database = database
        logger.info("Instances are created add_food") #################### logger

        db = Databasemanager(self.database)
        db.add_food(("Margerita", 10, "Mozerella Cheese"))
        db.add_food(("Fish", 10, "Thun Fish"))
        db.add_food(("Salami", 10, "Chicken"))

        db.add_drink(("Tea", 5, "L"))
        db.add_drink(("Cola", 5, "L"))
        db.add_drink(("Water", 5, "L"))


        self.food_list = db.get_list_foods()
        self.drink_list = db.get_list_drinks()

        #pizza_1 = Food("Margerita", 10, "Mozerella Cheese")
        #pizza_2 = Food("Fish", 10, "Thun Fish")
        #pizza_3 = Food("Salami", 10, "Chicken")

        #drink_1 = Drink("Tea", 5, "L")
        #drink_2 = Drink("Cola", 5, "L")
        #drink_3 = Drink("Water", 5, "L")

        
        #self.food_list.append(pizza_1)
        #self.food_list.append(pizza_2)
        #self.food_list.append(pizza_3)


        #self.drink_list.append(drink_1)
        #self.drink_list.append(drink_2)
        #self.drink_list.append(drink_3)
        
        

def place_order():

    logger.info("Input from user taken") ###################### Logger
    
    food = input("Enter Pizza name: ")
    drink = input("Enter Drink name: ")

    if food == "Margerita":
        food = Food("Margerita", 10, "Mozerella Cheese")
    
    elif food == "Fish":
        food = Food("Fish", 10, "Thun Fish")
    
    elif food == "Salami":
        food = Food("Salami", 10, "Chicken")
    
    
    
    if drink == "Tea":
        drink = Drink("Tea", 5, "L")
    
    elif drink == "Cola":
        drink = Drink("Cola", 5, "L")
    
    elif drink == "Water":
        drink = Drink("Water", 5, "L")



    order_1 = Order(food.title, drink.title, food.price, drink.price)
    order_1.calculate()
