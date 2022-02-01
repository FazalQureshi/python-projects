from models.menu import Menu
from models.menu import place_order
from config.resturant_log import *
from models.order import txt_pdf_1 as tp1
from models.order import txt_pdf_2 as tp2

logger.info("Module app is created") #####################logger

def app():

    menu1 = Menu()
    menu1.create_menu()
    menu1.show_pizza()
    menu1.show_drink()
    place_order()
    tp1()
    tp2()


logger.info("Application is started") ################logger
app()


