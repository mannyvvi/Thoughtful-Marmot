#Version 0.1
#08.03.2016
from Generate_Population import Baby_Born
from Generate_Population import Generate_Population
from Read_Population import Read_Population
import random

years = input()
Generate_Population(100)

People = []
Meh = Read_Population(People)
for row in Meh:
    print row
Mehsize = (len(Meh)/2)
print len(Meh)
for z in range(0,years):
    baby_count = random.randint(0,int(float(Mehsize/2)))
    while baby_count > 0:
        Baby_Born(Meh)
        baby_count = baby_count - 1
        
    for i in range(1,len(Meh)):
        try:
            #ages people
            person = Meh[i]
            age = person[2]
            age = int(float(age))
            age = age + 1
            person[2] = age

            #hunger and thirst
            food = int(float(person[3]))
            person[3] = food - 1
            water = int(float(person[4]))
            person[4] = water - 1
            
            if age > 80:
                alive_check = random.randint(80,100)
                if alive_check<age:
                    person[2] = "Dead"
                    Meh[i] = person[2]
                elif water < 0:
                    person[4] = "Dead"
                    Meh[i] = person[3]
                elif food < 0:
                    person[3] = "Dead"
                    Meh[i] = person[4]
            else:
                Meh[i] = person
        except ValueError:
            pass
print"" 
for row in Meh:
    if row == "Dead":
        Meh.pop()
    else:
        print row
print len(Meh)
