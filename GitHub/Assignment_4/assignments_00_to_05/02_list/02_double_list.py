def main():
    num:list = [1,2,3,4,5]

    for i in range(len(num)):
        element = num[i]
        num[i] =  element ** 2


    print(num)    


if __name__ == "__main__":
    main()    