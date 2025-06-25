def get_first_element(Ist):
    print(len(Ist))
    print(Ist[0])


def get_Ist():
    Ist = []

    element :str = input("Enter the element in list and press enter to stop :")
    while element != "":
        Ist.append(element)
        element = input("Enter the element in list and press enter to stop: ")
    return Ist


def main():
    Ist = get_Ist()
    get_first_element(Ist)

if __name__ == "__main__":
    main()