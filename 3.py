class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Drawing started")


class Pen(Stationery):

    def draw(self):
        print(f"Drawing with pen. title: {self.title}")


class Pencil(Stationery):

    def draw(self):
        print(f"Drawing with pencil. title: {self.title} ")


class Handle(Stationery):

    def draw(self):
        print(f"Drawing with handle. title: {self.title}")


pen = Pen("Blue Pen")
pencil = Pencil("Black Pencil")
handle = Handle("Red Handle")

pen.draw()
pencil.draw()
handle.draw()
