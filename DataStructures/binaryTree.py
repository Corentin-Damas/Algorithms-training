#. Define a Tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right= None
        self.data = data
        
    def insert(self, data):
        # Check if the first Node is Empty or not, if it's empty populate it with insert(data)
        if self.data is None:
            self.data = data
        
        # Build a news node
        else: 
            if data <self.data: 
                
                # If the value is lower and no node bellow create new node at the left 
                if self.left is None:
                    self.left = Node(data)
                
                # Else if there is a Node and it's still lower : recursion 
                else:
                    self.left.insert(data)
            
            # Same but if the data > previous data create new nodes to the right
            elif data > self.data: 
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def inOrderPrint(r):
    if r is None: 
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end = ' ')
        inOrderPrint(r.right)   

def preOrderPrint(r):
    if r is None: 
        return
    else: 
        print(r.data, end = ' ')
        preOrderPrint(r.left)
        preOrderPrint(r.right)  

def postOrder(r):
    if r is None: 
        return
    else: 
        print(r.data, end = ' ')
        postOrder(r.right)  
        postOrder(r.left)
    
def makeList(r):
    if r is None:
        return
    else: 
        d[r.data] = []
        makeList(r.left)
        if r.left:
            d[r.data].append(r.left.data)
        if r.right:
            d[r.data].append(r.right.data)
        makeList(r.right)
    return d
    
def DFPrint(tree):
    if tree is None:
        return
    else:
        if tree.left:
            DFPrint(tree.left)
        print(tree.data, end=" ")
        if tree.right:
            DFPrint(tree.right)


if __name__ == '__main__':
    root = Node('g')
    root.insert("c")
    root.insert("b")
    root.insert("a")
    root.insert("k")
    root.insert("i")
    root.insert("h")
    root.insert("e")
    
print('in Order')
inOrderPrint(root)
print("\nPre Order")
preOrderPrint(root)
print("\nPost Order")
postOrder(root)

# Adjacency list 
d ={}
aList = makeList(root)

print("\nAdjacency List")
for ele in aList: 
    print(f"{ele}:{d[ele]}")