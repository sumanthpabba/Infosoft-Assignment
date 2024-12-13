from typing import Optional


class Node():
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:

        if node.start < node.end: #Check for valid input
            if node.start >= self.end:  # No overlap, insert as right child
                if not self.right_child:
                    self.right_child = node
                    return True
                else:
                    return self.right_child.insert(node)
            elif node.end <= self.start:  # No overlap, insert as left child
                if not self.left_child:
                    self.left_child = node
                    return True
                else:
                    return self.left_child.insert(node)
            else:  # Overlap detected
                return False
        else:
            return False # Invalid input

class Calendar():
    def __init__(self):
        self.root: Node = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start=start, end=end)
            return True
        return self.root.insert(node=Node(start, end))
    

cal = Calendar()
print(cal.book(5,10))
print(cal.book(8,13))
print(cal.book(10,15))
