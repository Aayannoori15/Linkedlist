class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
class CDLL:
    def __init__(self,start=None):
        self.start=start
    def isempty(self):
        return self.start==None
    def insertatstart(self,data):
        n=Node(data)
        if self.isempty():
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
    def insertatlast(self,data):
        n=Node(data)
        if self.isempty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
    def search(self,data):
        temp=self.start
        if temp==None:
            return None
        if temp.item==data:
            return data
        else:
            temp=temp.next
            while temp is not self.start:
                if temp.item==data:
                    return data
                temp=temp.next
        return None
    def insertafter(self,temp,item):
        if temp is not None:
            n=Node(item)
            n.prev=temp
            n.next=temp.next 
            temp.next.prev=n
            temp.next=n
    def printlist(self):
        temp=self.start 
        if temp is not None:
            print(temp.item , end='')
        temp=temp.next 
        while temp is not self.start:
            print(temp.item , end='')
            temp=temp.next 
    def deletefirst(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
    def deletelast(self):
        if self.start is not None:
            if self.start ==self.start.next:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev
    def deleteitem(self,data):
        if self.start is not None :
            if self.start.next==self.start and self.start.item==data:
                self.start=None
            else:
                temp=self.start 
                if temp.item==data:
                    self.deletefirst()
                else:
                    while temp is not self.start:
                        if temp.item==data:
                            temp.prev.next=temp.next
                            temp.next.prev=temp.prev
    def __iter__(self):
        return CDLLiterator(self.start)
    
class CDLLiterator:
    def __init__(self,start):
        self.start=start
        self.current=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
            data=self.current.item
            self.current=self.current.next 
        return data