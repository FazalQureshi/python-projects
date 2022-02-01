from config.resturant_log import *


logger.info("Module food is created") ##################### logger

class Food:

    def __init__(self, title, price, ingeridients) -> None:
        self.title = title
        self.price = price
        self.ingeridients = ingeridients