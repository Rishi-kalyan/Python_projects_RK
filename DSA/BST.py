class Node():
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

class BST():
    def __init__(self):
        self.root=None
    
    def insert(self, value):
        temp=self.root
        new_node=Node(value)
        if self.root==None:
            self.root=new_node
        else:
            if new_node==temp:
                return False
            while(True):
                if new_node.value<temp.value:
                    if(temp.left==None):
                        temp.left=new_node
                        return True
                    else:
                        temp=temp.left
                if new_node.value>temp.value:
                    if(temp.right==None):
                        temp.right=new_node
                        return True
                    else:
                        temp=temp.right
    
    def contains(self, value):
        temp=self.root
        while(temp!=None):
            if(value==temp.value):
                return True
            else:
                if(value<temp.value):
                    temp=temp.left
                if(value>temp.value):
                    temp=temp.right
        return False
    
my_bst=BST()
my_bst.insert(1)
my_bst.insert(0)
my_bst.insert(2)
print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.right.value)
print(my_bst.contains(4))

