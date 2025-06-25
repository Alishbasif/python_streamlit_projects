def main():
    anthon_age:int = 21
    beth_age :int = 6 + anthon_age
    chen_age:int = 20 + beth_age
    drew_age = chen_age + anthon_age
    ethan_age = chen_age

    print(f"Anton's age is :{anthon_age}")
    print(f"Beth's age is : {beth_age}")
    print(f"Chen's age is : {chen_age}")
    print(f"Drew age is :{drew_age}")
    print(f"Ethan age is :{ethan_age}")

if __name__ == "__main__":
    main()