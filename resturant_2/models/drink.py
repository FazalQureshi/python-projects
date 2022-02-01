from config.resturant_log import *


logger.info("Module drink created") ##################### logger

class Drink:

    def __init__(self, title, price, volume) -> None:
        self.title = title
        self.price = price
        self.volume = volume