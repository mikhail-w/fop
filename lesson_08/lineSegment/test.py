class Car:
    def __init__(self, name, color):
        self._name = name
        self.color = color

    def get_name(self):
        return self._name

    def get_color(self):
        return self.color

    def set_color(self, value):
        self.color = value

    def set_name(self, value):
        self.name = value


c1 = Car("BMW", "Red")
c2 = Car("Audi", "Black")

# print(c1.__name)
print(c1.get_name())
c1._name = "Toyota"
print(c1._name)
print(c1.get_name())
