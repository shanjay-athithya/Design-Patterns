from abc import ABC

class Room():
    def __init__(self, flat_no, BHK, name=None, occupancy="Unoccupied"):
        self.flat_no = flat_no
        self.bhk = BHK
        self.name = name
        self.occu = occupancy

    def add_customer(self, name):
        self.occu = "occupied"
        self.name = name


class Room_data():
    def __init__(self):
        self._room_set = {}
        self._observers = []

    @property
    def room_set(self):
        return self._room_set

    @property
    def observers(self):
        return self._observers

    def add_room(self, obj):
        if obj.occu == "occupied" and obj.name is not None:
            self.room_set[obj.flat_no] = [obj.name, obj.bhk, obj.occu]
            self.notify()
        else:
            raise ValueError("Room is not occupied")

    def remove_room(self, obj):
        obj.occu = "Unoccupied"
        obj.name = None
        del self.room_set[obj.flat_no]
        self.notify()

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)


class Observer(ABC):
    def update(self, room_data):
        pass


class Maintenance_observer(Observer):
    def update(self, room_data):
        for flat_no, details in room_data.room_set.items():
            print(f"Flat number {flat_no} is occupied by {details[0]}, BHK: {details[1]}")

# Driver code
if __name__ == "__main__":
    # Create instances
    room_data = Room_data()
    maintenance_observer = Maintenance_observer()

    # Add the observer to the room data
    room_data.add_observer(maintenance_observer)

    # Add rooms
    room1 = Room(flat_no=101, BHK=2)
    room1.add_customer(name="John Doe")
    
    room2 = Room(flat_no=102, BHK=3)
    room2.add_customer(name="Jane")
    
    print("after adding 1 room")
    room_data.add_room(room1)
    
    print("after adding another room")
    room_data.add_room(room2)

    # Remove a room
    print("after removing a room")
    room_data.remove_room(room1)