from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

class ReadState(State):
    def read(self):
        print("Reading")
        return self

    def write(self):
        print("Switching to Write state")
        return WriteState()

class WriteState(State):
    def read(self):
        print('Switching to Read state')
        return ReadState()

    def write(self):
        print("Writing")
        return self
    
class ReadWriteState:
    def __init__(self):
        self.state = ReadState()

    def perform_read(self):
        self.state = self.state.read()

    def perform_write(self):
        self.state = self.state.write()

if __name__ == '__main__':
    # Example Usage
    reader_writer = ReadWriteState()

    # Perform read operations
    for _ in range(3):
        reader_writer.perform_read()

    # Perform write operations
    for _ in range(2):
        reader_writer.perform_write()
