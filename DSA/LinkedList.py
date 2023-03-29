class Node():
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList():
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_ll(self):
        if self.length==0:
            return None
        temp=self.head
        for _ in range(self.length):
            print(temp.value)
            temp=temp.next
    
    def append(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            return True
        self.tail.next=new_node
        self.tail=new_node
        self.length+=1

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head=None
            self.tail=None
            self.length-=1
            return True
        temp=self.head
        pre=self.head
        while temp.next is not None:
            pre=temp
            temp=temp.next
        pre.next=None
        self.tail=pre
        self.length-=1
        if self.length == 0:
            self.head=None
            self.tail=None
    
    def prepend(self, value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
            self.length+=1
            return True
        new_node.next=self.head
        self.head=new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
            self.length-=1
            return True
        temp=self.head
        self.head=temp.next
        self.length-=1
        return True

    def get(self, index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def insert(self, index, value):
        if index<0 or index>self.length:
            return None
        if index==0:
            self.prepend(value)
            return True
        if index==self.length:
            self.append(value)
            return True
        temp=self.get(index-1)
        new_node=Node(value)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True

    def set_value(self, index, value):
        if index<0 or index>=self.length:
            return None
        temp=self.get(index)
        temp.value=value
        return True

    def remove(self, index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            self.pop_first()
            return True
        if index==self.length-1:
            self.pop()
            return True
        temp=self.get(index-1)
        pre=self.get(index+1)
        temp.next=pre
        self.length-=1
        return True

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        before=None
        after=temp.next
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after






        

my_ll=LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.pop()
my_ll.prepend(0)
my_ll.pop_first()
my_ll.insert(0,1)
my_ll.set_value(1,2)
my_ll.set_value(2,3)
my_ll.remove(2)
my_ll.reverse()
my_ll.print_ll()
print(my_ll.head.value,my_ll.tail.value)