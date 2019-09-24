class BSTNode:
    '''represent the binary tree node'''
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.counter = 1
        
    def __str__(self):
        return str(self.data) + str(self.counter)
  
  class BST:
    """represent the binary search tree"""
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data, left=None, right=None)
        else:
            # recursively find the node and add data
            self.__insert(self.root, data)
    
    def __insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BSTNode(data, left=None, right=None)
            elif node.left.data == data: 
                node.left.counter += 1
            else:
                self.__insert(node.left , data)
        elif data > node.data:
            if node.right is None:
                node.right = BSTNode(data, left=None, right=None)
            elif node.right.data == data:
                node.right.counter += 1
            else:
                self.__insert(node.right, data)
        else:
            self.node.counter += 1
            
    def print_tree(self):
        if self.root is None:
            print('Empty! LOL')
        else:
            self.__print_tree(self.root)
    
    def __print_tree(self, node):
        # print recursively
        if node.left is not None:
            self.__print_tree(node.left)
        print(node.data, node.counter)
        if node.right is  not None:
            self.__print_tree(node.right)

a = [1, 3, 5, 11, 13, 40, 15, 2, 5, 3]
bst_Tree = BST()
for item in a:
    bst_Tree.insert(item)
bst_Tree.print_tree()
1 1
2 1
3 2
5 2
11 1
13 1
15 1
40 1
    
