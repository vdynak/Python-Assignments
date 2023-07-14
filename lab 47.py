#victoria dynak
#victoria.dynak.801839@gmail.com
#november 19 2022
#perfect number function

def isPerfect(number):
    x = False
    while x == False:
        sum = 0
        if number <= 0:
            print(number, "is not a perfect number.")
            number = int(input("Re-enter: "))
        elif number > 0:
            for y in range(1, number//2+1):
                if number % y == 0:
                    sum = sum + y
            if sum == number:
                print(number, "is a perfect number.")
                print("Congratulations!", number, "is a perfect number.")
                x = True
            else:
                print(number, "is not a perfect number.")
                number = int(input("Re-enter: "))

def main():
    number = int(input("Enter a perfect number: "))
    isPerfect(number)
    

if __name__ == "__main__":
    main()
