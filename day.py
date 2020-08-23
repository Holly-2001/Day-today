# program to tell todays day

import datetime

day = datetime.date.today().weekday()
date = datetime.date.today()
print("Today is\n" + str(date))
if day == 0:
    print(mon + daytxt)
    print("Gotta go to work!")
elif day == 1:
    print(tue + daytxt)
    print("Life is full of surprises!")
elif day == 2:
    print(wed + daytxt)
    print("Why weekend still so far!")
elif day == 3:
    print(thu + daytxt)
    print("Just another day...Gotta have some fun!")
elif day == 4:
    print(fri + daytxt)
    print("Make life useful!")
elif day == 5:
    print(sat + daytxt)
    print("In many countries Saturay is a working day.")
elif day == 6:
   
    print("Finally its Sunday!")
    
