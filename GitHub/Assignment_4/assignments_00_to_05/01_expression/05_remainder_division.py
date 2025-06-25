def main():

    dividend:int = int(input("\033[1;3m Enter the integer to be divide: \033[0m"))
    divisor:int = int(input("\033[1;3m Enter the integer by divide: \033[0m"))               

    quotient: int = dividend // divisor  
    remainder: int = dividend % divisor  
    print(f"\033[1;3m The result of the division {dividend} by {divisor} is {quotient} and the remainder is {remainder}. \033[0m")

if __name__ == "__main__":
    main()