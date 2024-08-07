class Square:
    def __init__(self, side_length=0.0):
        self.side_length = side_length

    def get_side_length(self) -> float:
        return self.side_length


class SquareHole:
    def __init__(self, sideLength: float):
        self.side_length = sideLength

    def can_fit(self, square: Square):
        return self.side_length >= square.get_side_length()


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self):
        return self.radius


class CircleToSquareAdapter(Square):
    def __init__(self, circle: Circle):
        self.circle = circle

    def get_side_length(self) -> float:
        return 2 * self.circle.get_radius()


if __name__ == '__main__':
    print('##### Test 1 #####')
    square_hole = SquareHole(5)

    square = Square(5)
    print(square_hole.can_fit(square))  # True

    circle = Circle(5)
    circle_adapter = CircleToSquareAdapter(circle)
    print(square_hole.can_fit(circle_adapter))  # False

    print('\n##### Test 2 #####')
    square_hole = SquareHole(5)

    square = Square(6)
    print(square_hole.can_fit(square))  # False

    circle = Circle(2)
    circle_adapter = CircleToSquareAdapter(circle)
    print(square_hole.can_fit(circle_adapter))  # True
