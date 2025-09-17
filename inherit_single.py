#Single level inheritance
class app1:
    def v1(self):
        print("orders")

class app1_1(app1):
    def v2(self):
        print("refund")

    def v1(self):
        print("cart")

a=app1_1()
a.v1()
a.v2()