from abc import ABC, abstractmethod
 
class HuffBaseNode(ABC):
    """Huffman tree node implementation: Base class"""

    @abstractmethod
    def is_leaf(self) -> bool:
        pass
    
    @abstractmethod
    def weight(self) -> int:
        pass


class HuffLeafNode(HuffBaseNode):
    """Huffman tree node: Leaf class"""

    def __init__(self, el: str, wt: int) -> None:
        super().__init__()
        self.element = el
        self.wt = wt

    def value(self) -> str:
        """Returns the element value"""
        return self.element
    
    def weight(self) -> int:
        """Returns the weight"""
        return self.wt
    
    def is_leaf(self) -> bool:
        """Return true"""
        return True
    

class HuffInternalNode(HuffBaseNode):
    """Huffman tree node: Internal class"""

    def __init__(self, l, r, wt: int) -> None:
        super().__init__()
        self.left = l 
        self.right = r
        self.wt = wt
    
    def left(self):
        """Returns the left child"""
        return self.left
    
    def right(self):
        """Returns the right child"""
        return self.right