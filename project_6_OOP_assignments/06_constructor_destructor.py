class Logger:

    def __init__(self):
        print("The Constructor is created!")

    def __del__(self):
        print("The constructor is being destructed!")   

l1 = Logger()
