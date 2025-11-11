class node:
    def __init__(self,item,next):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start is None
    def insert_at_start(self,data):
        n=node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=node(data,None)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def insert_after(self,temp,data):
        n=node(data,temp.next)
        temp.next=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            else:
                temp=temp.next
        return None
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    def deletefirst(self):
        if self.start is not None:
            self.start=self.start.next
    def deletelast(self):
        temp=self.start
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def Delete_data(self,data):
        temp=self.start
        if self.start is None:
            return
        elif self.start.next is None:
            if self.start.item == data:
                self.start=None
        else:
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if  temp.next.item == data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return lliterator(self.start)
class lliterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
   

myll=SLL()
print(myll)
myll.insert_at_start(22)
myll.insert_at_last(44)
for x in myll:
    print(x,end=' ')



            
