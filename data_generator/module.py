# Imports
import numpy as np
import pandas as pd
import random

# Classes
def data_generator():
        
    class Data_int_float:

        def __init__(self, name_column, max_val, min_val, number_of_rows) -> None:
            self.name_column = name_column
            self.max_val = max_val
            self.min_val = min_val
            self.number_of_rows = number_of_rows
            
        def create_list_int_float(self):
            #w = np.random.uniform(self.min_val, self.max_val, size=(self.number_of_rows))
            w = np.random.randint(self.min_val, self.max_val, size=(self.number_of_rows))
            
            return w


    class Data_str:

        def __init__(self, name_column, name_product, number_of_rows) -> None:

            self.name_column = name_column
            self.name_product = name_product
            self.number_of_rows = number_of_rows

        def create_list_str(self):
            e = random.choices(self.name_product, k = self.number_of_rows)
            return e


            


    # Inputs

    name_file = input("Enter the name of the 'CSV' file: ")
    number_of_rows = int(input("Enter number of rows for the data set: "))
    number_of_columns = int(input("Enter number of columns: "))
    name_list_int = []
    name_list_str = []
    products = []
    for i in range(number_of_columns):
        x = input(f"Enter data type for the {i}th column: Options -> int, str: ")
        
        name = input("Enter the name of the column: ")

        if x == "int":
            
            min = int(input("Enter min value: "))
            max = int(input("Enter max value: "))
            name = Data_int_float(name, max, min, number_of_rows)
            name_list_int.append(name)

        
        elif x == "str":
            q = 0
            while True:
                j = input("Enter a list of products type 'exit' to exit: ")
                if j == "exit":
                    break
                products.append(j)
                q +=1
            
            name = Data_str(name, products, number_of_rows)
            name_list_str.append(name)



    def dictionary_1():

        i = 0
        dict_1 = {}
        for t in name_list_int:
            r = t.create_list_int_float()
            dict_1[t.name_column] = r
            i+=1
        return dict_1


    def dictionary_2():

        i = 0
        dict_2 = {}
        for z in name_list_str:
            u = z.create_list_str()
            dict_2[z.name_column] = u
            i+=1
        return dict_2

    dic_1 = dictionary_1()
    dic_2 = dictionary_2()

    dic_3 = {**dic_1, **dic_2}

    df = pd.DataFrame(dic_3)
    df.to_csv(f'{name_file}.csv', index=True, sep=',')




'''
print(dic_1)
print(dic_2)
print()
print(dic_3)
print(name_list_int)






# Create a data frame

def df_data_generator():
    products = []
    for i in range(100):
        a = 'Product '
        b = str(i)
        c = a + b
        products.append(c)

    #prices = list(range(100))
    prices = np.random.uniform(50, 1000, size=(100))

    data = {'product_name': products,
            'price': prices
            }

    df = pd.DataFrame(data)
    df.to_csv('data_generator.csv', index=True, sep=',')
#print (df)
#print(df.describe)

#df_data_generator()




df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

df2

'''