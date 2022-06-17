class Base_Shop():
    def buy(self, item):
      print("buying item", item)

class Spa(Base_Shop):
    def __init__(self):
        print("in init of spa")

class CoffeeShop(Base_Shop):
    def __init__(self):
        print("in init of coffeeshop")

class Shop(Base_Shop):
    def __init__(self):
        print("in init of Shop")

class Hotel():
    def __init__(self):
        print("Hotel init")
        self.spa = Spa()
        self.cs = CoffeeShop()
        self.shop = Shop()

    def buy_item(self, shop, item)
        # if...
        pass

    def buy_spa_item(self, item):
        self.spa.buy(item)

bpl_h = Hotel()
bpl_h.buy_spa_item("soap")
