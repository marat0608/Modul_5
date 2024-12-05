class House:
    pass
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floors):
        if self.numbers_of_floors < new_floors or new_floors < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floors + 1):
                print(i)

h1 = House("ЖК Высота", 4)
print(h1.name, h1.numbers_of_floors)
h2 = House("ЖК Айсберг", 6)
print(h2.name, h2.numbers_of_floors)
h1.go_to(9)
h1.go_to(2)
h1.go_to(1)
h2.go_to(6)
h2.go_to(7)
h2.go_to(-1)