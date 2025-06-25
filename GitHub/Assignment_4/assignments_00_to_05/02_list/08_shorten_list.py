MAX_LENGTH:int = 3

def shorten(Ist):
    while len(Ist) > MAX_LENGTH:
       last_element = Ist.pop()
       print(last_element)

def get_element():

    Ist = []
    element = input ("Enter the value in list and press enter if you want to stop: ")
    while element != "":
        Ist.append(element)
        element = input ("Enter the value in list and press enter if you want to stop: ")
    return Ist 

def main():
    Ist = get_element()
    shorten(Ist)   


if __name__ == "__main__":
    main()   
