class Figure:
    def __init__(self, __sides, __color, filled):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        self.sides_count = 0

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __is_valid_color(self, r, g, b):
        if (r , g, b) >= 0 and (r, g, b) <= 255:
            def set_color(self, r, g, b):
                self.r = r
                self.g = g
                self.b = b
            #self.__color = (r , g, b)

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
    def __init__(self, __sides, __color, filled, __radius):
        super().__init__(__sides, __color, filled)
        self.__radius = __radius
        self.sides_count = 1
        super().set_sides()

    def get_square(self):
        return 3.14 * self.__radius

circle1 = Circle((200, 200, 100), 10)
circle1.set_color(55, 66, 77)
print(circle1.get_color())





