from abc import ABC, abstractmethod
from datetime import date

# Observer Pattern
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class SalesRep(Observer):
    def update(self, message):
        print(f"Sales Rep received alert: {message}")

class ShopOwner(Observer):
    def update(self, message):
        print(f"Shop Owner received alert: {message}")

# Singleton Pattern
class StockManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(StockManager, cls).__new__(cls)
            cls._instance.stock = {}
            cls._instance.observers = []
        return cls._instance

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def update_stock(self, medicine, quantity):
        if medicine in self.stock:
            self.stock[medicine] += quantity
        else:
            self.stock[medicine] = quantity
        self.notify_observers(f"Stock updated: {medicine} - Quantity: {quantity}")

    def check_stock(self, medicine, quantity):
        if medicine in self.stock and self.stock[medicine] >= quantity:
            return True
        return False

# Strategy Pattern
class StockAlertStrategy(ABC):
    @abstractmethod
    def alert(self, medicine):
        pass

class LowStockAlert(StockAlertStrategy):
    def alert(self, medicine):
        print(f"Low Stock Alert for {medicine}")

class ExpiryAlert(StockAlertStrategy):
    def alert(self, medicine):
        print(f"Expiry Alert for {medicine}")

# Context
class StockAlertContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def generate_alert(self, medicine):
        self.strategy.alert(medicine)

# Unit Testing
def unit_testing():
    stock_manager = StockManager()

    sales_rep = SalesRep()
    shop_owner = ShopOwner()

    stock_manager.add_observer(sales_rep)
    stock_manager.add_observer(shop_owner)

    stock_alert_context = StockAlertContext(LowStockAlert())

    stock_manager.update_stock("Medicine A", 50)
    stock_manager.update_stock("Medicine B", 20)

    if stock_manager.check_stock("Medicine A", 30):
        print("Medicine A is available.")
    else:
        stock_alert_context.generate_alert("Medicine A")

    if stock_manager.check_stock("Medicine C", 10):
        print("Medicine C is available.")
    else:
        stock_alert_context.set_strategy(ExpiryAlert())
        stock_alert_context.generate_alert("Medicine C")

if __name__ == "__main__":
    unit_testing()
