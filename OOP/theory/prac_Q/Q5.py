# Add debit/credit logs and private balance.


class bank:
    def __init__(self, balance, credit, debit):
        self.__balance = balance  #private
        self.credit = credit
        self.debit = debit

    def crd(self):
        self.__balance = self.__balance + self.credit
        print("credited amount is:", self.credit)
        print("total amount is:", self.__balance)

    def deb(self):
        self.__balance = self.__balance - self.debit
        print("Debited amount is:", self.debit)
        print("total amount is:", self.__balance)


b1 = bank(25000, 3400,7800)
b1.crd()
b1.deb()

try:
    print(b1.__balance)
except:
    print("Balance is private")

print("Credited amount is:", b1.credit)
print("Debited amount is:", b1.debit)
