def f():
    try:
        yield 1
        try:
            yield 2 # 1 2 4 5 8 9 10 11
            1/0
            yield 3  # never get here
        except ZeroDivisionError:
            yield 4
            yield 5
            raise
        except Exception:
            yield 6
        yield 7     # the "raise" above stops this
    except:
        yield 8
    yield 9
    try:
        x = 12
    finally:
       yield 10
    yield 11


print(list(f()))
# [1, 2, 4, 5, 8, 9, 10, 11]
