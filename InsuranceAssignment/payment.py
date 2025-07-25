from datetime import datetime

class Payments:
    def __init__(self, policyholder, amountPaid):
        self.policyholder = policyholder
        self.amountPaid = amountPaid
        self.date = datetime.now()

    def processPayment(self):
        self.policyholder.payments.append(self)

    def paymentReminder(self):
        print(f"Reminder: Payment due for {self.policyholder.fullName}")

    def penaltyPayment(self, penaltyAmount):
        print(f"Penalty of ${penaltyAmount} applied to {self.policyholder.fullName}")