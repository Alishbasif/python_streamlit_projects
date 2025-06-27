Peturksbouip:int = 16
Stanlau :int = 25
Mayengua :int = 48

age = int(input("\033[94m Enter your age : \033[0m"))

def main():
     
    if age >= Peturksbouip:
        print("\033[94m You are eligible to voting in Peturksbouip.\033[0m")
    else:
        print("\033[94m You are not eligible for voting. \033[0m")    


    if age >=  Stanlau:
        print("\033[94m You are eligible to vote in stanlau. \033[0m")
    else:
        print("\033[94m You are not eligible to vote in stanlau. \033[0m")    


    if age >= Mayengua:
        print("\033[94m You are eligible to vote in Mayengua. \033[0m")    
    else :
        print("\033[94m You are not eligible to vote in Mayengua. \033[0m")


if __name__ == "__main__":
    main()