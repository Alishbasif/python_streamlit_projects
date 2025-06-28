def get_user_num():

    user_num = []

    while True:
        user_input = input("\033[1;3m Input the number: \033[0m")
        if user_input == "":
            break

        num= int(user_input) 
        user_num.append(num)   
    return user_num


def count_num(num_1st):
    dic_num = {}

    for num in num_1st:
        if num not in dic_num:
            dic_num[num] = 1
        else:
            dic_num[num] += 1

    return dic_num


def print_num(dict_num):
    for num in dict_num:
        print(f"{num} appears {dict_num[num]} times.")


def main():
    userNumbers = get_user_num()
    num_dict= count_num(userNumbers)
    print_num(num_dict)

if  __name__ == "__main__":
    main()


