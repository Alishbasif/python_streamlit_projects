def get_user_info():
    
    phonebook = {}
    while True:
        user_name = input("Enter name : ")

        if user_name == "":
            break
        user_num = input(f"Enter number of {user_name} : ")   
        
        phonebook[user_name] = user_num   
    return phonebook
    

def print_dic(phonebook):
        for name in phonebook:
            print(f"{name} ---> {phonebook[name]}")
        return name


def lookup(phonebook):
     
    while True:
        name = input("Enter number for lookup: ")
        if name == "":
            break

        if name not in phonebook:
             print(f"{name} is not stored in phonebook.")
        else:
             print(phonebook[name])    


def main():
    phonebook = get_user_info()
    print_dic(phonebook)
    lookup(phonebook)



if __name__ == "__main__":
    main()    
        