#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 29 2022
#main() testing
   
def main():
    string = input("Enter a string: ")
    character = input("Enter a char: ")
    count = 0
    for x in string:
        if x == character:
            count+=1

    print('number of', character, "in", string, "is", count)

if __name__ == '__main__':
    main()
