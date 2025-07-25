class product:
    def __init__(self,productID,productName,price):
        self.productID = productID
        self.productName = productName
        self.price = price
        self.status = 'Available'

    def productUpdate(self, productName=None, price=None):
        if productName:
            self.productName = productName
        if price:
            self.price = price

    def productSuspend(self):
        self.status = 'Suspended'