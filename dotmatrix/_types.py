from __future__ import annotations

from typing import Iterable, Protocol, Tuple, TypeVar, Union

V = TypeVar("V")
O = TypeVar("O", covariant=True)

Point = Tuple[int, int]


class UseDefault:
    """Sentinel value type that indicates that the default brush is to be used."""

    @staticmethod
    def resolve(v: Union[V, UseDefault], default: V) -> V:
        """Resolve the given value dispute.

        :param v: given value
        :type v: Union[V, UseDefault]
        :param default: given default
        :type default: V
        :return: the actual value
        :rtype: V
        """
        return default if isinstance(v, UseDefault) else v


USE_DEFAULT = UseDefault()


class Dotted(Protocol):
    """An object that can be drawn on a Matrix."""

    def __dots__(self) -> Iterable[Point]:
        """Generate the pixel positions representing this object.

        :return: pixels to draw
        :rtype: Iterable[Point]
        """


class Display(Protocol[V, O]):
    """An object that can be used as a matrix display."""

    width: int
    height: int
    default_brush: V

    def __init__(
        self, width: int, height: int, *, default_brush: Union[V, UseDefault]
    ) -> None:
        """Initialize a matrix object.

        :param width: width of the matrix
        :type width: int
        :param height: height of the matrix
        :type height: int
        """

    def render(self) -> O:
        """Render the current matrix state.

        :return: render result
        :rtype: O
        """

    def __getitem__(self, pos: Point) -> V:
        """Get the value of a pixel.

        :param pos: position of pixel to get
        :type pos: Point
        :raises IndexError: requested pixel is out of the bounds of the matrix
        :return: state of the pixel
        :rtype: bool
        """

    def __setitem__(self, pos: Point, val: V):
        """Set the value of a pixel.

        :param pos: position of the pixel to set
        :type pos: Point
        :param val: the value to set the pixel to
        :type val: bool
        :raises IndexError: requested pixel is out of the bounds of the matrix
        """
