class House:
    houses_history = []

    def __new__(cls, *args): #https://docs.python.org/3/reference/datamodel.html#object.__new__
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def __str__(self):
        return f"Name: {self.name}, number of floors: {self.num_of_floors}"

    def __len__(self):
        return self.num_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.num_of_floors == other.num_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors < other.num_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.num_of_floors <= other.num_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors > other.num_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.num_of_floors >= other.num_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.num_of_floors != other.num_of_floors

    def __del__(self):
        print(f"{self.name} снесен, но отсанется в истории")

    def __add__(self, value):
        if isinstance(value, int):
            self.num_of_floors += value
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            return self + value

    def __radd__(self, value):
        if isinstance(value, int):
            return self + value

    def go_to(self, new_floor):
        if new_floor < self.num_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print("No this floor")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
