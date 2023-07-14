#victoria dynak
#victoria.dynak1@login.cuny.edu
#october 30 2022
#24 hour time

userhour = int(input("Enter hour (in 24 hour time): "))

if userhour<12:
  print("Good Morning")
elif userhour>=12 and userhour<17:
  print("Good Afternoon")
else:
  print("Good Evening")
