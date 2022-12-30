class node():
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList():
    def __init__(self,value):
        new_node=node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self, value):
        new_node=node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def pop(self):
        temp=self.head
        pre=self.head
        if self.length == 0:
            return False
        elif self.length == 1:
            self.head=None
            self.tail=None
        else:
            while temp.next is not None:    
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
            self.length-=1
            if self.length == 0:
                self.head=None
                self.tail=None
            return temp

    def prepend(self, value):
        new_node=node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.length == 0:
            return False
        elif self.length == 1:
            self.head=None
            self.tail=None
            self.length-=1
        else:
            temp=self.head
            self.head=temp.next
            temp=None
            self.length-=1
            if self.length == 0:
                self.tail=None

    def get(self, index):
        if index<0 or index>=self.length:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp

    def set_value(self, index, value):
            temp=self.get(index)
            if temp is not None:
                temp.value=value
                return True
            return False

    def insert(self, index, value):
        if index<0 or index>self.length:
            return False
        elif index==0:
            self.prepend(value)
        elif index==self.length:
            self.append(value)
        else:
            temp=self.get(index-1)
            new_node=node(value)
            new_node.next=self.get(index)
            temp.next=new_node
            self.length+=1
            return True

    def remove(self, index):
        if index<0 or index>=self.length:
            return False
        elif index==0:
            self.pop_first()
        elif index==self.length-1:
            self.pop()
        else:
            temp=self.get(index-1)
            temp.next=self.get(index+1)
            self.length-=1
            return temp.next
        
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


my_linked_list=LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.pop()
my_linked_list.append(6)
my_linked_list.pop_first()
my_linked_list.set_value(1,7)
my_linked_list.insert(1,6)
my_linked_list.insert(3,8)
my_linked_list.remove(3)
my_linked_list.reverse()
my_linked_list.reverse()
my_linked_list.print_list()