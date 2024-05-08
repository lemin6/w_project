class Product:
    def __init__(self, name_product, category, price, description, date):
        self.name_product = name_product
        self.category = category
        self.price = price
        self.description = description
        self.date = date
    def create(self, quantity):
        total_price = self.price * quantity
        return f"Total price: {total_price}"

product1 = Product('acer', 'computer', 6000, 'gfdgdsf', 2020)

print(product1.create(5))

