class Rectangle:

    def __init__(self, x, y, width, heigth):
        self.x = x
       	self.y = y
       	self.width = width
       	self.heigth = heigth

    def get_area(self):
        return print('Rectangle', '\t'.join(map(str,
            [self.x, self.y, self.width, self.heigth])))


rect1 = Rectangle(5, 10, 50, 100)
rect2 = Rectangle(1, 2, 10, 20)
rect1.get_area()
rect2.get_area()
