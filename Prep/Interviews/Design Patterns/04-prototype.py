from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass


class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        res = self.length
        print(res)
        return res

    def clone(self) -> Shape:
        return Square(self.length)


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        res = self.width
        print(res)
        return res

    def get_height(self) -> int:
        res = self.height
        print(res)
        return res

    def clone(self) -> Shape:
        return Rectangle(self.width, self.height)


class Test:
    def clone_shapes(self, shapes: List[Shape]) -> List[Shape]:
        return [shape.clone() for shape in shapes]


if __name__ == '__main__':
    square = Square(10)  # 10 is the length
    another_square = square.clone()  # Clone with length 10
    print(square == another_square)  # False

    rectangle = Rectangle(10, 20)  # 10 is width, 20 is height
    another_rectangle = rectangle.clone()  # Clone with width 10 and height 20
    print(rectangle == another_rectangle)  # False

    test = Test()
    shapes = [square, rectangle, another_square, another_rectangle]
    cloned_shapes = test.clone_shapes(shapes)

    print(shapes == cloned_shapes)  # False
    print(len(shapes) == len(cloned_shapes))  # True
    print(shapes[0] == cloned_shapes[0])  # False
    print(shapes[0].length == cloned_shapes[0].length)  # True
