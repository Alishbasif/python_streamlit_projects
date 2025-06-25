days_in_year = 365
hours_in_day = 24
mint_in_hour = 60
seconds_in_mint = 60

def main():
    print(f"\033[1;3m There are {days_in_year * hours_in_day * mint_in_hour * seconds_in_mint} seconds in a year.\033[0m")

if __name__ == "__main__":
    main()