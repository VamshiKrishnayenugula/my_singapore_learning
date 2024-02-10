#creating a dynamic class using class keyword

class car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_car(self):
        return f'the car is {self.name} and color is {self.color}'
    

obj = car('bmw','red')

print(obj.print_car())