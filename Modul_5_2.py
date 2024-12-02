class House:
    pass
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors
    def go_to(self, new_floors):
        if h1.numbers_of_floors < new_floors or new_floors == 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floors + 1):
                print(i)
    def __str__(self):
        return str(f'Название: {self.name}, Количество этажей: {self.numbers_of_floors}')
    def __len__(self):
        return self.numbers_of_floors

h1 = House("ЖК Высота", 7)
h2 = House("ЖК Акация", 20)
print(h1.name, h1.numbers_of_floors)
h1.go_to(8)
h1.go_to(4)
h1.go_to(1)
print(h1)
print(h2)
print(len(h1))
print(len(h2))