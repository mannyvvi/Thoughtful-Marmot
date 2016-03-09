#Version 0.1
#08.03.2016

class Person:
    def __init__(self,first_name,last_name,age):     
        self.first_name =  first_name
        self.last_name = last_name
        self.age = age
        self.food = 100
        self.water = 100

    def display(self):
        print "Name: " + self.first_name + " " + self.last_name
        print "Age: " , self.age
        print "Needs: "
        print self.food
        print self.water

