from spa import Spa
from coffeeshop import CoffeeShop
from shop import Shop

class Hotel():
    def __init__(self):
        print("Hotel init")
        self.spa = Spa()
        self.cs = CoffeeShop()
        self.shop = Shop()

    def display_coffee_detials(self):
        for coffee in self.cs.get_coffee_details():
            print("* ", coffee)


bhopal_hotel = Hotel()
bhopal_hotel.display_coffee_detials()
