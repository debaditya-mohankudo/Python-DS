class QNode():
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class Q():
    def __init__(self):
        self.qhead=None
        self.qtail=None
        self.__size = 0
        
    def __len__(self):
        return self.__size
        
    def enqueue(self, data):
        new_node = QNode(data)
        if len(self) == 0:
            self.qhead = new_node
            self.qtail = new_node
        else:
            self.qtail.next = new_node
            self.qtail = new_node
        self.__size += 1
        
    def dequeue(self):
        if len(self) == 0:
            return None
        elif len(self) == 1:
            data = self.qhead.data
            self.qhead.data = None
            self.qtail.data = None
            self.__size -= 1
            return data
        else:
            data = self.qhead.data
            self.qhead = self.qhead.next
            self.__size -= 1
            return data
    
    def size(self):
        return len(self)


def queue_the_string(queue):
    """ convert a string into an queue and return an queue object """
    q = Q()
    for char in queue:
        q.enqueue(char)
    return q
        
def reverseK(queue,k,n):
    # code here
    out = []
    q = queue_the_string(queue)
    counter = 1
    while(counter <= n):
        if counter <= k:
            out = [q.dequeue()] + out
        else:
            out = out + [q.dequeue()]
        counter += 1
    return out
