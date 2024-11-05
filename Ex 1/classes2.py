class Digital:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.type = None
        self.pack = None
        self.paid = None
        self.number = None

    def new_customer(self, name, type, pack, is_paid, number):
        self.name = name
        self.type = type
        self.pack = pack
        self.paid = is_paid
        self.number = number

    def change_pack(self, new_pack):
        self.pack = new_pack

    def paid_status(self):
        if self.paid == 'yes':
            return "the customer has paid"
        else:
            return "the bill is not paid"
        
    def display(self):
        return (f"""
        customer id : {self.id}
        the customer name is : {self.name}
        Setup Box type is {self.type}
        package : {self.pack}
        paid status is {self.paid}
        Customer number is {self.number}""")

if '__main__' == __name__:
    c1 = Digital(1)
    c1.new_customer(input("enter you name : "), "hd", "basic", "paid", 9998888990)
    details = c1.display()
    print(details)