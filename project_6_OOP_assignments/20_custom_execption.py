class InvalidAgeError(Exception):
    def __init__(self, messege ="Your age must be 18 or older."):
        self.messege = messege
        super().__init__(messege)

def check_age(age):
    if age < 18:
         raise InvalidAgeError()
        
    else:
        print("You are registered!")
    
try:
    check_age(20)
    check_age(10)

except InvalidAgeError as e:
    print(f"Error:  {e}")   
