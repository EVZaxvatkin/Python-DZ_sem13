from exception import MinsideError


class Rectangle:
    def __init__(self, a: int, b: int):
        if a > 0:
            self.a = a
        else:
            raise MinsideError(a, 0)

        if b > 0:
            self.b = b
        else:
            raise MinsideError(b, 0)

        self.b = b if b is not None else a

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

if __name__ == "__main__":
    TEXT = f"Введите длинну стороны прямоугольника "
    try:
        a = int(input(TEXT + "№1: "))
        b = int(input(TEXT + "№2: "))

    except ValueError as v:
        print(f"Нужно задать число: {v}")

    r = Rectangle(a, b)

    rect = Rectangle(a, b)
    print(f'{rect.perimeter()= } {rect.area()= }')