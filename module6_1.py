class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal, Plant):
    def eat(self, food):
        if food.name == Fruit.edible:
            print(f'{self.name} съел {food.name}')
        elif food.name == Plant.edible:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False
            Animal.fed = True

class Predator(Animal,Plant):

    # def __init__(self,name):
    #     self.name = name
    def eat(self, food):
        #self.food = food
        if food == Plant.edible:
            print(f'{self.name} съел {food}')
        elif food == Fruit.edible:
            print(f'{self.name} не стал есть {food}')
    alive = False
    fed = True

class Fruit(Plant):
    edible = True

    def __init__(self,name):
        self.name = name

class Flower(Plant):
    edibale = False

    def __init__(self, name):
        self.name = name

a1 = Predator("Волк")
a2 = Mammal("Хатико")
print(a1.name)
print(a2.name)
p1 = Flower('Цветик')
print(p1.name)
p2 = Fruit("Апельсин")
print(p2.name)
print(a1.alive)
print(a1.fed)
a1.eat(p1)
# class Fruit(Plant):
#
# class Flower(Plant):
