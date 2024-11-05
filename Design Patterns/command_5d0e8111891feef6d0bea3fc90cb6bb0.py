from abc import ABC

class command(ABC):
    def __init__(self,receiver):
        self.receiver=receiver

    def process_command(self):
        pass

class command_implementation(command):
    def __init__(self,receiver):
        self.receiver=receiver

    def process_command(self):
        self.receiver.update()
        print('Receiver Notified!')

class receiver:
    def __init__(self,name):
        self.name=name

    def update(self):
        print('Service Done!')
        print('Receiver Updated!')

class invoker:
    def command(self,cmd):
        self.cmd=cmd
        
    def execute(self):
        self.cmd.process_command()

if __name__=='__main__':
    r=receiver('John')
    cmd=command_implementation(r)
    i=invoker()
    i.command(cmd)
    i.execute()