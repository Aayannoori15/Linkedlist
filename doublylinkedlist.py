class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.next=next
        self.item=item
class DLL:
    def __init__(self,start=None):
        self.start=start
    def isempty(self):
        return self.start==None
    def insertatstart(self,item):
        n=Node(None,item,self.start)
        if not self.start.isempty():
            self.start.prev=n
        self.start=n
    def insertatlast(self,data):
        temp=self.start
        while temp.next:
            temp=temp.next
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n
    def search(self,data):
        temp=self.start
        while temp:
            if temp.item==data:
                return temp
            temp=temp.next
    def insertafter(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
    def printlist(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next
    def deletefirst(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None
    def deletelast(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def deleteitem(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp.next is not None:
                if temp.item == data :
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next
                    else:
                        temp.prev.next=None
                else:
                    temp=temp.next
    
    def __iter__(self):
        return DLLIterator(self.start)
class DLLIterator:
        def __init__(self,start):
            self.current=start
        def __iter__(self):
            return self
        def __next__(self):
            if not self.current:
                raise StopIteration
            data=self.current.item
            self.current=self.current.next 
            return data
