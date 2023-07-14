#victoria dynak
#victoria.dynak61@login.cuny.edu
#october 8 2022
#converter


print("(a) convert centimeters to feet")
print("(b) convert centimeters to feet and inches")
print("(c) convert feet and inches to centimeters")
decision = str(input("Enter a or b or c: "))
if(decision == "a"):
    centimeters = float(input("Enter height in centimeters: "))
    feet = (0.0328084 * centimeters)
    print(round(feet,2))
elif(decision == "b"):
    centimeters = float(input("Enter height in centimeters: "))
    feet = int(centimeters/30.48)
    inches_non = float((centimeters - (feet * 30.48))/2.54)
    inches = round(inches_non)
    if (inches > 0):
        print("height is ", feet, "feet and" , inches, "inches")
    else:
        print("height is ", feet, "feet")
elif(decision=="c"):
    numbers = input("Enter height in feet and inches, seperated by a space: ")
    numberslist = numbers.split(" ")
    feet_str = numberslist[0]
    feet = int(feet_str)
    inches_str = numberslist[1]
    inches = int(inches_str)
    feet_inch = 12 * feet
    total = feet_inch + inches
    centimeters_non = total*2.54
    centimeters = round(centimeters_non,0)
    print("height is ", centimeters, " cm")
else:
    print("Wrong choice, please enter only a or b or c.")
