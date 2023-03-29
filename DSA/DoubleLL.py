class Node():
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class Doubly_LL():
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.length+=1
            return True
        self.tail.next=new_node
        new_node.prev=self.tail
        self.tail=new_node
        self.length+=1
        return True
    
    def print_list(self):
        if self.length==0:
            return None
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        return True

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head=None
            self.tail=None
            self.length-=1
            return True
        temp=self.tail
        self.tail=temp.prev
        self.tail.next=None
        self.length-=1
        if(self.length==0):
            self.head=None
            self.tail=None
        return True
    
    def prepend(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.length+=1
            return True
        temp=self.head
        new_node.next=self.head
        temp.prev=new_node
        self.head=new_node
        self.length+=1
        return True

    def pop_first(self):
        temp=self.head
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
            self.length-=1
            return temp
        self.head=self.head.next
        self.head.prev=None
        self.length-=1
        return temp

    def get(self, index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp


    def set_value(self, index, value):
        temp=self.get(index)
        temp.value=value
        return temp

    def insert(self, index, value):
        if index<0 or index>self.length:
            return None
        if self.length==0:
            self.prepend(value)
            return True
        if index==self.length:
            self.append(value)
            return True
        temp=self.get(index-1)
        new_node=Node(value)
        new_node.prev=temp
        new_node.next=temp.next
        temp.next.prev=new_node
        temp.next=new_node
        self.length+=1
        return True

    def remove(self, index):
        temp=self.get(index)
        if index<0 or index>=self.length:
            return None
        if self.length==0:
            self.pop_first()
            return temp
        if index==self.length-1:
            self.pop()
            return temp
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
        self.length-=1
        return temp

    def reverse(self):
        self.tail=self.head
        while self.head.next is not None:
            self.head.next, self.head.prev, self.head = self.head.prev, self.head.next, self.head.next
        self.head.next, self.head.prev=self.head.prev, None
        

double=Doubly_LL(1)
double.append(2)
double.append(3)
double.pop()
double.prepend(0)
double.append(4)
double.insert(3,3)
double.remove(3)
double.reverse()
double.reverse()
double.print_list()
print(double.head.value,double.tail.value)
print(double.length)