from array import array
from math import ceil
from typing import Callable, Iterable, Protocol, Sequence, Tuple, TypeVar, Union

T = TypeVar("T")
S = TypeVar("S")


Point = Tuple[int, int]
PointF = Tuple[float, float]


class Dotted(Protocol):
    """An object that can be drawn on a Matrix."""

    def __dots__(self) -> Iterable[Point]:
        """Generate the pixel positions representing this object.

        :return: pixels to draw
        :rtype: Iterable[Point]
        """


# Position of each bit in braille character, in logical order...
BIT_POS = [0, 3, 1, 4, 2, 5, 6, 7]


class Matrix:
    """A matrix made up of braile dots."""

    __slots__ = ("width", "_char_width", "height", "_char_height", "data")

    def __init__(self, width: int, height: int) -> None:
        """Initialize a matrix object.

        :param width: width of the matrix
        :type width: int
        :param height: height of the matrix
        :type height: int
        """
        self.width = width
        self.height = height
        self._char_width = ceil(width / 2)
        self._char_height = ceil(height / 4)
        # Use array of unsigned chars for easy data integrity.
        self.data = array("B", [0 for _ in range(self._char_height * self._char_width)])

    def render(self) -> str:
        """Render the current matrix state.

        :return: render result
        :rtype: str
        """
        chars = (chr(0x2800 | byte) for byte in self.data)
        lines: list[str] = []
        for _ in range(self._char_height):
            line = ""
            for _ in range(self._char_width):
                line += next(chars)
            lines.append(line)
        return "\n".join(lines)

    def _pos_to_idx(self, x: int, y: int) -> Point:
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError(f"Out of bounds: {(x,y)}")
        (cx, dx), (cy, dy) = divmod(x, 2), divmod(y, 4)
        return cx + cy * self._char_width, BIT_POS[dx + dy * 2]

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

    def set(self, x: int, y: int, val: bool):
        """Set the value of a pixel.

        Doesn't fail on out of bounds!

        :param x: x coordinate of the pixel
        :type x: int
        :param y: y coordinate of the pixel
        :type y: int
        :param val: the value to set the pixel to
        :type val: bool
        """
        try:
            self[x, y] = True
        except IndexError:
            ...

    def get(self, x: int, y: int, *, default: T = None) -> Union[bool, T]:
        """Set the value of a pixel.

        Doesn't fail on out of bounds!

        :param x: x coordinate of the pixel
        :type x: int
        :param y: y coordinate of the pixel
        :type y: int
        :param default: value to default to upon out of bounds, defaults to None
        :type default: T, optional
        :return: the value of the pixel (if exists)
        :rtype: Union[bool, T]
        """
        try:
            return self[x, y]
        except IndexError:
            return default  # type: ignore

    def scatter(self, *ps: Point, brush: bool = True):
        """Scatter points.

        :param *ps: points to scatter on the canvas
        :type ps: Point
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        """
        for x, y in ps:
            self.set(x, y, brush)

    def show(self, obj: Dotted, at: Point = (0, 0), *, brush: bool = True):
        """Draw an object implementing the Dotted protocol.

        :param obj: the object to draw
        :type obj: Dotted
        :param at: the position to draw the object at, defaults to (0, 0)
        :type at: Point, optional
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        """
        x0, y0 = at
        self.scatter(*((x0 + x, y0 + y) for x, y in obj.__dots__()), brush=brush)

    def line(self, p0: Point, p1: Point, *, brush: bool = True):
        """Draw a line.

        :param p0: coordinates of the first point
        :type p0: Point
        :param p1: coordinates of the second point
        :type p1: Point
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        :raises IndexError: one of requested pixels is out of the bounds of the matrix
        """
        (x0, y0), (x1, y1) = p0, p1
        dx, sx = abs(x1 - x0), [-1, 1][x0 < x1]
        dy, sy = -abs(y1 - y0), [-1, 1][y0 < y1]
        err = dx + dy

        while 1:
            self.set(x0, y0, brush)
            if x0 == x1 and y0 == y1:
                break
            e2 = err * 2
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def chain(self, *ps: Point, brush: bool = True):
        """Draw a chain of segments.

        :param *ps: points defining the segements
        :type ps: Point
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        """
        for seg in zip(ps[:-1], ps[1:]):
            self.line(*seg, brush=brush)

    def polygon(self, *ps: Point, brush: bool = True):
        """Draw a polygon.

        :param *ps: in order points of the polygon
        :type ps: Point
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        """
        for ps in zip(ps, [ps[-1], *ps[:-1]]):
            self.line(*ps, brush=brush)

    def rectangle(self, c0: Point, c1: Point, *, brush: bool = True):
        """Draw a rectangle.

        The two given corners must be opposite of one another.

        :param c0: coordinates of the first corner.
        :type c0: Point
        :param c1: coordinates of the second corner.
        :type c1: Point
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        """
        (x0, y0), (x1, y1) = c0, c1
        self.polygon(c0, (x1, y0), c1, (x0, y1), brush=brush)

    def circle(self, c: Point, r: int, *, brush: bool = True):
        """Draw a circlee.

        :param c: coordinates of the circle's center
        :type c: Point
        :param r: radius of the circle
        :type r: int
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        :raises IndexError: one of the requested pixels is out of the bounds of the matrix
        """
        x0, y0 = c
        f, ddFx, ddFy = 1 - r, 0, -2 * r
        x, y = 0, r

        self.scatter(
            (x0, y0 + r), (x0, y0 - r), (x0 + r, y0), (x0 - r, y0), brush=brush
        )

        while x < y:
            if f >= 0:
                y -= 1
                ddFy += 2
                f += ddFy
            x += 1
            ddFx += 2
            f += ddFx + 1

            self.scatter(
                (x0 + x, y0 + y),
                (x0 - x, y0 + y),
                (x0 + x, y0 - y),
                (x0 - x, y0 - y),
                (x0 + y, y0 + x),
                (x0 - y, y0 + x),
                (x0 + y, y0 - x),
                (x0 - y, y0 - x),
                brush=brush,
            )

    def ellipse(self, c: Point, r1: int, r2: int, *, brush: bool = True):
        """Draw an ellipse.

        :param c: x coordinate of the ellipse's center
        :type c: Point
        :param r1: horizontal radius of the ellipse
        :type r1: int
        :param r2: vertical radius of the ellipse
        :type r2: int
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        :raises IndexError: one of requested pixels is out of the bounds of the matrix
        """
        x0, y0 = c
        dx, dy = 0, r2
        r12, r22 = r1 * r1, r2 * r2
        err = r22 - (2 * r2 - 1) * r12

        while 1:
            self.scatter(
                (x0 + dx, y0 + dy),
                (x0 + dx, y0 - dy),
                (x0 - dx, y0 + dy),
                (x0 - dx, y0 - dy),
                brush=brush,
            )

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
            self.scatter((x0 + dx, y0), (x0 - dx, y0), brush=brush)

    def plot(self, xs: Sequence[int], ys: Sequence[int], *, brush: bool = True):
        """Plot a series of XY-coordinates.

        :param xs: x coordinates to plot
        :type xs: Sequence[int]
        :param ys: y coordinates to plot
        :type ys: Sequence[int]
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        """
        self.chain(*zip(xs, ys), brush=brush)

    def plotf(
        self,
        f: Callable[[T], S],
        xs: Iterable[T],
        *,
        origin: Point = (0, 0),
        to_x: Callable[[T], int] = round,  # type: ignore
        to_y: Callable[[S], int] = round,  # type: ignore
        transpose: bool = False,
        brush: bool = True,
    ):
        """Plot a function.

        :param f: function to plot
        :type f: Callable[[T], S]
        :param xs: function inputs
        :type xs: Iterable[T]
        :param origin: origin to center the plot around, defaults to (0, 0)
        :type origin: Point, optional
        :param to_x: x-coordinate transformation/cast, defaults to `round`
        :type to_x: Callable[[T], int], optional
        :param to_y: y-coordinate transformation/cast, defaults to `round`
        :type to_y: Callable[[S], int], optional
        :param transpose: transpose plot, defaults to False
        :type transpose: bool, optional
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        """
        x0, y0 = origin
        coords = [x0 + to_x(x) for x in xs], [y0 + to_y(f(x)) for x in xs]
        self.plot(*coords[:: 1 - 2 * transpose], brush=brush)

    def curve(
        self,
        *ps: Point,
        steps: int = 0,
        brush: bool = True,
    ):
        """Draw a Bezier curve.

        :param *ps: control points of the curve
        :type ps: Point
        :param steps: amount steps to take, defaults to a sensible amount
        :type steps: int, optional
        :raises ValueError: raised if to few points are given to define a curve
        :param brush: value to set the pixels to, defaults to True
        :type brush: bool, optional
        """
        if len(ps) < 2:
            raise ValueError("Need at least two points to define a curve.")
        else:
            if steps <= 0:
                max_segments_lengths = (
                    max(abs(x0 - x1), abs(y0 - y1))
                    for (x0, y0), (x1, y1) in zip(ps, [ps[-1], *ps[:-1]])
                )
                steps = sum(max_segments_lengths) // 4
            intermediates = (
                (round(x), round(y))
                for i in range(steps)
                for x, y in [de_casteljau(i / steps, ps)]
            )
            self.chain(ps[0], *intermediates, ps[-1], brush=brush)


def de_casteljau(t: float, ps: Iterable[Tuple[float, float]]) -> Tuple[float, float]:
    """De Casteljau's algorithm.

    :param t: Position to determin the point for
    :type t: float
    :param ps: Controll points
    :type ps: Iterable[Tuple[float, float]]
    :return: Final point at position t
    :rtype: Tuple[float, float]
    """
    beta = [*ps]
    n = len(beta)
    for j in range(1, n):
        for k in range(n - j):
            x0, y0 = beta[k]
            x1, y1 = beta[k + 1]
            beta[k] = (x0 * (1 - t) + x1 * t, y0 * (1 - t) + y1 * t)
    return beta[0]
