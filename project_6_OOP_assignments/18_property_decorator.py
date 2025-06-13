class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("Getting Price!")
        return self.__price
    

    @price.setter
    def price_set(self,value):
        if value < 0:
            print("The value is Negative.")

        else:
            print("The price has been updated.")
            self.__price += value
            print(f"Your updated price is {self.price}.")          
     

    @price.deleter
    def del_price(self):
        print("The price has been deleter.")
        del self.__price

# creating objects

p1 = Product(100000)
print(p1.price)
p1.price_set = -1789
p1.price_set = 5000
del p1.del_price

# this will raise an error because price attribute is now deleted.
# print(p1.price)
