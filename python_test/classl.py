from __future__ import *

class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    #def __str__(self):
    #    return '__str__ test'
    def __repr__(self):
        return 'Car({self.color!r}, {self.mileage!r})'

my_car = Car('red',656532)

