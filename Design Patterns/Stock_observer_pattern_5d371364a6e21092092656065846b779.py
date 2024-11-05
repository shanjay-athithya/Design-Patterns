class Stock:

    def __init__(self,name,val):
        self.obs_list=[]
        self.name=name
        self.value=val

    def __str__(self):
        return f'{self.name}:{self.value}'

    def attach(self,obs):
        self.obs_list.append(obs)

    def detach(self,obs):
        self.obs_list.remove(obs)

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self,new_val):
        self.value = new_val
        self.notify()

    def notify(self):
        for x in self.obs_list:
            x.update(self)

class Stock_info:

    def __init__(self):
        ...
        

    def update(self,stock):
        print(stock)
        
if __name__=='__main__':
    s=Stock('HCL',1050)
    
    

              
