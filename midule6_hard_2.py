import math

class Figure:
    def __init__(self, __color, *__sides, filled=True):
        self.__sides = list(__sides)
        self.__color = list(__color)
        self.filled = filled
        self.sides_count = 0

    def get_color(self):
        return self.__color


    def __is_valid_color(self, r, g, b):
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_types and valid_values

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r , g, b]



    def __is_valid_side(self, *sides):
        for i in sides:
            if i > 0 and len(*sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def len(self):
        return self.sides_count * self.__sides

    def set_sides(self, *new_sides):
        self.new_sides = list(new_sides)
        #list_sides = []
        if len(new_sides) == self.sides_count:
        #if self.__is_valid_side(sides) and len(new_sides) == self.sides_count:
            #list_sides.append(self.new_sides)
            self.__sides = list(new_sides)



class Circle(Figure):
    def __init__(self, __color, *__sides):
        super().__init__(__color , __sides)
        b = sum(__sides)
        self.__radius = b / 3.14
        self.sides_count = 1
        #super().set_color(r, g, b)
        #super().len()

    def get_square(self):
        return 3.14 * self.__radius



class Triangle(Figure):

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.sides_count = 3
        super().get_sides()


    def get_square(self):
        s = sum(self.get_sides()) / 2
        #area = math.sqrt(s * (s - self.__sides[0]) * (s - self.__sides[1]) *(s - self.__sides[2]))
        area = math.sqrt(s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) *(s - self.get_sides()[2]))
        return area

class Cube(Figure):
    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        #Figure.__init__(self, __color, *__sides)
        self.sides_count = 12
        self.actual_sides = list(__sides) * 12
        #super().get_sides()

    def get_sides(self):
        if len(self.new_sides) == 1:
            return self.actual_sides
        else:
            return self.__sides

    def get_volume(self):
        return self.get_sides()[0] **3
        #return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
circle1.set_color(55, 66, 77)
print(circle1.get_color())

print(circle1.get_square())

circle1.set_sides(15)
print(circle1.get_sides())

#print(len(circle1))
print(circle1.len())

cube1 = Cube((222, 35, 130), 6)
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(8,8,8,8,8,8,8,8,8,8,8,8)
print(cube1.__dict__)
print(cube1.get_sides())

print(cube1.get_volume())

triangle1 = Triangle((34, 200, 45), (23, 23,35))
triangle1.set_color(54, 67,34)
print(triangle1.get_color())

print(triangle1.get_square())
