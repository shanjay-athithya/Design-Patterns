class Product:
    def __init__(self, brand, price, quantity):
        self.brand = brand
        self.price = price
        self.quantity = quantity
    
    def display(self):
        return (f'''the brand name is : {self.brand}
                    the price is : {self.price}
                    the quantity is : {self.quantity}''')

class ElectronicProduct(Product):
    def __init__(self, brand, price, quantity, type, range):
        super().__init__(brand, price, quantity)
        self.type = type
        self.range = range
    
    def display(self):
        return (f'''the brand name is : {self.brand}
                    the price is : {self.price}
                    the quantity is : {self.quantity}
                    the type of the product is : {self.type}
                    the range of the product is : {self.range}''')
        
if __name__ == '__main__':
    # Case 1: Creating an ElectronicProduct
    e = ElectronicProduct("Sony", 499, 10, "Smartphone", "Pro")
    
    # Case 2: Displaying the details of the ElectronicProduct
    print("Electronic Product Details:")
    print(e.display())

    # Case 3: Creating a regular Product
    p = Product("Samsung", 799, 5)

    # Case 4: Displaying the details of the regular Product
    print("\nProduct Details:")
    print(p.display())

    # Case 5: Creating an ElectronicProduct with user input
    brand_name = input("Enter the brand name: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    product_type = input("Enter the type of electronic product: ")
    product_range = input("Enter the variant: ")
    e2 = ElectronicProduct(brand_name, price, quantity, product_type, product_range)

    # Displaying the details of the second ElectronicProduct
    print("\nSecond Electronic Product Details:")
    print(e2.display())

    # Case 6: Creating a regular Product with user input
    brand_name = input("Enter the brand name: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    p2 = Product(brand_name, price, quantity)

    # Displaying the details of the second Product
    print("\nSecond Product Details:")
    print(p2.display())
