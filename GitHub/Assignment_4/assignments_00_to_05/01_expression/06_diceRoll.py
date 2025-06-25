import random          #This will generate the random numbers.

def main():
   numSide = 6

   dice1:int = random.randint(1, numSide)
   dice2:int = random.randint(1, numSide)
   sumDice:int = dice1 + dice2

   print(f"\033[1;3mThe Dice have {numSide} die.\033[0m")
   print(f"\033[1;3m The value in First Die = \033[0m", dice1)
   print(f"\033[1;3m The value in Second Die =\033[0m ", dice2)
   print(f"\033[1;3m Total of two dice : {sumDice}\033[0m")


if __name__ == "__main__":
   main()