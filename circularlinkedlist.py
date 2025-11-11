class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,last=None):
        self.last=last
    def isempty(self):
        return self.last==None
    def insertatstart(self,data):
        if self.last is not None:
            n=Node(data,self.last.next)
            self.last.next=n
        else:
            n=Node(data,n)
            self.last=n
    def insertatlast(self,data):
        n=Node(data)
        if self.isempty():
            self.last=n
            n.next=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def search(self,data):
        if self.last==None:
            return None
        temp=self.last.next
        while temp is not self.last:
            if temp.item == data:
                return data
        temp=temp.next 
        if temp.item == data:
            return data
        return None
    def insertafter(self,temp,data):
        if temp is not None:
            n=Node(data)
            n.next=temp.next
            temp.next=n
            if temp==self.last:
                self.last=n
    def printlist(self):
        if self.isempty()==False:
            temp=self.last.next
            while temp is not self.last:
                print(temp.item,end=' ')
                temp=temp.next
            print(temp.item)
    def deletefirst(self):
        if self.isempty():
            pass
        if not self.isempty():
            if self.last.next==self.last:
                self.last=None
            else :
                self.last.next=self.last.next.next 
    def deletelast(self):
        if not self.last==None:
            if self.last.next==self.last:
                self.last=None
        else:
            temp=self.last=None
            while temp.next is not self.last:
                temp=temp.next
            temp.next=temp.next.next
            self.last=temp
    def deleteitem(self,data):
        if not self.isempty():
            if self.last.next==self.last and self.last.item==data:
                self.last=None
            else:
                if self.last.next==data:
                    self.last.next=self.last.next.next
                else:
                    temp=self.last.next
                    while temp is not self.last:
                        if temp.next.item==data:
                                if temp.next is not self.last:
                                    temp.next=temp.next.next 
                                    break
                                else:
                                    temp.next=temp.next.next
                                    self.last=temp
                                    break
                        if temp==self.last:
                            break
    def __iter__(self):
        if self.last==None:
            return CLLiterator(None):
        else:
            return CLLiterator(self.last.next):
class CLLiterator:
    def __init__(self,start):
        self.current=start
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        if self.current == self.start:
            temp = data
            self.current = None     
            return temp
        return data



