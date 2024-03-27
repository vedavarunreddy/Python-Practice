
class Vehicle():
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        
    def manufactured_place(self):
        if self.make in ["ford", "chevy", "tesla"]:
            return f"{self.make} -> American Made"
        else:
            return f"{self.make} -> Imported car"
    
    def make_model(self):
        return f"{self.make} {self.model}"
    
    def car_year(self):
        try:
            self.year = int(self.year)
            if self.year > 2000:
                return f"Car from the 21st century -> {self.model}"
            else:
                return f"This is an old car pal -> {self.model}"
        except Exception:
            print(Exception)
            print("You entered a non-integer value for year! ")
            
    def max_price_check(self, max_price):
        if max_price > float(self.price):
            return f"This {self.model} Within the budget"
        else:
            return f"This {self.model} Over budget! by ${float(self.price) - max_price}"
        
car = Vehicle("tesla", "model S", 2020, 8000)
print(car.manufactured_place())
print(car.make_model())
print(car.car_year())
MAX_PRICE = float(input("What is your max price for the car?: "))
print(car.max_price_check(MAX_PRICE))

class Style(Vehicle):
    def __init__(self, make, model, year, price, num_of_doors):
        super().__init__(make, model, year, price)
        self.num_of_doors = num_of_doors
        
    def car_type(self):
        if int(self.num_of_doors) >= 4:
            return f"Family car"
        else:
            return f"Sports car"


print()     

car2 = Style("Ferrari", "420", 1980, 40000, 2)
print(car2.manufactured_place())
print(car2.make_model())
print(car2.car_year())
MAX_PRICE = float(input("What is your max price for the car?: "))
print(car2.max_price_check(MAX_PRICE))
print(car2.car_type())