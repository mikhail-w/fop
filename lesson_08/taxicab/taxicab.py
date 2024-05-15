class Taxicab:
    def __init__(self, x, y, od=50):
        # private data members
        self.__x_coord = x
        self.__y_coord = y
        self.__odometer = od

    def get_x_coord(self):
        return self.__x_coord

    def get_y_coord(self):
        return self.__y_coord

    def get_odometer(self):
        return self.__odometer

    def move_x(self, x):
        self.__x_coord += x
        self.__odometer += abs(x)

    def move_y(self, y):
        self.__y_coord += y
        self.__odometer += abs(y)

    def show_coords(self):
        print(f"Coordinates: ({self.__x_coord}, {self.__y_coord})")


# a = Taxicab(5, -8)
# a.move_x(3)
# a.move_y(-4)
# a.move_x(-1)
# print(f"Odometer reading: {a.get_odometer()}")
# a.show_coords()

b = Taxicab(10, 23)
print(f"Odometer reading: {b.get_odometer()}")
