def main():
    
    my_list = []
    element = input("Enter the Value and press enter if you want to stop:")

    while element:
        my_list.append(element)
        element = input("Enter the Value :")
    print("Here's the list" , my_list)
    
    
if __name__ =="__main__":
    main()

