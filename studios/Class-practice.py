class Rectangle():
    '''Rectangle class takes two ints (width and length)'''
    
    def __init__(self, width = 5, length = 5):
        self.width = width
        self.length = length
        
    def __str__(self):
        print("I'm a rectangle.  My length is {} and width is {}".format(self.width, self.length))
    
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return self.width * 2 + self.length * 2
    
    def is_smaller(self, rect):
        return self.area() < rect.area()
    
    def is_square(self):
        return self.width == self.length
        
        
my_rectangle = Rectangle(12,5)
my_other_rectangle = Rectangle(6,4)
print(my_rectangle)