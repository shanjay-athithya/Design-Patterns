from typing import Iterable,Iterator

class student:

    def __init__(self,name,mark,club):
        self.name=name
        self.mark=mark
        self.club=club
    
    def __str__(self):
        result=''
        result+=self.name+'\n'+str(self.mark)+'\n'+self.club
        return result

class iterable_student(Iterable[str]):

    def __init__(self,*args):
        self.student_list=[*args]
    
    def append(self,obj):
        self.student_list.append(obj)      
    
    def __str__(self):
        return str(self.student_list)

    def __getitem__(self,index):
        return self.student_list[index].club
    
    def __iter__(self):
        return iterator_student(self.student_list)

class iterator_student(Iterator[str]):

    def __init__(self,iterable_list):
        self.iterator_list=[x for x in iterable_list if x.club=='nss']
        self.index=0
    
    def __next__(self):
        if self.index<len(self.iterator_list):
            x = self.iterator_list[self.index]
            self.index+=1
            return x
        else:
            raise StopIteration

a=student('xyz1',10,'nss')
b=student('xyz2',20,'nso')
c=student('xyz3',30,'yrc')
d=student('xyz4',40,'nss')
e=student('xyz5',50,'nso')
f=student('xyz6',60,'yrc')
g=student('xyz7',70,'nss')
h=student('xyz8',80,'nso')
i=student('xyz9',90,'yrc')
j=student('xyz10',100,'nss')

iterable_student_list=iterable_student(a,b,c,d)
iterable_student_list.append(e)
iterable_student_list.append(f)
iterable_student_list.append(g)
iterable_student_list.append(h)
iterable_student_list.append(i)
iterable_student_list.append(j)

#iterator_student_list=iter(iterable_student_list)

for i in iterable_student_list:
    print(i)
