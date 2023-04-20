from MochaClass import Mocha
from ExpressoClass import Expresso
from WhipClass import Whip
from SoyClass import Soy
from HouseBlendClass import HouseBlend
from DarkRoastClass import DarkRoast

class StarbuzzCoffee():
    def __init__(self):
        beverage = Expresso()
        print(beverage.get_description())
        print(f'${beverage.cost()}')

        beverage_two = DarkRoast()
        beverage_two = Mocha(beverage_two)
        beverage_two = Mocha(beverage_two)
        beverage_two = Whip(beverage_two)
        print(beverage_two.get_description())
        print(f'${beverage_two.cost()}')

        beverage_three = HouseBlend()
        beverage_three = Soy(beverage_three)
        beverage_three = Mocha(beverage_three)
        beverage_three = Whip(beverage_three)
        print(beverage_three.get_description())
        print(f'${beverage_three.cost()}')


StarbuzzCoffee()