
class Empty:
    pass

def plain_func(a, b, c, d):
    print(type(a), type(b), type(c), type(d))

plain_func(Empty, 1, "hi", [])

