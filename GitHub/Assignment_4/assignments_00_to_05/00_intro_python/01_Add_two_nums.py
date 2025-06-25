def main():
    
    print("This program adds two numbers")
    # first number
    num1  = input("Enter First Number:")
    num1 :int = int(num1)

    # second number
    num2 = input("Enter Second Number:")
    num2: int = int(num2)

    # sum of numbers
    sum : int = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}") 

if __name__ == "__main__":
    main()
