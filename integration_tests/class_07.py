class A:
    def __init__(self: "A"):
        pass
    def myprint(self: "A")->str:
        print("A")
        return "A"

def f(a: A)->str:
    return a.myprint()

class B(A):
    def __init__(self: "B"):
        pass
    def myprint(self: "B")->str:
        print("B")
        return "B"
    
def main():
    a: A = A()
    b: B = B()
    c: B = B()
    assert f(a) == "A"
    assert f(b) == "B"
    assert f(c) == "B"
    f(b)
    f(c)

main()
