class Figure:
    def __init__(self, __sides, *__color, filled=True):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        self.sides_count = 0

    def get_color(self):
        return self.__color

    # def set_color(self, r, g, b):
    #     self.r = r
    #     self.g = g
    #     self.b = b
    def __is_valid_color(self, r, g, b):
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_types and valid_values

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r , g, b



    def is_valid_side(self, *sides):
        for i in sides:
            if i > 0 and len(*sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    #def len(self)

    def set_sides(self, *new_sides):
        self.new_sides = new_sides
        if len(new_sides) != self.sides_count:
            self.__sides == self.new_sides


class Circle(Figure):
    def __init__(self, __sides, *__color):
        super().__init__(__sides, __color)
        self.__radius = 3,14 / __sides
        self.sides_count = 1
        super().set_color(r, g, b)

    def get_square(self):
        return 3.14 * self.__radius

circle1 = Circle(10,(200, 200, 100))
circle1.set_color(55, 66, 77)
print(circle1.get_color())





