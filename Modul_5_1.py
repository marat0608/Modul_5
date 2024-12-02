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

h1 = House("ЖК Высота", 15)
print(h1.name, h1.numbers_of_floors)
h1.go_to(16)
h1.go_to(10)
h1.go_to(1)
