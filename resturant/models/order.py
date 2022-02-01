from config.resturant_log import *
import os
from pathlib import Path
os.chdir(Path(__file__).parent)


logger.info("Module order created") ##################### logger

class Order:

    def __init__(self, food_name, drink_name, food_total, drink_total) -> None:
        self.food_name = food_name
        self.drink_name = drink_name
        self.food_total = food_total
        self.drink_total = drink_total
        
        
    def calculate(self):

        logger.info("Bill is calculated") ##################### logger

        self.total = self.food_total + self.drink_total
        print(f"Your Order: {self.food_name}, {self.drink_name}")
        print(f"Your total is: {self.total} Euros")

        logger.info("Bill as .txt file created") ##################### logger

        with open("Bill.txt", mode="a+", encoding="UTF-8") as f:
            f.write(f"Your Order: {self.food_name}, {self.drink_name}\nYour total: {self.total} Euros ")



def txt_pdf_1():
    from fpdf import FPDF

    # save FPDF() class into 
    # a variable pdf
    pdf = FPDF()   
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    
    # open the text file in read mode
    f = open("Bill.txt", "r")
    
    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
    
    # save the pdf with name .pdf
    pdf.output("library_1.pdf")   


def txt_pdf_2():

    import aspose.words as aw

    # load TXT document
    doc = aw.Document("Bill.txt")

    # save TXT as PDF file
    doc.save("txt-to-pdf.pdf", aw.SaveFormat.PDF)