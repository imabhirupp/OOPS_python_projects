def add(*args):
    s = 0
    for n in args:
        s = s+n
    print(s)
add(1,2,3,5,6)


def calc(n, **kwargs):
    n = n + kwargs["add"]
    n = n * kwargs["multiply"]
    print(n)
calc(10,add=5,multiply=6)


class Car():
    def __init__(self, **abhi):
        self.company = abhi.get("company")
        self.model = abhi.get("model")
        self.color = abhi.get("color")
        self.price = abhi.get("price")

my_car = Car(company="Nissan",model="GTR",price="$1,80,000")
print(my_car.company)
print(my_car.color)
print(my_car.price)