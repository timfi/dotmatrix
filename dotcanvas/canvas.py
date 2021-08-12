from math import ceil

BIT_POS = [0, 3, 1, 4, 2, 5, 6, 7]


def byte_to_braille(byte: int) -> str:
    """Convert a given byte into it's corresponding braille charater.

    The byte will be converted as follows:
                          +-----+
        +----------+      | 0 1 |
        | 76543210 |  ->  | 2 3 |
        +----------+      | 4 5 |
                          | 6 7 |
                          +-----+

    :param byte: the byte to convert
    :type byte: int
    :return: the corresponding braille charater
    :rtype: str
    """
    bits = ([0] * 8 + [*map(int, bin(byte)[2:])])[:-9:-1]
    return chr(0x2800 + sum(b << p for b, p in zip(bits, BIT_POS)))


class Canvas:
    """A canvas made up of braile dots."""

    __slots__ = ("width", "height", "data")

    def __init__(self, width: int, height: int) -> None:
        """Initialize a Canvas Object.

        :param width: width of the canvas
        :type width: int
        :param height: height of the canvas
        :type height: int
        """
        self.width = width
        self.height = height
        self.data = 0

    def __getitem__(self, pos: tuple[int, int]) -> bool:
        """Get the value of a pixel on the canvas.

        :param pos: position of pixel to get
        :type pos: tuple[int, int]
        :raises IndexError: requested pixel is out of the bounds of the canvas
        :return: state of the pixel
        :rtype: bool
        """
        x, y = pos
        if 0 <= x < self.width and 0 <= y < self.height:
            return bool(1 & (self.data >> (self.width * y + x)))
        else:
            raise IndexError(f"Out of bounds: {(x,y)}")

    def __setitem__(self, pos: tuple[int, int], val: bool):
        """Set the value of a pixel on the canvas.

        :param pos: position of the pixel to set
        :type pos: tuple[int, int]
        :param val: the value to set the pixel to
        :type val: bool
        :raises IndexError: requested pixel is out of the bounds of the canvas
        """
        x, y = pos
        if 0 <= x < self.width and 0 <= y < self.height:
            self.data ^= (-val ^ self.data) & (1 << (self.width * y + x))
        else:
            raise IndexError(f"Out of bounds: {(x,y)}")

    def render(self) -> str:
        """Render the current canvas state.

        :return: rendered canvas
        :rtype: str
        """
        char_height = ceil(self.height / 4)
        char_width = ceil(self.width / 2)
        lines = []
        for char_y in range(char_height):
            line = ""
            for char_x in range(char_width):
                byte = sum(
                    (3 & self.data >> (y + char_y * 4) * self.width + char_x * 2)
                    << y * 2
                    for y in range(4)
                )
                line += byte_to_braille(byte)
            lines.append(line)
        return "\n".join(lines)

    def line(self, x0: int, y0: int, x1: int, y1: int):
        """Draw a line on the canvas.

        :param x0: x coordinate of the first point
        :type x0: int
        :param y0: y coordinate of the first point
        :type y0: int
        :param x1: x coordinate of the second point
        :type x1: int
        :param y1: y coordinate of the second point
        :type y1: int
        :raises IndexError: one of requested pixels is out of the bounds of the canvas
        """
        dx, sx = abs(x1 - x0), [-1, 1][x0 < x1]
        dy, sy = -abs(y1 - y0), [-1, 1][y0 < y1]
        err = dx + dy

        while 1:
            self[x0, y0] = True
            if x0 == x1 and y0 == y1:
                break
            e2 = err * 2
            if e2 > dy:
                err += dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def circle(self, x0: int, y0: int, r: int):
        """Draw a circle on the canvase.

        :param x0: x coordinate of the circle's center
        :type x0: int
        :param y0: y coordinate of the circle's center
        :type y0: int
        :param r: radius of the circle
        :type r: int
        :raises IndexError: one of the requested pixels is out of the bounds of the canvas
        """
        f = 1 - r
        ddFx = 0
        ddFy = -2 * r
        x = 0
        y = r

        self[x0, y0 + r] = True
        self[x0, y0 - r] = True
        self[x0 + r, y0] = True
        self[x0 - r, y0] = True

        while x < y:
            if f >= 0:
                y -= 1
                ddFy += 2
                f += ddFy
            x += 1
            ddFx += 2
            f += ddFx + 1

            self[x0 + x, y0 + y] = True
            self[x0 - x, y0 + y] = True
            self[x0 + x, y0 - y] = True
            self[x0 - x, y0 - y] = True
            self[x0 + y, y0 + x] = True
            self[x0 - y, y0 + x] = True
            self[x0 + y, y0 - x] = True
            self[x0 - y, y0 - x] = True

    def ellipse(self, x0: int, y0: int, r1: int, r2: int):
        """Draw an ellipse on the canvas.

        :param x0: x coordinate of the ellipse's center
        :type x0: int
        :param y0: y coordinate of the ellipse's center
        :type y0: int
        :param r1: horizontal radius of the ellipse
        :type r1: int
        :param r2: vertical radius of the ellipse
        :type r2: int
        :raises IndexError: one of requested pixels is out of the bounds of the canvas
        """
        dx, dy = 0, r2
        r12, r22 = r1 * r1, r2 * r2
        err = r22 - (2 * r2 - 1) * r12

        while 1:
            self[x0 + dx, y0 + dy] = True
            self[x0 + dx, y0 - dy] = True
            self[x0 - dx, y0 + dy] = True
            self[x0 - dx, y0 - dy] = True

            e2 = 2 * err
            if e2 < (2 * dx + 1) * r22:
                dx += 1
                err += (2 * dx + 1) * r22
            if e2 > -(2 * dy + 1) * r12:
                dy -= 1
                err -= (2 * dy - 1) * r12

            if dy < 0:
                break

        while dx < r1:
            dx += 1
            self[x0 + dx, y0] = True
            self[x0 - dx, y0] = True

    def rectangle(self, x0: int, y0: int, x1: int, y1: int):
        """Draw a rectangle on the canvas.

        The two given corners must be oposite of one another.

        :param x0: x coordinate of the first corner.
        :type x0: int
        :param y0: y coordinate of the first corner.
        :type y0: int
        :param x1: x coorindate of the last corner.
        :type x1: int
        :param y1: y coorindate of the last corner.
        :type y1: int
        :raises IndexError: one of requested pixels is out of the bounds of the canvas
        """
        self.line(x0, y0, x1, y0)
        self.line(x0, y0, x0, y1)
        self.line(x1, y0, x1, y1)
        self.line(x0, y1, x1, y1)

    def triangle(self, x0: int, y0: int, x1: int, y1: int, x2: int, y2: int):
        """Draw a triangle on the canvas.

        :param x0: x coordinate of the first corner.
        :type x0: int
        :param y0: y coordinate of the first corner.
        :type y0: int
        :param x1: x coordinate of the second corner.
        :type x1: int
        :param y1: y coordinate of the second corner.
        :type y1: int
        :param x2: x coordinate of the third corner.
        :type x2: int
        :param y2: y coordinate of the third corner.
        :type y2: int
        :raises IndexError: one of requested pixels is out of the bounds of the canvas
        """
        self.line(x0, y0, x1, y1)
        self.line(x0, y0, x2, y2)
        self.line(x1, y1, x2, y2)

    @property
    def as_array(self) -> list[list[bool]]:
        """Get pixels of canvas."""
        return [[self[x, y] for x in range(self.width)] for y in range(self.height)]

    def transpose(self):
        """Transpose the canvas."""
        T = [*zip(*self.as_array)]
        self.width, self.height = self.height, self.width
        for y in range(self.height):
            for x in range(self.width):
                self[x, y] = T[y][x]
