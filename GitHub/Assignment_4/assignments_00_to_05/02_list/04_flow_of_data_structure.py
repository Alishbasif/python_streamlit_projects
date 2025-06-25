def add_three_copies(list, message):

    for i in range(3):
        list.append(message)


def main():        
    message = input("Enter the message, you want to copy three times: ")
    list = []
    print("List before", list)

    add_three_copies (list, message)
    print("List after", list)


if __name__ == "__main__":
    main()    