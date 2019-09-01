class StackNode(object):
    """class to represent a node in stack"""
    def __init__(self, item, link):
        self.item = item
        self.next = link

class Stack(object):
    """class to represent the stack"""
    def __init__(self):
        self.__top = None
        self.__size = 0
        
    def __len__(self):
        """returns size of the stack """
        return self.__size
    
    def push(self, item):
        """push an item onto the top of the slack"""
        self.__top = StackNode(item, self.__top)
        self.__size += 1
        
    def pop(self):
        """remove the top item from stack """
        self.__top = self.__top.next
        self.__size -= 1
        
    def peek(self):
        """ know the top item without removing the item from stack"""
        if self.__top is None:
            return None 
        else:
            return self.__top.item
