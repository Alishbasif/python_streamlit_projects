Inches_in_foot = 12
#conversion of oot into inches,    1 foot = 12 inches,   foot is bigger than inches.
def main():
    foot = float(input("\033[1;3m Enter the feet to convert in inches: \033[0"))
    conv_foot:float = float(foot * Inches_in_foot)
    print("The " + str(foot) +" foot is converted into " + str(conv_foot) + " inches.")


if __name__ == "__main__":
    main()