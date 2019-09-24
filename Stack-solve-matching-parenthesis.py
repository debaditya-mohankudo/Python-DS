class node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class stack:
    def __init__(self):
        self.__top = None
        self.__size = 0
        
    def __len__(self):
        return self.__size
    
    def is_empty(self):
        if len(self) == 0:
            return True
    
    def push(self, data):
        if self.is_empty():
            self.__top = node(data, None)
            self.__size += 1
        else:
            self.__top = node(data, self.__top)
            self.__size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        elif len(self) == 1:
            top_data = self.__top.data
            self.__size -= 1
            self.__top = None
            return top_data
        else:
            top_data = self.__top.data
            self.__top = self.__top.next_node
            self.__size -= 1
            return top_data
        
    def peek(self):
        if self.is_empty():
            return None
        return self.__top.data
################################
p1 = "{({{[]}})}("

map_p = {
'{' : 1,
'}' : -1,
'(' : 2,
')' : -2,
'[' : 3,
']' : -3
}
s = stack()
for p in p1:
    if s.peek() is None:
        s.push(p)
    else:
        if map_p[p] + map_p[s.peek()] == 0:
            s.pop()
        else:
            s.push(p)
if len(s):
    print("not closed properly")
            
