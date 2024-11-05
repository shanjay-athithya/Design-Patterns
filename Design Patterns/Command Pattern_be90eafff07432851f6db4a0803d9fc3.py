from abc import ABC, abstractmethod
#abstract command class
class command(ABC):

    @abstractmethod
    def process():
        pass
#various commands
class CloseWindow(command):
   
    def process(self):
        x=OS()
        x.close()

   
class SaveWindow(command):
   
    def process(self):
        x=OS()
        x.save()
#invoker
class GUI():
    def altf4(self):
        CloseWindow().process()
    def closebutton():
        CloseWindow().process()
    def ctls(self):
        SaveWindow().process()
                    
#Implementer  
class OS():
    def __init__(self):
        ...
        
    def close(self):
        print("detach memory and close")
    def save(self):
        print("save in memory")
       
G = GUI()
G.altf4()
G.ctls()
