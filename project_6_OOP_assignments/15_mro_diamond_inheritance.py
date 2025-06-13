class A:
    def show():
        print("This is class A")

class B(A) :
    def show():
        print("This is class B")

class C(A):
    def show():
        print("This is class C")


class D(B,C):  #if this would be written (C,B)  output will be: This is class C
    pass


d = D()
D.show()