# ⣿ dotmatrix
_A dot matrix rendered using braille characters._

[![PyPI](https://img.shields.io/pypi/v/dotmatrix)](https://pypi.org/project/dotmatrix/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dotmatrix)](https://pypi.org/project/dotmatrix/)
[![PyPI - License](https://img.shields.io/pypi/l/dotmatrix)](https://pypi.org/project/dotmatrix/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Description

This library provides class called `Matrix` which represents a dot matrix that can be rendered to a string of [Braille](https://en.wikipedia.org/wiki/Braille) [characters](https://en.wikipedia.org/wiki/Braille_Patterns). In addition the class also provides some usefull functions for drawing all kinds of things onto said matrix.

### A word on fonts...

This heavily relies on the font you want display the resulting characters with. Some "monospace" fonts/systems **dot not** treat **all** characters as having the same width! In particular this affects the [blank braille character](https://en.wikipedia.org/wiki/Braille_pattern_dots-0) (this: `⠀`). The system that causes the most problems seems to be Windows while both mac OS and your average linux distribution don't screw it up. If you are having problems with the images in this readme you can have a look at the images included in the spoilers.

## Install

Use can install this library from [PyPI](https://pypi.org/project/dotmatrix/):

```sh
pip install dotmatrix
```

### Example

**Code**

```python
from dotmatrix import Matrix

m = Matrix(64, 64)

m.rectangle((0, 0), (63, 63))
m.circle((31, 31), 31)

print(m.render())
```

**Output**

```
⡏⠉⠉⠉⠉⠉⠉⠉⢉⡩⠭⠛⠛⠉⠉⠉⠉⠉⠙⠛⠫⠭⣉⠉⠉⠉⠉⠉⠉⠉⠉⢹
⡇⠀⠀⠀⠀⢀⡠⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⣀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⢸
⡇⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⢸
⡇⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⢸
⣧⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⢸
⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣼
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢹
⡏⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⢸
⡇⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⢸
⡇⠀⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⢸
⡇⠀⠀⠀⠑⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠁⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠈⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠊⠀⠀⠀⠀⠀⠀⢸
⣇⣀⣀⣀⣀⣀⣀⣀⣀⣈⣉⣒⣒⣤⣤⣤⣤⣤⣔⣒⣊⣉⣀⣀⣀⣀⣀⣀⣀⣀⣀⣸
```

<details><summary>image</summary>

This is what it should look like:

![](https://github.com/timfi/dotmatrix/blob/root/.resources/img/basic_example.png)
</details>

## Drawing functions

As of now this library contains the following drawing functions:
- `scatter` – Draws some points.
- `iscatter` – Draws some points (from an iterator).
- `show` – Draws an object implementing the `Dotted` protocol.
- `line` – Draws a line.
- `chain` – Draws a chain of segments.
- `polygon` – Draws a polygon.
- `rectangle` – Draws an axis aligned rectangle. (from two opposing corners)
- `cricle` – Draws a circle.
- `ellipse` – Draws an axis aligned ellipse.
- `curve` – Draws a [Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve).
- `plot` – Plots a series of XY-coordinates. (matplotlib.pyplot style)
- `plotf` – Plots a function.

<details><summary>Dotted protocol</summary>

---
```python
class Dotted(Protocol):
    """An object that can be drawn on a Matrix."""

    def __dots__(self) -> Iterable[Point]:
        """Generate the pixel positions representing this object.

        :return: pixels to draw
        :rtype: Iterable[Point]
        """
```
---
</details>

⚠️  _The origin of the coordinate system, i.e. `(0, 0)`, is at the top left corner!_


## Does it need to be Braille characters?

No, no it does not. It's just the default; you are free to choose how you want to render things. To facilitate this any given `Matrix` object internally makes use of an object implementing the `Display` protocol. For example this library implements, next to the `Braille` displays, some more display like `Block` or `Unit`.

<details><summary>Display protocol</summary>

---
```python
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
```
---
</details>
<details><summary>Block display</summary>

---
**Code**

```python
from dotmatrix import Matrix
from dotmatrix.displays import Block

# Using a different display is as simple as passing it
# into the display-argument of the initializer.
m = Matrix(16, 16, display=Block)

m.rectangle((0, 0), (15, 15))
m.circle((7, 7), 7)

print(m.render())
```

**Output**

```
█▀▀██▀▀▀▀▀██▀▀▀█
█▄▀         ▀▄ █
█▀           ▀▄█
█             ██
█             ██
██           █ █
█ ▀▄▄     ▄▄▀  █
█▄▄▄▄█████▄▄▄▄▄█
```

---
</details>
<details><summary>Unit display</summary>

---
**Code**

```python
from dotmatrix import Matrix
from dotmatrix.displays import Block

# The following isn't required for using the Unit display.
# It's just here to demonstrate that you "pre-instantiate"
# a display and construct a Matrix object from it using
# Matrix.from_display.
d = Unit(16, 16, chars=["  ", "##"])
m = Matrix.from_display(d)

m.curve((0, 0), (15, 0), (0, 15), (15, 15))

print(m.render())
```

**Output**

```
########
        ####
            ##
              ##
              ##
              ##
              ##
              ##
                ##
                ##
                ##
                ##
                ##
                  ##
                    ##
                      ##########
```

---
</details>

## More examples

<details><summary>Bézier flower</summary>

---
**Code**

```python
from dotmatrix import Matrix

m = Matrix(64, 64)

m.curve((0, 0), (63, 0), (0, 63), (63, 63))
m.curve((0, 0), (0, 63), (63, 0), (63, 63))
m.curve((63, 0), (0, 0), (63, 63), (0, 63))
m.curve((63, 0), (63, 63), (0, 0), (0, 63))

print(m.render())
```

**Output**

```
⡏⠉⠉⠉⠉⠒⠒⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠤⠒⠒⠉⠉⠉⠉⢹
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⢄⠀⠀⠀⠀⠀⠀⡠⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡄⠀⠀⢠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜
⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃
⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀
⠀⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀
⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠢⠤⢄⣀⣀⣀⣀⣀⣀⣸⣇⣀⣀⣀⣀⣀⣀⡠⠤⠔⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⠤⠒⠒⠉⠉⠉⠉⠉⠉⢹⡏⠉⠉⠉⠉⠉⠉⠒⠒⠤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀
⠀⢀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀
⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀
⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆
⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⠘⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠑⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⣇⣀⣀⣀⣀⠤⠤⠔⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠢⠤⠤⣀⣀⣀⣀⣸
```

<details><summary>image</summary>

This is what it should look like:

![](https://github.com/timfi/dotmatrix/blob/root/.resources/img/bezier_flower.png)
</details>

---
</details>

<details><summary>Function plotting</summary>

---
**Code**

```python
from dotmatrix import Matrix

m = Matrix(64, 64)

m.rectangle((0, 0), (63, 63))
m.plotf(
    lambda x: 0.005 * x ** 3,
    range(-31, 31),
    origin=(31,31),
)

print(m.render())
```

**Output**

```
⡏⠉⠉⠉⠉⠉⢹⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹
⡇⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⢄⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⢸
⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣸⣀⣀⣀⣀⣀⣀⣸
```

<details><summary>image</summary>

This is what it should look like:

![](https://github.com/timfi/dotmatrix/blob/root/.resources/img/plotting.png)
</details>

---
</details>

## Development

In case you want to add some code to this project your need to first make sure you have [poetry](https://python-poetry.org/) installed. Afterwards you can run the following commands to get your setup up and running:

```sh
poetry install
poetry shell
pre-commit install
```

Due note that you will have to commit from _inside the virtual environment_ or you need to have the dev-tools installed in your local python installation.

All PRs will be style checked with [isort](https://github.com/PyCQA/isort/), [pydocstyle](https://github.com/PyCQA/pydocstyle/) and [black](https://github.com/psf/black) as well as type checked with [mypy](http://www.mypy-lang.org/). In addition to this all PRs should target the `dev`-branch and contain as many signed commits as possible (better yet _only_ signed commits 😉 ). If you have no clue how or why to sign your commits have a look at the [GitHub docs](https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification) on this topic.
