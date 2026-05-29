class shop():

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_item(self):

        for item in self.items:
            print(f"{item.beverages} : {item.quantity}")


class item():

    def __init__(self, beverages, quantity):
        self.beverages = beverages
        self.quantity = quantity


item1 = item("Coffee", 20)
item2 = item("Tea", 0)
item3 = item("Poison", -1/12)

myshop = shop("Akshay Store")

myshop.add_item(item1)
myshop.add_item(item2)
myshop.add_item(item3)

myshop.list_item()