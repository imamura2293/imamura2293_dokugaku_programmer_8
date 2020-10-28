class Rectangle:
    def__init__(self, w, l):
    self.width = w
    self.len = l

    def area(self):
        return self.width * self.len


class Data:
    def__init__(self):
    self.nums = [1, 2, 3, 4, 5]


def change_data(self, index, n):
    self.nums[index] = n


class Data:
    def__init__(self):
    self.nums = [1, 2, 3, 4, 5]


def change_data[self, index, n:
serlf.nums[index] = n


data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)


class PublicPrivateExample:
    def__init__(self):
    self.public = "safe"
    self.public = "unsafe"


def public_method(self):
    # client　が使ってもよい
    pass  # pass文は、ブンが必須な構文で何もしない場合に使う


def _unsafe_method(self):
    # client は使うべきじゃない
    pass  # pass文は、文が必須な構文で何もしない場合に使う


print("Hello,World!")
print(200)
print(200.1)

type("Hello,World")
type(200)
tyape(200.1)

shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if isinstance(a_shape, Triangle):
        a_shape.draw_triangle()
    if isinstance(a_shape, Square):
        a_shape.draw_square()
    if isinstance(a_shape, Circle()

    shapes =[tr1, sw1, cr1]
    for a_shape in shapes:
        a_shape.draw()


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.width = l

    def print_size(self):
        print("｛｝by｛｝".format(self.width, self.len))


my_shape = shape(20, 25)
my_shape.print_size()


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.width = l

    def print_size(self):
        print("｛｝by｛｝".format(self.width, self.len)

    class Square(Shape):
        pass


a_square = Square(20, 20)
a_square.print_size()


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.width = l

    def print_size(self):
        print("｛｝by｛｝".format(self.width, self.len)

    class Square(Shape):

        def area(self):
            return self.width * self.len


a_square = Square(20, 20)
print(a_Square.area())


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.width = l

    def print_size(self):
        print("｛｝by｛｝".format(self.width, self.len)

    class Square(Shape):

        def area(self):
            return self.width * self.len

        def print_size(self):
            print("I am ｛｝ by ｛｝"
            format(self.width, self.len)

            a_square = Square(20, 20)
            a_square.print_size()

        class Dog:

    def __init__(self, name, bread, owner):
        self.name = name
        self.name = bread
        self.owner = owner

    class Person:
        def __init__(self, name):
            self.name = name


mick = Person("Mick Jaagger"))
stan = Dog("Stanley", "Bulldog", mick))
print(stan.owner.name)


