import abc
class Beverage(metaclass=abc.ABCMeta):
    description = 'Unknown Beverage'
    def get_description(self):
        return self.description
    
    def cost(self) -> float:
        pass

    