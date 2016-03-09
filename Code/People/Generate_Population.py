#Version 0.1
#08.03.2016
import random
import csv
from Person_core import Person

def Baby_Born(People):
        first_names = open('first_names_list.txt').read().splitlines()
        last_names = open('last_names_list.txt').read().splitlines()
        Guy = Person(random.choice(first_names),random.choice(last_names) ,0)
        Guy_list = [Guy.first_name,Guy.last_name,Guy.age,Guy.food,Guy.water]
        People.append(Guy_list)

def Generate_Population(number):
    People = []
    Titles = ["First Name","Last Name","Age","Food","Water"]
    People.append(Titles)

    def generate_person(People):
        first_names = open('first_names_list.txt').read().splitlines()
        last_names = open('last_names_list.txt').read().splitlines()
        Guy = Person(random.choice(first_names),random.choice(last_names) ,random.randint(0,100))
        Guy_list = [Guy.first_name,Guy.last_name,Guy.age,Guy.food,Guy.water]
        People.append(Guy_list)

        
    for x in range(0,number):
        generate_person(People)


    with open('population.csv', 'wb') as csvfile:
        pop_writer = csv.writer(csvfile)
        pop_writer.writerows(People)
                                    
        
