class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def computeArea(self):
        return self.length*self.width

#Driver code
length = 5
width = 10
init_obj = Rectangle(length,width)
print(init_obj.computeArea())
