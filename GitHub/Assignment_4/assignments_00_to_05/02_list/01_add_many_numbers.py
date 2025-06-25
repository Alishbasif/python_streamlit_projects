def add_many_num(number) ->int:

    initialNum:int = 0
    
    for num in number :
        initialNum += num
    
    return initialNum
    

def main():
    number:list[int] = [1,2,3,4,5]
    sum:int = add_many_num(number)
    print(f"The sum of the numbers is {sum}.")


if __name__ =="__main__":
    main()    