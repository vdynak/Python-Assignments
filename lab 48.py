#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 20 2022
#1-6 user/computer draw

import random
def number():
    number = int(input("Enter only 1-6: "))
    while number>6 or number<1:
        print("Input needs to be 1-6. Re-enter: ")
        number = int(input("enter only 1-6: "))
    return number
def compute():
    user = number()
    computer = random.randrange(1,7)
    print("user: " + str(user))
    print("computer: " + str(computer))
    if user == computer:
        print("draw")
    elif user + computer in (3,6,7,8):
        print("user wins")
    else:
        print("computer wins")
def main():
    compute()

if __name__ == "__main__":
    main()
