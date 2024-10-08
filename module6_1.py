class Animal:
    # alive = True
    # fed = False

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    # edible = False

    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Fruit(Plant):
    def __init__(self, name):
        #self.name = name
        super().__init__(name)
        self.edible = True


class Flower(Plant):
    pass


a1 = Predator("Волк с Уолл Стрит")
a2 = Mammal("Хатико")
print(a1.name)
print(a2.name)
p1 = Flower('Цветик семицветик')
print(p1.name)
p2 = Fruit("Заводной апельсин")
print(p2.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
