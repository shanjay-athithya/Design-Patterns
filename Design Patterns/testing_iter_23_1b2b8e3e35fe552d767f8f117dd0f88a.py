from typing import Iterable, Iterator
x = "vasuki"

class iter_cap(Iterable[str]):
    def __init__(self, lst):
       self.lst = lst;

    def __iter__(self):
        return spl_itr(self.lst)
    def __str__(self):
        return(self.lst)

class spl_itr(Iterator):
    def __init__(self,lst):
        self.lst=[]
        for x in lst:
            if(x.isupper()):
                self.lst.append(x)
        print("the list is ",self.lst)
        self.idx = 0
        

    def __next__(self):
        if(self.idx<len(self.lst)):
            x = self.lst[self.idx]
            self.idx = self.idx+ 1
            return x
        else:
            raise StopIteration
       
    
            


# Driver    
x = iter_cap("VasukiP")

for i in x:
    print(i)
