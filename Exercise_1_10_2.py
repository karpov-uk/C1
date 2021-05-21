class Rectangle:

    def __init__(self, width, heigth):
       	self.width = width
       	self.heigth = heigth

    def get_area(self):
        return self.width * self.heigth


rect1 = Rectangle(5, 10)
rect2 = Rectangle(10, 20)

print(rect1.width, rect1.heigth, rect1.get_area())
print(rect2.width, rect2.heigth, rect2.get_area())