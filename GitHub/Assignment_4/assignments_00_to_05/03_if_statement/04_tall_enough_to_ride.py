min_height:int = 50

user_age:int = int(input("\033[1;3m Enter your age :\033[1;3m"))

def main():
    if user_age >= min_height:
        print("\033[1;3m You are tall enough to ride.\033[1;3m")

    else:
        print("\033[1;3m You are not tall enough to ride.\033[1;3m")


if __name__ == "__main__":
    main()