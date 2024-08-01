from lpython import i32

class Base:
    def __init__(self:"Base"):
        self.x_A : i32 = 10

class Derived(Base):
    def __init__(self:"Derived") :
        super().__init__()
        self.y_B : i32 = 6
    def get_x_A(self:"Derived"):
        print(self.x_A)
def main():
    d : Derived = Derived()
    print(d.x_A)
    print(d.y_B)
    d.get_x_A()
main()
