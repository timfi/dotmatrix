from typing import List

from .._types import USE_DEFAULT, Point, Union, UseDefault

__all__ = ("Unit",)


class Unit:
    """A matrix made up of a pair of characters."""

    __slots__ = (
        "width",
        "height",
        "default_brush",
        "data",
        "chars",
    )

    def __init__(
        self,
        width: int,
        height: int,
        *,
        default_brush: Union[bool, UseDefault] = USE_DEFAULT,
        chars: tuple[str, str] = ("  ", "██"),
    ) -> None:
        """Initialize a matrix object.

        :param width: width of the matrix
        :type width: int
        :param height: height of the matrix
        :type height: int
        """
        self.default_brush = USE_DEFAULT.resolve(default_brush, True)
        self.width = width
        self.height = height
        self.data = 0
        self.chars = chars

    def render(self) -> str:
        """Render the current matrix state.

        :return: render result
        :rtype: str
        """
        data = self.data
        lines: List[str] = []
        for _ in range(self.height):
            line = ""
            for _ in range(self.width):
                line += self.chars[1 & data]
                data >>= 1
            lines.append(line)
        return "\n".join(lines)

    def __getitem__(self, pos: Point) -> bool:
        """Get the value of a pixel.

        :param pos: position of pixel to get
        :type pos: Point
        :raises IndexError: requested pixel is out of the bounds of the matrix
        :return: state of the pixel
        :rtype: bool
        """
        x, y = pos
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError(f"Out of bounds: {(x,y)}")
        return bool(1 & self.data >> x + y * self.width)

    def __setitem__(self, pos: Point, val: bool):
        """Set the value of a pixel.

        :param pos: position of the pixel to set
        :type pos: Point
        :param val: the value to set the pixel to
        :type val: bool
        :raises IndexError: requested pixel is out of the bounds of the matrix
        """
        x, y = pos
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError(f"Out of bounds: {(x,y)}")
        self.data ^= (-val ^ self.data) & (1 << x + y * self.width)
