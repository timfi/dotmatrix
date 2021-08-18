from typing import Iterable, Tuple

from ._types import Point

__all__ = ("de_casteljau", "bresenham_line", "bresenham_circle", "bresenham_ellipse")


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
