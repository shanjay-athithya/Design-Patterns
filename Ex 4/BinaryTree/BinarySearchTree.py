from AbstractBinaryTree import AbstractBinaryTree
from Node import Node

class BinarySearchTree(AbstractBinaryTree):
    def __init__(self):
        super().__init__()
        self.root = None
        
    def construct(self, data):
        if isinstance(data, list) and len(data) != 0:
            for _item in data:
                self.root = self.insert(_item, self.root)
        else:
            raise ValueError("data must be a list and should not be empty")
            
    def insert(self, item, pos):
        if pos is None:
            return Node(item)
        elif item < pos.item:
            pos.left = self.insert(item, pos.left)
        elif item > pos.item:
            pos.right = self.insert(item, pos.right)
        return pos
        
    def preorder(self, pos):
        order =f"[{pos.item}"
        if pos.left is not None:
            order += self.preorder(pos.left)
        if pos.right is not None:
            order += self.preorder(pos.right)
        order += ']'
        return order
    
    def inorder(self, pos):
        order = ''
        if pos.left is not None:
            order += self.inorder(pos.left)
        order += f"[{pos.item}"
        if pos.right is not None:
            order += self.inorder(pos.right)
        order += ']'
        return order
    
    def postorder(self, pos):
        order = ''
        if pos.left is not None:
            order += self.postorder(pos.left)
        if pos.right is not None:
            order += self.postorder(pos.right)
        order = f"[{pos.item}]" + order
        return order
    
    def _inorder(self, node):
        if node:
            return self._inorder(node.left) + [node.item] + self._inorder(node.right)
        return []

    def _preorder(self, node):
        if node:
            return [node.item] + self._preorder(node.left) + self._preorder(node.right)
        return []

    def _postorder(self, node):
        if node:
            return self._postorder(node.left) + self._postorder(node.right) + [node.item]
        return []
    
if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.construct([4,9,0,7,4])
    print(tree._inorder(tree.root))