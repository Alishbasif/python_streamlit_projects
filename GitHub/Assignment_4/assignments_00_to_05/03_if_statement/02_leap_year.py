year:int = int(input("Please enter the year: "))

def main():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                print("That's the leap year.")
            else:
                print("That's not the leap year.")

        else:
            print("That's the leap year") 

    else:   
         print("That's not the leap year.")    


if __name__ == "__main__":
    main()
