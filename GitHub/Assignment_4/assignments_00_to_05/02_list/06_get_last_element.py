def get_last_element(Ist):
    
    print(len(Ist)-1)
    print(Ist[-1])


def get_Ist():
    Ist = []

    element = input("Enter the element in list and press enter to stop: ")
    while element != "" :
        Ist.append(element)
        element = input("Enter the element in list and press enter to stop: ")
    return Ist

def main():
    Ist = get_Ist()
    get_last_element(Ist)


if __name__ =="__main__":
    main()    