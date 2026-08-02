class Rectangle:

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: float) -> None:
        self.width = width

    def set_height(self, height: float) -> None:
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape: "Rectangle") -> int:
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):

    def __init__(self, side: float):
        super().__init__(side, side)

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    def set_side(self, side: float) -> None:
        self.width = side
        self.height = side

    def set_width(self, width: float) -> None:
        self.set_side(width)

    def set_height(self, height: float) -> None:
        self.set_side(height)
