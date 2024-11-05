from abc import ABC,abstractmethod

class State(ABC):

    @abstractmethod
    def go_up(self):
        pass

    @abstractmethod
    def go_down(self):
        pass

class GroundFloor(State):

    def __init__(self,elevator):
        print('you are in ground floor')
        self.elevator=elevator

    def go_up(self):
        self.elevator.level=Firstfloor(self.elevator)
    
    def go_down(self):
        print('already in ground floor')

class Firstfloor(State):

    def __init__(self,elevator):
        print('you are in First floor')
        self.elevator=elevator
    
    def go_down(self):
        self.elevator.level=GroundFloor(self.elevator)
    
    def go_up(self):
        self.elevator.level=SecondFloor(self.elevator)

class SecondFloor(State):

    def __init__(self,elevator):
        print('you are in second floor')
        self.elevator=elevator
    
    def go_up(self):
        print('no more floors')
    
    def go_down(self):
        self.elevator.level=Firstfloor(self.elevator)

class Elevator:

    def __init__(self):
        self.level=GroundFloor(self)
    
    def go_up(self):
        self.level.go_up()
    
    def go_down(self):
        self.level.go_down()

e=Elevator()
e.go_down()
e.go_up()
e.go_up()
e.go_down()
