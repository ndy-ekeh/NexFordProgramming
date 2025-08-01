from product import product
from payment import Payments
from policyHolderClass import policyHolder

# Create products
product1 = product(1, "Life Insurance", 20000)
product2 = product(2, "Health Insurance", 10000)

# Create policyholders
ph1 = policyHolder(101, "Ndubisi Ekeh", "ndyknight@gmail.com")
ph2 = policyHolder(102, "Esther Adewale", "estherAdewale@gmail.com")

# Register products
ph1.createproduct(product1)
ph2.createproduct(product2)

# Process payments 
payment1 = Payments(ph1, product1.price)
payment1.processPayment()

payment2 = Payments(ph2, product2.price)
payment2.processPayment()

# Display details
print("=== Policyholder 1 ===")
ph1.accountDetails()

print("\n=== Policyholder 2 ===")
ph2.accountDetails()