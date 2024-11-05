from typing import Iterable, Iterator

# Iterator Pattern
class iterable_tkt(Iterable[str]):
    
    def __init__(self):
        self.data = []

    def append(self, obj):
        self.data.append(obj)

    def __str__(self):
        return str(self.data)

    def __getitem__(self, index):
        return self.data[index].dept

    def __iter__(self):
        return iterator_tkt(self.data)

class iterator_tkt(Iterator[str]):
    def __init__(self, iterable_list):
        self.iterator_list = iterable_list
        self.index = 0

    def __next__(self):
        if self.index < len(self.iterator_list):
            x = self.iterator_list[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration

# Observer Pattern
class ticket:
    def __init__(self, name, dept, service):
        self.name = name
        self.dept = dept
        self.service = service
        self.tkt_no = None

    def __str__(self):
        return f"{self.name}: {self.service} : {self.dept}"

# Observer Pattern
class helpdesk:
    
    def __init__(self):
        self.observers = iterable_tkt()
        self.tickets = {}
        self.tkt_no = 1

    def notify(self, obj):
        for observer in self.observers:
            if obj == observer:
                observer.update(self)

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            self.tickets[observer] = []

    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def add_ticket(self, obj):
        for observer in self.observers:
            if observer == obj.service:
                obj.tkt_no = self.tkt_no
                self.tkt_no += 1
                self.tickets[observer].append(obj)
                self.notify(observer)

    def remove_ticket(self, obj):
        for observer in self.observers:
            if observer == obj.service:
                self.tickets[observer].remove(obj)
                self.notify(observer)

# Decorator Pattern
class Update:
    def update(self, ticket):
        pass

class civil(Update):
    def update(self, ticket):
        print(f"New work added for civil: {ticket}")

class software(Update):
    def update(self, ticket):
        print(f"New work added for software: {ticket}")

class hardware(Update):
    def update(self, ticket):
        print(f"New work added for hardware: {ticket}")

if __name__ == '__main__':
    obs = civil()
    obs1 = software()
    obs2 = hardware()
    h = helpdesk()
    h.attach(obs)
    h.attach(obs1)
    h.attach(obs2)
    tkt1 = ticket("shan", "it", "civil")
    print(tkt1)
    tkt2 = ticket("sing", 'it', 'software')
    print(tkt2)
    h.add_ticket(tkt1)
    h.add_ticket(tkt2)
    h.remove_ticket(tkt1)
