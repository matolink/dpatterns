from BeverageClass import Beverage
from CondimentDecorator import CondimentDecorator
class Whip(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage
    
    def get_description(self):
        string = self.beverage.get_description() + ', Whip'
        return string
    
    def cost(self):
        value = self.beverage.cost() + 0.10
        return value