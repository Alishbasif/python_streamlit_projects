class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} of model {self.model} is starting...")  


c1 = Car("Toyota", "Corolla")
c1.start()