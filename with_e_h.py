def isLeap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("%d is leap year"%year)
            else:
                print("%d not leap year"%year)
        else:
            print("%d is leap year"%year)
    else:
        print("%d not leap year"%year)
        
def main():
    while True:
        year = input("Enter a year: ")
        try:
            year = int(year)
            if isinstance(year, int):
                isLeap(year)
                break
        except ValueError:
            print("This is not a year. Try again.")
            continue

if __name__ == "__main__":
    main()