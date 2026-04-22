
class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def __init__(self,radius):
        self.radius =radius
    def area(self):
        print("circle area =,3.14*self.radius*self.radius")

c = Circle(5)
c.area()