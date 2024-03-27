

class Rectangle():
    def __init__(self, length, height):
        self.length = float(length)
        self.height = float(height)
    
    def basic_info(self):
        print(f"Constructing a rectangle with length: {self.length} and height: {self.height}")
        
    def perimeter_calculation(self):
        perimeter = 2 * (self.length + self.height)
        print(f"The perimeter is: {perimeter} cm")
        
    def area_calculation(self):
        area = (self.length * self.height)
        print(f"The area is: {area} cm^2")
        
    def shorten_length(self):
        shorten_length_by = float(input("Do you wish to shorten the length of the rectangle? By how much?: "))
        self.length = self.length - shorten_length_by
        

rectangle1 = Rectangle(2,4)
rectangle1.basic_info()
rectangle1.perimeter_calculation()
rectangle1.area_calculation()

rectangle1.shorten_length()
print()
rectangle1.perimeter_calculation()
rectangle1.area_calculation()