class Node():
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue():
    def __init__(self, value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    
    def enqueue(self, value):
        new_node=Node(value)
        if self.length==0:
            self.first=new_node
            self.last=new_node
            self.length=+1
            return True
        self.last.next=new_node
        self.last=new_node
        self.length+=1
        return True
    
    def dequeue(self):
        temp=self.first
        if self.length==0:
            return None
        if self.length==1:
            self.first=None
            self.last=None
            self.length-=1
            return temp
        self.first=temp.next
        temp.next=None
        self.length-=1
        if(self.length==0):
            self.first=None
            self.last=None
        return temp
    
    def print_queue(self):
        temp=self.first
        for _ in range(self.length):
            print(temp.value)
            temp=temp.next
        
my_queue=Queue(0)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
