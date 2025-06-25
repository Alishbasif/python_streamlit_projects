def main():
    side_1:int = int(input("\033[1;3m What is the length of side 1? \033[0m"))
    side_2:int = int(input("\033[1;3m What is the length of side 2? \033[0m"))
    side_3:int = int(input("\033[1;3m What is the length of side 3? \033[0m"))


    perimeter_triangle = (side_1 + side_2 + side_3)

    print(f"\033[1;3m The perimeter of the triangle is :{perimeter_triangle} \033[0m")


if __name__ == "__main__":
    main()

    