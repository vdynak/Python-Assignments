#victoria dynak
#victoria.dynak61@login.cuny.edu
#november 6 2022
#coffees and prices

#test = input("What would you like?")
#test1 = input("What size?")

def computePrice(liquid, size):
    if liquid == "coffee":
        if size == "small":
            x = print("small size coffee: ")
            return 2.5
        if size == "medium":
            x = print("medium size coffee: ")
            return 2.75
        if size == "large":
            x = print("large size coffee: ")
            return 3.00
        else:
            return -1
    elif liquid == "misto":
        if size == "small":
            x = print("small size misto: ")
            return 3.15
        if size == "medium":
            x = print("medium size misto: ")
            return 3.35
        if size == "large":
            x = print("large size misto: ")
            return 3.7
        else:
            return -1
    elif liquid == "mocha":
        if size == "small":
            x = print("small size mocha: ")
            return 3.5
        if size == "medium":
            x = print("medium size mocha: ")
            return 3.8
        if size == "large":
            x = print("large size mocha: ")
            return 4.25
        else:
            return -1
    elif liquid == "tea":
        if size == "small":
            x = print("small size tea: ")
            return 2.35
        if size == "medium":
            x = print("medium size tea: ")
            return 2.45
        if size == "large":
            x = print("large size tea: ")
            return 2.90
        else:
            return -1
    else:
        return -1
        
#computePrice(test, test1)
