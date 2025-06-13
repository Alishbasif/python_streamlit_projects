class Bank:
    bank_name = "HBL"

    @classmethod
    def change_bank_name(cls,name):
         cls.bank_name = name
         return cls.bank_name
           

b1 = Bank()
print(Bank.bank_name)
print(Bank.change_bank_name("State Bank"))  
print(Bank.bank_name)      


