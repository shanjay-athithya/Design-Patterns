class Bus:

    def __init__(self,name):
        self.name=name
    
    def increase(self):
        print('speed increased to 50kmph')

class Car:

    def __init__(self,name):
        self.name=name
    
    def accelerate(self):
        print('speed increased to 70kmph')
    
class bike:
    
    def __init__(self,name):
        self.name=name
    
    def speedo(self):
        print('speed increased to 100kmph')

class AdapterBike:

    def __init__(self,bike):
        self.bike=bike
        self.name=bike.name
    
    def accelerate(self):
        self.bike.speedo()

class AdapterBus:

    def __init__(self,bus):
        self.bus=bus
        self.name=bus.name
    
    def accelerate(self):
        self.bus.increase()

class VehicleDetail:

    def __init__(self):
        pass

    def get_details(self,vehicle):
        print(vehicle.name)
        vehicle.accelerate()

b=Bus('volvo')
c=Car('lamborghini')
bi=bike('yamaha')
l=[c,AdapterBike(bi),AdapterBus(b)]
a=VehicleDetail()
for i in l:
    a.get_details(i)
    