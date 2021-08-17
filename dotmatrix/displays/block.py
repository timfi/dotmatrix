from array import array
from math import ceil
from typing import List

from .._types import USE_DEFAULT, Point, Union, UseDefault

__all__ = ("Block",)


BLOCKS = (
    "  ",
    "▀ ",
    " ▀",
    "▀▀",
    "▄ ",
    "█ ",
    "▄▀",
    "█▀",
    " ▄",
    "▀▄",
    " █",
    "▀█",
    "▄▄",
    "█▄",
    "▄█",
    "██",
)


class Block:
    """A matrix made up of unicode block characters."""

    __slots__ = (
        "width",
        "_char_width",
        "height",
        "_char_height",
        "default_brush",
        "data",
    )

    def __init__(
        self,
        width: int,
        height: int,
        *,
        default_brush: Union[bool, UseDefault] = USE_DEFAULT,
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
        self._char_width = ceil(width / 2)
        self._char_height = ceil(height / 2)
        # Use array of unsigned chars for easy data integrity.
        self.data = array("B", [0 for _ in range(self._char_height * self._char_width)])

    def render(self) -> str:
        """Render the current matrix state.

        :return: render result
        :rtype: str
        """
        chars = (BLOCKS[0xF & byte] for byte in self.data)
        lines: List[str] = []
        for _ in range(self._char_height):
            line = ""
            for _ in range(self._char_width):
                line += next(chars)
            lines.append(line)
        return "\n".join(lines)

    def _pos_to_idx(self, x: int, y: int) -> tuple[int, int]:
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError(f"Out of bounds: {(x,y)}")
        (cx, dx), (cy, dy) = divmod(x, 2), divmod(y, 2)
        return cx + cy * self._char_width, (dx + dy * 2)

    def __getitem__(self, pos: Point) -> bool:
        """Get the value of a pixel.

        :param pos: position of pixel to get
        :type pos: Point
        :raises IndexError: requested pixel is out of the bounds of the matrix
        :return: state of the pixel
        :rtype: bool
        """
        c, i = self._pos_to_idx(*pos)
        return bool(1 & self.data[c] >> i)

    def __setitem__(self, pos: Point, val: bool):
        """Set the value of a pixel.

        :param pos: position of the pixel to set
        :type pos: Point
        :param val: the value to set the pixel to
        :type val: bool
        :raises IndexError: requested pixel is out of the bounds of the matrix
        """
        c, i = self._pos_to_idx(*pos)
        self.data[c] ^= (-val ^ self.data[c]) & (1 << i)
        self.data[c] &= 0xF
