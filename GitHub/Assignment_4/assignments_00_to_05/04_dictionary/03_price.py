def main():

    fruits = {'apple': 4.5, 'durian':27, 'jackfruit':68, 'kiwi':2.5, 'rambtun':6.5, 'mango':4}
    for fruitsName in fruits:
        total_cost = 0
        price = fruits[fruitsName]
        amount = int(input("How much (" + fruitsName + ") do you want? "))
        total_cost += price * amount
    print("The total cost of fruit are : $",total_cost)

if __name__ == "__main__":
    main()


    