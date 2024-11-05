from abc import ABC, abstractmethod

class AbstractBinaryTree(ABC):
    
    @abstractmethod
    def construct(self, data):
        pass
    
    @abstractmethod
    def insert(self, item, pos):
        pass
    
    @abstractmethod
    def preorder(self, pos):
        pass
    
    @abstractmethod
    def postorder(self, pos):
        pass
    
    @abstractmethod
    def inorder(self, pos):
        pass