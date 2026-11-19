product_name, product_code = input().split()
product_code = int(product_code)

class Products:
    def __init__(self, product_name, product_code):
        self.pn = product_name
        self.pc = product_code

product1 = Products(product_name, product_code)
product2 = ("codetree", 50)

print("product", product2[1], "is", product2[0])
print("product", product1.pc, "is", product1.pn)