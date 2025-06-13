class Engine:

    def start(self):
        print("Engine has been started.")

class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
       return self.engine.start()
    

c1 = Car()
c1.start_car() 