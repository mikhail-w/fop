class Point:

    def __init__(self, x_coordinate, y_coordinate):
        self.__x_coord = x_coordinate
        self.__y_coord = y_coordinate

    def get_x_coord(self):
        return self.__x_coord

    def get_y_coord(self):
        return self.__y_coord

    def distance_to(self, point_obj):
        distance = (
            (((point_obj.get_x_coord()) - (self.get_x_coord())) ** 2)
            + (((point_obj.get_y_coord()) - (self.get_y_coord())) ** 2)
        ) ** 0.5

        return distance


class LineSegment:
    def __init__(self, point_1, point_2):
        self.__endpoint_1 = point_1
        self.__endpoint_2 = point_2

    def get_endpoint_1(self):
        return self.__endpoint_1

    def get_endpoint_2(self):
        return self.__endpoint_2

    def length(self):
        return self.__endpoint_1.distance_to(self.__endpoint_2)

    def is_parallel_to(self, line_seg):
        slope_1 = self.slope()
        slope_2 = line_seg.slope()
        print(f"Line segment: {slope_1}")
        print(f"Line segment2: {slope_2}")

        return slope_1 == slope_2

    def slope(self):
        return (
            (self.__endpoint_2.get_y_coord()) - (self.__endpoint_1.get_y_coord())
        ) / ((self.__endpoint_2.get_x_coord()) - (self.__endpoint_1.get_x_coord()))


point_1 = Point(7, 4)
point_2 = Point(-6, 18)
# print(f"Distance: {point_1.distance_to(point_2)}")
line_seg_1 = LineSegment(point_1, point_2)
print(f"Length: {line_seg_1.length()}")
print(f"Slope: {line_seg_1.slope()}")

point_3 = Point(-2, 2)
point_4 = Point(24, 12)
line_seg_2 = LineSegment(point_3, point_4)
print(line_seg_1.is_parallel_to(line_seg_2))
