from abc import ABC, abstractmethod
import datetime

# Abstract Class (Abstraction)
class BankAccount(ABC):
    @abstractmethod
    def get_account_type(self):
        pass
    
    @abstractmethod
    def calculate_interest(self):
        pass

# Base Class with Encapsulation
class Account(BankAccount):
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        # Private attributes (Encapsulation)
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__transactions = []
        
    # Getter methods (Controlled access - Encapsulation)
    def get_account_number(self) -> str:
        return self.__account_number
    
    def get_account_holder(self) -> str:
        return self.__account_holder
    
    def get_balance(self) -> float:
        return self.__balance
    
    # Methods to modify private attributes (Encapsulation)
    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposit: +${amount:.2f} on {datetime.datetime.now()}")
            return True
        return False
    
    def withdraw(self, amount: float) -> bool:
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(f"Withdrawal: -${amount:.2f} on {datetime.datetime.now()}")
            return True
        return False
    
    def get_transactions(self) -> list:
        return self.__transactions.copy()
    
    # Abstract method implementation
    def get_account_type(self) -> str:
        return "Generic Account"

# Subclass 1 - Savings Account (Inheritance)
class SavingsAccount(Account):
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        super().__init__(account_number, account_holder, initial_balance)
        self.__interest_rate = 0.02  # 2% annual interest
        
    # Method overriding (Polymorphism)
    def calculate_interest(self) -> float:
        interest = self.get_balance() * self.__interest_rate / 12  # Monthly interest
        self.deposit(interest)
        return interest
    
    def get_account_type(self) -> str:
        return "Savings Account"

# Subclass 2 - Checking Account (Inheritance)
class CheckingAccount(Account):
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        super().__init__(account_number, account_holder, initial_balance)
        self.__overdraft_limit = 100.0
        
    # Method overriding (Polymorphism)
    def calculate_interest(self) -> float:
        return 0.0  # Checking accounts typically don't earn interest
    
    def withdraw(self, amount: float) -> bool:
        if amount > 0 and (self.get_balance() + self.__overdraft_limit) >= amount:
            self._Account__balance -= amount  # Accessing protected attribute
            self._Account__transactions.append(f"Withdrawal: -${amount:.2f} on {datetime.datetime.now()}")
            return True
        return False
    
    def get_account_type(self) -> str:
        return "Checking Account"

# Demonstration
def main():
    # Create accounts
    savings = SavingsAccount("SA001", "John Doe", 1000.0)
    checking = CheckingAccount("CA001", "Jane Smith", 500.0)
    
    # Demonstrate Encapsulation
    print(f"Savings Account Holder: {savings.get_account_holder()}")
    print(f"Initial Savings Balance: ${savings.get_balance():.2f}")
    
    # Demonstrate operations
    savings.deposit(500.0)
    savings.withdraw(200.0)
    checking.deposit(300.0)
    checking.withdraw(700.0)  # Within overdraft limit
    
    # Demonstrate Polymorphism
    accounts = [savings, checking]
    for account in accounts:
        print(f"\nAccount Type: {account.get_account_type()}")
        print(f"Interest Earned: ${account.calculate_interest():.2f}")
        print(f"Current Balance: ${account.get_balance():.2f}")
        
        # Show transaction history
        print("Transaction History:")
        for transaction in account.get_transactions():
            print(f"  - {transaction}")

if __name__ == "__main__":
    main()