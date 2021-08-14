from ward import test

from dotcanvas import Canvas

for dim in range(1, 6):
    # Test horizontal lines
    for y in range(dim):
        for x0 in range(dim):
            for x1 in range(x0, dim):

                @test(f"Canvas({dim}x{dim}): horizontal line @ y={y} ∧ x∈[{x0},{x1})")  # type: ignore[no-redef]
                def _(dim=dim, y=y, x0=x0, x1=x1):
                    c = Canvas(dim, dim)
                    res = sum(1 << x for x in range(x0, x1 + 1)) << dim * y
                    c.line(x0, y, x1, y)
                    assert c.data == res

    # Test vertical lines
    for x in range(dim):
        for y0 in range(dim):
            for y1 in range(y0, dim):

                @test(f"Canvas({dim}x{dim}): vertical line @ x={x} ∧ y∈[{y0},{y1})")  # type: ignore[no-redef]
                def _(dim=dim, x=x, y0=y0, y1=y1):
                    c = Canvas(dim, dim)
                    res = sum(1 << (x + dim * y) for y in range(y0, y1 + 1))
                    c.line(x, y0, x, y1)
                    assert c.data == res

    # Test diagonals
    for i in range(dim):
        for j in range(i, dim, -1):

            @test(f"Canvas({dim}x{dim}): diangonal line @ ({i},{i})-({j},{j})")  # type: ignore[no-redef]
            def _(dim=dim, i=i, j=j):
                c = Canvas(dim, dim)
                res = sum(1 << y + y * dim for y in range(i, j + 1))
                c.line(i, i, j, j)
                assert c.data == res

            @test(f"Canvas({dim}x{dim}): diangonal line @ ({j},{i})-({i},{j})")  # type: ignore[no-redef]
            def _(dim=dim, i=i, j=j):
                c = Canvas(dim, dim)
                res = sum(1 << dim - y - 1 + y * dim for y in range(i, j + 1))
                c.line(j, i, i, j)
                assert c.data == res
