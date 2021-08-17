from __future__ import annotations

from typing import (
    Callable,
    Generic,
    Iterable,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
)

from ._types import USE_DEFAULT, Display, Dotted, Point, UseDefault
from .display import BrailleDisplay

__all__ = ("Matrix",)


T = TypeVar("T")
S = TypeVar("S")
V = TypeVar("V")
O = TypeVar("O")


class Matrix(Generic[V, O]):
    """The matrix base class."""

    display: Display[V, O]

    def __init__(
        self,
        width: int,
        height: int,
        *,
        default_brush: Union[V, UseDefault] = USE_DEFAULT,
        display: Union[Display[V, O], Type[Display[V, O]]] = BrailleDisplay,  # type: ignore
    ) -> None:
        """Initialize a matrix object.

        :param width: width of the matrix
        :type width: int
        :param height: height of the matrix
        :type height: int
        """
        if isinstance(display, type):
            self.display = display(width, height, default_brush=default_brush)
        elif width == display.width and height == display.height:
            self.display = display
            self.display.default_brush = USE_DEFAULT.resolve(
                default_brush, display.default_brush
            )
        else:
            raise ValueError(
                "Dimensions of display don't match the given matrix dimensions.\n"
                "Try using Matrix.from_display to construct a matrix for a given display."
            )

    @classmethod
    def from_display(cls, display: Display[V, O]) -> Matrix[V, O]:
        """Create a matrix for a given display.

        :param display: the display to create the matrix for
        :type display: Display[V, O]
        :return: a matrix matching the display
        :rtype: Matrix[V, O]
        """
        return cls(display.width, display.height, display=display)

    def render(self) -> O:
        """Render the current matrix state.

        :return: render result
        :rtype: O
        """
        return self.display.render()

    def __getitem__(self, pos: Point) -> V:
        """Get the value of a pixel.

        :param pos: position of pixel to get
        :type pos: Point
        :raises IndexError: requested pixel is out of the bounds of the matrix
        :return: state of the pixel
        :rtype: V
        """
        return self.display[pos]

    def __setitem__(self, pos: Point, val: V):
        """Set the value of a pixel.

        :param pos: position of the pixel to set
        :type pos: Point
        :param val: the value to set the pixel to
        :type val: V
        :raises IndexError: requested pixel is out of the bounds of the matrix
        """
        self.display[pos] = val

    def set(self, x: int, y: int, val: Union[V, UseDefault]):
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
            self[x, y] = (
                self.display.default_brush if val is USE_DEFAULT else cast(V, val)
            )
        except IndexError:
            ...

    def get(self, x: int, y: int, *, default: T = None) -> Union[V, T]:
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

    def scatter(self, *ps: Point, brush: Union[V, UseDefault] = USE_DEFAULT):
        """Scatter points.

        :param *ps: points to scatter on the canvas
        :type ps: Point
        :param brush: value to set the pixels to
        :type brush: V, optional
        """
        self.iscatter(ps, brush=brush)

    def iscatter(self, ps: Iterable[Point], brush: Union[V, UseDefault] = USE_DEFAULT):
        """Scatter points from an iterator.

        :param ps: points to scatter on the canvas
        :type ps: Iterable[Point]
        :param brush: value to set the pixels to
        :type brush: V, optional
        """
        for x, y in ps:
            self.set(x, y, brush)

    def show(
        self,
        obj: Dotted,
        at: Point = (0, 0),
        *,
        brush: Union[V, UseDefault] = USE_DEFAULT,
    ):
        """Draw an object implementing the Dotted protocol.

        :param obj: the object to draw
        :type obj: Dotted
        :param at: the position to draw the object at, defaults to (0, 0)
        :type at: Point, optional
        :param brush: value to set the pixels to
        :type brush: V, optional
        """
        x0, y0 = at
        self.iscatter(((x0 + x, y0 + y) for x, y in obj.__dots__()), brush=brush)

    def line(self, p0: Point, p1: Point, *, brush: Union[V, UseDefault] = USE_DEFAULT):
        """Draw a line.

        :param p0: coordinates of the first point
        :type p0: Point
        :param p1: coordinates of the second point
        :type p1: Point
        :param brush: value to set the pixels to
        :type brush: V, optional
        :raises IndexError: one of requested pixels is out of the bounds of the matrix
        """
        self.iscatter(bresenham_line(p0, p1), brush=brush)

    def circle(self, c: Point, r: int, *, brush: Union[V, UseDefault] = USE_DEFAULT):
        """Draw a circlee.

        :param c: coordinates of the circle's center
        :type c: Point
        :param r: radius of the circle
        :type r: int
        :param brush: value to set the pixels to
        :type brush: V, optional
        :raises IndexError: one of the requested pixels is out of the bounds of the matrix
        """
        self.iscatter(bresenham_circle(c, r), brush=brush)

    def ellipse(
        self, c: Point, r1: int, r2: int, *, brush: Union[V, UseDefault] = USE_DEFAULT
    ):
        """Draw an ellipse.

        :param c: x coordinate of the ellipse's center
        :type c: Point
        :param r1: horizontal radius of the ellipse
        :type r1: int
        :param r2: vertical radius of the ellipse
        :type r2: int
        :param brush: value to set the pixels to
        :type brush: V, optional
        :raises IndexError: one of requested pixels is out of the bounds of the matrix
        """
        self.iscatter(bresenham_ellipse(c, r1, r2), brush=brush)

    def chain(self, *ps: Point, brush: Union[V, UseDefault] = USE_DEFAULT):
        """Draw a chain of segments.

        :param *ps: points defining the segements
        :type ps: Point
        :param brush: value to set the pixels to
        :type brush: V, optional
        """
        for seg in zip(ps[:-1], ps[1:]):
            self.line(*seg, brush=brush)

    def polygon(self, *ps: Point, brush: Union[V, UseDefault] = USE_DEFAULT):
        """Draw a polygon.

        :param *ps: in order points of the polygon
        :type ps: Point
        :param brush: value to set the pixels to
        :type brush: V, optional
        """
        for ps in zip(ps, [ps[-1], *ps[:-1]]):
            self.line(*ps, brush=brush)

    def rectangle(
        self, c0: Point, c1: Point, *, brush: Union[V, UseDefault] = USE_DEFAULT
    ):
        """Draw a rectangle.

        The two given corners must be opposite of one another.

        :param c0: coordinates of the first corner.
        :type c0: Point
        :param c1: coordinates of the second corner.
        :type c1: Point
        :param brush: value to set the pixels to
        :type brush: V, optional
        """
        (x0, y0), (x1, y1) = c0, c1
        self.polygon(c0, (x1, y0), c1, (x0, y1), brush=brush)

    def plot(
        self,
        xs: Sequence[int],
        ys: Sequence[int],
        *,
        brush: Union[V, UseDefault] = USE_DEFAULT,
    ):
        """Plot a series of XY-coordinates.

        :param xs: x coordinates to plot
        :type xs: Sequence[int]
        :param ys: y coordinates to plot
        :type ys: Sequence[int]
        :param brush: value to set the pixels to
        :type brush: V, optional
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
        brush: Union[V, UseDefault] = USE_DEFAULT,
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
        :param brush: value to set the pixels to
        :type brush: V, optional
        """
        x0, y0 = origin
        coords = [x0 + to_x(x) for x in xs], [y0 + to_y(f(x)) for x in xs]
        self.plot(*coords[:: 1 - 2 * transpose], brush=brush)

    def curve(
        self,
        *ps: Point,
        steps: int = 0,
        brush: Union[V, UseDefault] = USE_DEFAULT,
    ):
        """Draw a Bezier curve.

        :param *ps: control points of the curve
        :type ps: Point
        :param steps: amount steps to take, defaults to a sensible amount
        :type steps: int, optional
        :raises ValueError: raised if to few points are given to define a curve
        :param brush: value to set the pixels to
        :type brush: V, optional
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


def bresenham_line(p0: Point, p1: Point) -> Iterable[Point]:
    """Bresenham's line drawing algorithm.

    :param p0: coordinates of the first point
    :type p0: Point
    :param p1: coordinates of the second point
    :type p1: Point
    :yield: points on the line
    :rtype: Point
    """
    (x0, y0), (x1, y1) = p0, p1
    dx, sx = abs(x1 - x0), [-1, 1][x0 < x1]
    dy, sy = -abs(y1 - y0), [-1, 1][y0 < y1]
    err = dx + dy

    while 1:
        yield (x0, y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


def bresenham_circle(c: Point, r: int) -> Iterable[Point]:
    """Bresenham's circle drawing algorithm.

    :param c: coordinates of the circle's center
    :type c: Point
    :param r: radius of the circle
    :type r: int
    :yield: points on the circle
    :rtype: Point
    """
    x0, y0 = c
    f, ddFx, ddFy = 1 - r, 0, -2 * r
    x, y = 0, r

    yield from ((x0, y0 + r), (x0, y0 - r), (x0 + r, y0), (x0 - r, y0))

    while x < y:
        if f >= 0:
            y -= 1
            ddFy += 2
            f += ddFy
        x += 1
        ddFx += 2
        f += ddFx + 1

        yield from (
            (x0 + x, y0 + y),
            (x0 - x, y0 + y),
            (x0 + x, y0 - y),
            (x0 - x, y0 - y),
            (x0 + y, y0 + x),
            (x0 - y, y0 + x),
            (x0 + y, y0 - x),
            (x0 - y, y0 - x),
        )


def bresenham_ellipse(c: Point, r1: int, r2: int) -> Iterable[Point]:
    """Bresenham's ellipse drawing algorithm.

    :param c: x coordinate of the ellipse's center
    :type c: Point
    :param r1: horizontal radius of the ellipse
    :type r1: int
    :param r2: vertical radius of the ellipse
    :type r2: int
    :yield: points on the ellipse
    :rtype: Point
    """
    x0, y0 = c
    dx, dy = 0, r2
    r12, r22 = r1 * r1, r2 * r2
    err = r22 - (2 * r2 - 1) * r12

    while 1:
        yield from (
            (x0 + dx, y0 + dy),
            (x0 + dx, y0 - dy),
            (x0 - dx, y0 + dy),
            (x0 - dx, y0 - dy),
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
        yield from ((x0 + dx, y0), (x0 - dx, y0))
