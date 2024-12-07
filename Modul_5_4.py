class House:
    pass
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors
    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

h1 = House("ЖК Утес", 10)
print(House.houses_history)
h2 = House("ЖК Айсберг", 20)
print(House.houses_history)
h3 = House("ЖК Эльбрус", 20)
print(House.houses_history)

#Удаление объектов
del h2
del h3
print(House.houses_history)