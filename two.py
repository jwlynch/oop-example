class Example2:
    def __init__(self):
        print("entering Example2::__init__()")
        print(f"  self is {self}")
        print("leaving Example2::__init__()")

    def prt(self, ref):
        print("entering Example2::prt()")
        print(f"  self is {self},")
        print(f"  ref is {ref}")
        print("leaving Example2::prt()")

ex2 = Example2()

print(f"\nex2 is {ex2}")

# now let's call the prt method, with a ref to the same object we're passing
# which is ex2

ex2.prt(ex2)
