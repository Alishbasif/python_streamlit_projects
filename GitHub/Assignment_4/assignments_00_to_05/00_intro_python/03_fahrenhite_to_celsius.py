def main():

    degrees_fahrenhiet = float(input("\033[1;3m Enter the temperture to convert fahrenhite to celsius: \033[0m"))
    degrees_celsius = (degrees_fahrenhiet-32)*5.0/9.0

    print(f"\033[1;3m Temperature {degrees_fahrenhiet} F : {degrees_celsius} C \033[0m")

if __name__ == "__main__":
    main()