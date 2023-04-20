from BeverageClass import Beverage
from CondimentDecorator import CondimentDecorator
class Mocha(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage
    
    def get_description(self):
        string = self.beverage.get_description() + ', Mocha'
        return string
    
    def cost(self):
        value = self.beverage.cost() + 0.20
        return value