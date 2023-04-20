from BeverageClass import Beverage
import abc
class CondimentDecorator(metaclass=abc.ABCMeta):
    beverage = Beverage()

    def get_description():
        pass