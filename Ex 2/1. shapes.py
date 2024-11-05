class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def getPoint(self):
        self.x = int(input('enter the x cord : '))
        self.y = int(input('enter the y cord : '))
        
    def showPoint(self):
        return (f'the x cors is : {self.x} and the y cors is : {self.y}')

class Circle(Point):
    def __init__(self, radius = 0):
        super().__init__()
        self.radius = radius
        
    def getCircle(self):
        print('enter the center of the circle')
        self.getPoint()
        print('enter any point on the circle')
        self.centre = Point()
        self.centre.getPoint()
        self.radius = self.calcRad(self.centre)
        
    def calcRad(self, any):
        return ((self.x - any.x) ** 2 + (self.y - any.y) ** 2) ** 0.5
    
    def calcArea(self):
        return 3.14 * ((self.radius) ** 2)
    
class Cone(Circle):
    def __init__(self, apex = 0):
        super().__init__()
        self.apex = apex
        
    def calcVolume(self):
        print("enter the apex point")
        self.apex = Point()
        self.apex.getPoint()
        self.getCircle()
        a  = self.calcArea()
        self.height = ((self.centre.x - self.apex.x) ** 2 + (self.centre.y - self.apex.y)  ** 2) ** 0.5
        return 1/3 * self.height * a

class Polygon(Point):
    def __init__(self, points_array = [], num_sides = 0):
        self.points_array = points_array
        self.num_sides = num_sides
    
    def get_details(self):
        self.num_sides = int(input("enter the number of sides : "))
        for i in range(self.num_sides):
            p = Point()
            p.getPoint()
            self.points_array.append(p)

class Square(Polygon):
    def __init__(self):
        super().__init__()
        self.get_details()
        self.length = self.calcLength()
        
    def calcLength(self):
        return ((self.points_array[0].x - self.points_array[1].x) ** 2 + (self.points_array[0].y - self.points_array[1].y) ** 2) ** 0.5
    
    def area(self):
        return self.length ** 2
    
    def perimeter(self):
        return self.length * 4
    
if __name__ == '__main__':
    # Create a Point object
    p = Point()
    p.getPoint()
    print(p.showPoint())

    # Create a Circle object
    c = Circle()
    c.getCircle()
    print(f"Radius of the circle: {c.radius}")
    print(f"Area of the circle: {c.calcArea()}")

    # Create a Cone object
    cone = Cone()
    print(cone.calcVolume())

    # Create a Square object
    s = Square()
    print(f"Area of the square: {s.area()}")
    print(f"Perimeter of the square: {s.perimeter()}")
