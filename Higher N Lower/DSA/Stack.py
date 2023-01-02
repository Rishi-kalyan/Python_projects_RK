class Node():
    def __init__(self, value):
        self.value=value
        self.next=None
    
class Stack():
    def __init__(self, value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    
    def push(self, value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
            self.height+=1
            return True
        new_node.next=self.top
        self.top=new_node
        self.height+=1
        return True

    def pop(self):
        temp=self.top
        if self.height==0:
            return None
        if self.height==1:
            self.top=None
            self.height-=1
            return temp
        self.top=temp.next
        self.height-=1
        return temp

    def print_stack(self):
        if self.height==0:
            return None
        temp=self.top
        for _ in range(self.height):
            print(temp.value)
            temp=temp.next
        
my_stack=Stack(4)
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
my_stack.pop()
my_stack.print_stack()
        
    