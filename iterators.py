class LinkedList:
    
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def insert(self, value):
        self.head = Node(value, self.head)

    def __iter__(self):
        def generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return generator()


    
    def __len__(self):
        
        length = 0
        for _ in self:
            length += 1
        return length
        # or just this after the method signature: 
        # return len(list(iter(self)))
    
    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item
            raise IndexError
    
    
    def __str__(self):
        out = ""
        
        for value in self:
            out += f"[ {value} ] -> "
        return out + "None"
    
    def __eq__(self, extra):
        return list(self) == list(extra)
    
    
    def __contains__(self, value):
        for item in self:
            if item == value:
                return True

        return False
    
class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_