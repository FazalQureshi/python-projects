from models.menu import Menu
from models.menu import place_order as po
from config.resturant_log import *
from models.order import txt_pdf_1 as tp1
from models.order import txt_pdf_2 as tp2
from pathlib import Path
os.chdir(Path(__file__).parent)

from databasemanager import Databasemanager



db = Databasemanager("./restaurant2.db")


logger.info("Module app is created") #####################logger

def app():

    
    menu1 = Menu()
    menu1.create_menu("./restaurant2.db")
    menu1.show_pizza()
    menu1.show_drink()
    po()
    #menu1.show_pizza()
    #menu1.show_drink()
    #place_order()
    tp1()
    tp2()


logger.info("Application is started") ################logger
app()


