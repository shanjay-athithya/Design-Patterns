from abc import ABC, abstractmethod

# Abstract Product: Car
class Car(ABC):
    @abstractmethod
    def assemble(self):
        pass

# Concrete Products: Sedan, SUV, Hatchback
class Sedan(Car):
    def assemble(self):
        return "Assembling Sedan"

class SUV(Car):
    def assemble(self):
        return "Assembling SUV"

class Hatchback(Car):
    def assemble(self):
        return "Assembling Hatchback"

# Abstract Factory: CarFactory
class CarFactory(ABC):
    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_interior(self):
        pass

    def create_car(self):
        engine = self.create_engine()
        body = self.create_body()
        interior = self.create_interior()
        return f"{engine}\n{body}\n{interior}"

# Concrete Factories: SedanFactory, SUVFactory, HatchbackFactory
class SedanFactory(CarFactory):
    def create_engine(self):
        return "V6 Engine"

    def create_body(self):
        return "Sedan Body"

    def create_interior(self):
        return "Luxury Interior"

class SUVFactory(CarFactory):
    def create_engine(self):
        return "V8 Engine"

    def create_body(self):
        return "SUV Body"

    def create_interior(self):
        return "Spacious Interior"

class HatchbackFactory(CarFactory):
    def create_engine(self):
        return "Inline-4 Engine"

    def create_body(self):
        return "Hatchback Body"

    def create_interior(self):
        return "Compact Interior"

# Client Code
def produce_car(factory):
    try:
        car = factory.create_car()
        print(f"\nProducing a new car:\n{car}")
    except NotImplementedError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    sedan_factory = SedanFactory()
    suv_factory = SUVFactory()
    hatchback_factory = HatchbackFactory()

    produce_car(sedan_factory)
    produce_car(suv_factory)
    produce_car(hatchback_factory)
