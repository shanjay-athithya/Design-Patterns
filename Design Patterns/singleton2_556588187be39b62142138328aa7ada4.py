class Result :

    s_instance = None

    def __init__(self) :
        self.IA = 0.4 + 1
        self.EA = 0.6
        print('hi')

    def __new__(cls,*args,**kwargs):
        if cls.s_instance is None :
            cls.s_instance = super().__new__(cls,*args,**kwargs)
        print('last statement')
        return cls.s_instance
        
r = Result()
r2 = Result()

print(r,r2)
print(r2.IA)
print(r.IA)