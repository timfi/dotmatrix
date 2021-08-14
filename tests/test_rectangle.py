from random import randrange

from ward import test

from dotcanvas import Canvas


def _test_equiv(
    dim: int,
    x00: int,
    y00: int,
    x10: int,
    y10: int,
    x01: int,
    y01: int,
    x11: int,
    y11: int,
):
    c0 = Canvas(dim, dim)
    c0.rectangle(x00, y00, x10, y10)
    c1 = Canvas(dim, dim)
    c1.rectangle(x01, y01, x11, y11)
    assert c0.data == c1.data


for dim in range(3, 10):
    for _ in range(10):
        x0 = randrange(0, dim // 2)
        y0 = randrange(0, dim // 2)
        x1 = randrange(x0 + 1, dim)
        y1 = randrange(y0 + 1, dim)

        @test(f"Canvas({dim}x{dim}): retangle @ {(x0,y0)}, {(x1,y1)}: checking correctness")  # type: ignore[no-redef]
        def _(dim=dim, x0=x0, y0=y0, x1=x1, y1=y1):
            c = Canvas(dim, dim)
            c.rectangle(x0, y0, x1, y1)
            res = (
                0
                | sum(1 << x for x in range(x0, x1 + 1)) << y0 * dim
                | sum((1 << x0 | 1 << x1) << y * dim for y in range(y0 + 1, y1))
                | sum(1 << x for x in range(x0, x1 + 1)) << y1 * dim
            )
            assert c.data == res

        @test(f"Canvas({dim}x{dim}): retangle @ {(x0,y0)}, {(x1,y1)}: check equivalences")  # type: ignore[no-redef]
        def _(dim=dim, x0=x0, y0=y0, x1=x1, y1=y1):
            _test_equiv(dim, x0, y0, x1, y1, x0, y1, x1, y0)
            _test_equiv(dim, x0, y0, x1, y1, x1, y0, x0, y1)
            _test_equiv(dim, x1, y0, x0, y1, x0, y1, x1, y0)
