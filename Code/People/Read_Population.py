#Version 0.1
#08.03.2016
import csv

def Read_Population(People):
    People = []
    with open('population.csv', 'rb') as csvfile:
                popreader = csv.reader(csvfile)
                for row in popreader:
                    People.append(row)
    return People




