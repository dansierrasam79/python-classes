#compute area and perimeter
from math import pi
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def computeArea(self):
        return pi*self.radius*self.radius

    def computePerimeter(self):
        return 2*pi*self.radius
# Driver code

#instantiate first circle object and pass in a radius of 3
init_circle_obj = Circle(3)

# call the computeArea method and display circle area rounded to two decimal places
print(round(init_circle_obj.computeArea(),2))

# call the computeArea method and display the circle perimeter rounded to two decimal places
print(round(init_circle_obj.computePerimeter(),2))

