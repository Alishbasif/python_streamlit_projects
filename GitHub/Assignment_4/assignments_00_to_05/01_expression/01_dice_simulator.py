import random          #This will generate the random numbers.

def rollDice():
   numSide = 6

   dice1:int = random.randint(1, numSide)
   dice2:int = random.randint(1, numSide)
   sumDice:int = dice1 + dice2
   print(f"\033[1;3m Total of two dice : {sumDice}\033[0m")

def main():
    rollDice()
    rollDice()
    rollDice()
    
if __name__ == "__main__":
    main()