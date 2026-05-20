def i(a):
    return int(a) if a == int(a) else a
def P1():
    def parity(b):
        if (b % 2 == 0):
            print(f"{b} is even.")
        else:
            print(f"{b} is odd.")
    parity(int(input("Enter the Number: ")))
def P2():
    def table(c):
        x = 1
        while (x<=10):
            print(f"{c} × {x} = {c * x}")
            x += 1
    table(int(input("Enter the Number: ")))
def P3():
    d = i(float(input("Enter first Number: ")))
    e = i(float(input("Enter second Number: ")))
    print(f"{max(d,e)} is largest.")
def P4():
    f = i(float(input("Enter the Length: ")))
    g = i(float(input("Enter the Breadth: ")))
    print(f"Area of rectangle with length {f} and breadth {g} is {i(f * g)}.")
def P5():
    h = i(float(input("Enter the Number: ")))
    print(f"Square of {h} is {h ** 2}.\nCube of {h} is {h ** 3}.")
P1()
P2()
P3()
P4()
P5()