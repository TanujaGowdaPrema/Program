#Create an Interface class ‘Bank’ with an abstract method ‘getBalance’.
# $100 , $150 and $200 are deposited in banks A, B and C respectively. 
# ‘BankA’, ‘BankB’ and ‘BankC’ are subclasses of class ‘Bank’, each having a method named ‘getBalance’.
# Call this method by creating an object of each of the three classes.

from abc import  ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def get_balance(self):
        pass
class Bank_A(Bank):
    def get_balance(self):
        print("Deposited for BankA is $100")           
class Bank_B(Bank):
    def get_balance(self):
        print("Deposited for BankB is $150")          
class Bank_C(Bank):
    def get_balance(self):
        print("Deposited for BankC is $200")

BA1=Bank_A()
BA1.get_balance()

BA2=Bank_B()
BA2.get_balance()

BA3=Bank_C()
BA3.get_balance()




        
