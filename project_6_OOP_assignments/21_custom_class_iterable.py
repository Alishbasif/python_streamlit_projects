class Countdown:
    def __init__(self, start):
          self.start = start

    def __iter__(self):
         return self
    
    def __next__(self):
        if self.start < 0:
            raise StopIteration
        
        else:
            value = self.start
            self.start -= 1
            return value
        
for numbers in Countdown(10):
    print(numbers)



