# ⣿ dotmatrix
_A dot matrix rendered using braille characters._

[![PyPI](https://img.shields.io/pypi/v/dotmatrix) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dotmatrix)](https://pypi.org/project/dotmatrix/) ![PyPI - License](https://img.shields.io/pypi/l/dotmatrix) [![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Description

This library provides class called `Matrix` which represents a dot matrix that can be rendered to a string of [Braille](https://en.wikipedia.org/wiki/Braille) characters. In addition the class also provides some usefull functions for drawing all kinds of things onto said matrix.
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

## Drawing functions

As of now this library contains the following drawing functions:
- `scatter` – Scatters some points.
- `show` – Draws an object implementing the `Dotted` protocol.
- `line` – Draws a line.
- `chain` – Draws a chain of segments.
- `polygon` – Draws a polygon.
- `rectangle` – Draws an axis aligned rectangle. (from a simplified representation, i.e. from two opposing corners)
- `cricle` – Draws a circle.
- `ellipse` – Draws an axis aligned ellipse.
- `plot` – Plots a series of XY-coordinates. (matplotlib.pyplot style)
- `plotf` – Plots a function.
- `curve` – Draws a [Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve).

Implementing the `Dotted` protocol for any class comes down to adding a `__dots__` function to your class:

```
def __dots__(self) -> Iterable[Tuple[int, int]]:
    """Generate the pixel positions representing this object."""
```

⚠️&nbsp;&nbsp;_The origin or the coordinate system, i.e. `(0, 0)`, is at the top left corner!_


## More examples

### Bézier curves

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

### Function plotting

**Code**

```python
from dotmatrix import Matrix

m = Matrix(64, 64)

m.plotf(
    lambda x: 0.005 * x ** 3,
    range(-31, 31),
    origin=(31,31),
)

print(m.render())
```

**Output**

```
⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⢄⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀
```

## Development

In case you want to add some code to this project your need to first make sure you have [poetry](https://python-poetry.org/) installed. Afterwards you can run the following commands to get your setup up and running:

```sh
poetry install
poetry shell
pre-commit install
```

Due note that you will have to commit from _inside the virtual environment_ or you need to have the dev-tools installed in your local python installation.

All PRs will be style checked with [isort](https://github.com/PyCQA/isort/), [pydocstyle](https://github.com/PyCQA/pydocstyle/) and [black](https://github.com/psf/black) as well as type checked with [mypy](http://www.mypy-lang.org/).
