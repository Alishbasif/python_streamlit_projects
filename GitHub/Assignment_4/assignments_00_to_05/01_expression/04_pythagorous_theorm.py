import math

def main():
    ab:float = float(input("\033[1;3m Enter the length of Base(AB): \033[0m"))
    bc:float = float(input("\033[1;3m Enter the length of Perpendicular(BC): \033[0m"))

    ac = math.sqrt (ab**2 + bc**2)
    print(f"\033[1;3m The Hypotenous of triangle ABC is {ac}. \033[0m ")

if __name__  == "__main__":
    main()