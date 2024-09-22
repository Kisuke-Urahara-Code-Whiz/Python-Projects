class a:

    def __init__(self):
        self.a = 1
        self.b = 2

    def do(self):
        print("Hasta la vista")

    def haha(self):
        print(f" Final a : {self.a}")

class b(a):

    def __init__(self):
        super().__init__()
        self.c = 3

    def show(self):
        print(self.a)
        print(self.b)
        print(self.c)


obj = b()
obj.show()
print(f" Inherited class a : {obj.a}")
obj.a +=1
print(f" Inherited class a : {obj.a}")
print("\nConcept 1\n")
obj.haha()

obj.do()

user = a()
print(f" Super class a : {user.a}")
print("Concept 2")
user.haha()