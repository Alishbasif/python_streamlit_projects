import random


min_num:int = 1
max_num:int = 100

def main():
    for num in range(10):
        value = random.randint(min_num , max_num)
        print(value)

if __name__ == "__main__":
    main()
