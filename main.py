class MyList:
    def __init__(self):
        self.data = []

    def add_element(self, element):
        self.data.append(element)

    def remove_element(self, element):
        if element in self.data:
            self.data.remove(element)
        else:
            print(f"{element} noy found in the list")

    def get_length(self):
        return len(self.data)

    def get_elements(self):
        return self.data

    def clear_list(self):
        self.data = []
        print("list cleared")


my_list = MyList()
my_list.add_element(1)
my_list.add_element(2)
my_list.add_element(3)

print("original list", my_list.get_elements())
print("list length", my_list.get_length())

my_list.remove_element(2)

print("updated list", my_list.get_elements())

my_list.clear_list()

print("cleared list", my_list.get_elements())
