# Author : Shakirah_Oladokun
# Assignment number & name: Final Project
# Date : July 2020
# Program Description: Problem Solving and programming

#The TransactionItem class holds data fot ID,name,quntity and price
class TransactionItem():
    #Initialize the data attribute
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__quantity = 0
        self.__price = 0

    #create the get and set methods
    def get_id(self):
        return self.__id
    
    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name
    
    
    def get_qty(self):
        return self.__quantity
    def set_qty(self, new_qty):
        #Ensure quantity is positive
        if new_qty > 0:
            self.__quantity = new_qty

    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__price = new_price
    

    #Calculate the total cost of the transaction
    def calc_cost(self):
        cost = self.__quantity * self.__price
        return cost


    def __str__(self):
        transaction_cost = format(self.calc_cost(), '.2f')
        strout = str(self.__id) + ' ' +self.__name + ' ' + \
                 str(self.__quantity) + ' $' + str(transaction_cost)
        return strout
