class Counter:
    count = 0

    def __init__(self):
       Counter.obj_counter()
  
    @classmethod
    def obj_counter(cls):
       cls.count += 1

    @classmethod
    def display(cls):
       return cls.count

c1 = Counter()
c2= Counter()
c3= Counter()
print(Counter.display())
