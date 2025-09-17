#Multi level inheritance
'''class grandfather:
    def car(self):
        print("red car")

class dad(grandfather):
    def house(self):
        print("white house")

class son(dad):
    def factory(self):
        print("yellow factory")

s=son()
s.car()
s.house()
s.factory()
'''
class boy:
    def car(self):
        print("Ford Mustang")


class friend:
    def cars(self):
        print("g wagon,911")

c = boy()
c.car()
