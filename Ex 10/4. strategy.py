from abc import ABC, abstractmethod

class Entity(ABC):
    pass

class Benz(Entity):
    def __init__(self):
        self.name = 'Benz'
        self.base_price = 2000000
    
class BMW(Entity):
    def __init__(self):
        self.name = 'BMW'
        self.base_price = 3000000
        
class Strategy(ABC):
    @abstractmethod
    def price(self, entity):
        pass

class NormalStrategy(Strategy):
    def price(self, entity):
        return entity.base_price * 1
    
class DiscountingStrategy(Strategy):
    def price(self, entity):
        return entity.base_price * 0.9
    
class PriceCalculator:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def calculate_price(self, entity):
        return self.strategy.price(entity)
    
    def change_strategy(self, strategy):
        self.strategy = strategy

# Driver Code
if __name__ == '__main__':
    benz_car = Benz()
    bmw_car = BMW()

    normal_strategy = NormalStrategy()
    discount_strategy = DiscountingStrategy()

    calculator = PriceCalculator(normal_strategy)

    print(f"Price of {benz_car.name} with Normal Strategy: {calculator.calculate_price(benz_car)}")
    print(f"Price of {bmw_car.name} with Normal Strategy: {calculator.calculate_price(bmw_car)}")

    calculator.change_strategy(discount_strategy)

    print(f"Price of {benz_car.name} with Discounting Strategy: {calculator.calculate_price(benz_car)}")
    print(f"Price of {bmw_car.name} with Discounting Strategy: {calculator.calculate_price(bmw_car)}")
