from ward import test

from dotcanvas import Canvas, __version__
from dotcanvas.canvas import byte_to_braille


@test("test version")  # type: ignore[no-redef]
def _():
    assert __version__ == "0.1.0"
