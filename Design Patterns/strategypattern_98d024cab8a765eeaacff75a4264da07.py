from abc import ABC,abstractmethod

class percent_offer(ABC):

    @abstractmethod
    def discount(self):
        pass

class percent_10_offer(percent_offer):

    def discount(self):
        return 0.1

class percent_20_offer(percent_offer):

    def discount(self):
        return 0.2

class offer:

    def __init__(self,price,offer_name):
        self.price=price
        self.offer=offer_name()
    
    def calculate_amt(self):
        discount_val= self.price*self.offer.discount()
        print(discount_val)
        print(f'total amt: {self.price-discount_val}')

o=offer(5000,percent_10_offer)
o.calculate_amt()

    
