class Decorator:
    def log_function_call(func):
        def wrapper(*args, **kwargs):
            print("Function has been called.")
            return func(*args, **kwargs)
        return wrapper
    

    @log_function_call
    def say_hello(self):
      print("Hello World!")


h1 = Decorator()
h1.say_hello()

