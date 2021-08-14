from ward import raises, test

from dotcanvas.canvas import Canvas

c = Canvas(1, 1)


@test("setting a value")  # type: ignore[no-redef]
def _():
    # 0 -> 1
    c[0, 0] = 1
    assert c.data == 1
    # 1 -> 1
    c[0, 0] = 1
    assert c.data == 1
    # 1 -> 0
    c[0, 0] = 0
    assert c.data == 0
    # 0 -> 0
    c[0, 0] = 0
    assert c.data == 0


@test("getting a value")  # type: ignore[no-redef]
def _():
    c[0, 0] = 1
    assert c[0, 0] == 1
    c[0, 0] = 0
    assert c[0, 0] == 0


@test("x ≥ width")  # type: ignore[no-redef]
def _():
    with raises(IndexError):
        c[1, 0]
    assert c.get(1, 0) == None
    with raises(IndexError):
        c[1, 0] = True
    c.set(1, 0, True)


@test("x < 0")  # type: ignore[no-redef]
def _():
    with raises(IndexError):
        c[-1, 0]
    assert c.get(-1, 0) == None
    with raises(IndexError):
        c[-1, 0] = True
    c.set(-1, 0, True)


@test("y ≥ width")  # type: ignore[no-redef]
def _():
    with raises(IndexError):
        c[0, 1]
    assert c.get(0, 1) == None
    with raises(IndexError):
        c[0, 1] = True
    c.set(0, 1, True)


@test("y < 0")  # type: ignore[no-redef]
def _():
    with raises(IndexError):
        c[0, -1]
    assert c.get(0, -1) == None
    with raises(IndexError):
        c[0, -1] = True
    c.set(0, -1, True)
