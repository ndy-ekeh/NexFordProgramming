class policyHolder:
    def __init__(self,holderID,fullName,email):
        self.holderID = holderID
        self.fullName = fullName
        self.email = email
        self.status = 'Active'
        self.payments = []
        self.products = []

    def createproduct(self, product):
        self.products.append(product)

    def suspend(self):
        self.status = 'Suspended'

    def reactivate(self):
        self.status = 'Active'

    def accountDetails(self):
        print(f"Policyholder ID: {self.holderID}")
        print(f"fullname: {self.fullName}")
        print(f"Email: {self.email}")
        print(f"Status: {self.status}")
        print("Products Purchased:")

        for product in self.products:
            print(f"  - {product.productName} (${product.price})")
        print("Payments made:")
        
        for payment in self.payments:
            print(f"  - {payment.amountPaid} on {payment.date}")