C= 299792458
def main():
    m:float = float(input("\033[1;3m Enter the Kilos of Mass = : \033[0m"))
    e :float= m * (C**2)

    print(f"\033[1;3m Finding the energy using E= mc^2 \033[0m")
    print(f"\033[1;3m Mass : {m}kg\033[0m")
    print(f"\033[1;3m Speed of Light : {C} m/s\033[0m")
    print(f"\033[1;3m The energy in joules is {e} joules of energy")

if __name__ =="__main__" :
    main()   