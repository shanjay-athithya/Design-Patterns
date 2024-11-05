from abc import ABC, abstractmethod

# Abstract Product A
class ElectronicDevice(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Product A1
class Laptop(ElectronicDevice):
    def display(self):
        return "Laptop"

# Concrete Product A2
class Smartphone(ElectronicDevice):
    def display(self):
        return "Smartphone"


# Abstract Product B
class Accessory(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Product B1
class LaptopAccessory(Accessory):
    def display(self):
        return "Laptop Accessory"

# Concrete Product B2
class SmartphoneAccessory(Accessory):
    def display(self):
        return "Smartphone Accessory"


# Abstract Factory
class DeviceFactory(ABC):
    @abstractmethod
    def create_device(self) -> ElectronicDevice:
        pass

    @abstractmethod
    def create_accessory(self) -> Accessory:
        pass



# Concrete Factory 1
class LaptopFactory(DeviceFactory):
    def create_device(self) -> ElectronicDevice:
        return Laptop()

    def create_accessory(self) -> Accessory:
        return LaptopAccessory()

# Concrete Factory 2
class SmartphoneFactory(DeviceFactory):
    def create_device(self) -> ElectronicDevice:
        return Smartphone()

    def create_accessory(self) -> Accessory:
        return SmartphoneAccessory()




# Client
class ECommerceApp:
    def __init__(self, factory: DeviceFactory):
        self.factory = factory

    def order_product(self):
        device = self.factory.create_device()
        accessory = self.factory.create_accessory()

        print(f"Ordered a {device.display()} with {accessory.display()}")

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Ordering a Laptop
    laptop_factory = LaptopFactory()
    ecommerce_app_1 = ECommerceApp(laptop_factory)
    ecommerce_app_1.order_product()

    # Test Case 2: Ordering a Smartphone
    smartphone_factory = SmartphoneFactory()
    ecommerce_app_2 = ECommerceApp(smartphone_factory)
    ecommerce_app_2.order_product()
