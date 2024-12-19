"""
Objectives
    - improving the student's skills in operating with the getter, setter, and deleter methods;
    - improving the student's skills in creating their own exceptions.
"""


class AccountException(Exception):
    pass

class Account:
    def __init__(self):
        self.__account_number = 123
        self.__balance = 0

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @account_number.setter
    def account_number(self, account_number):
        raise AccountException(
            "It's not possible to change the account number!"
        )

    @balance.setter
    def balance(self, amount):
        # Deposit
        if amount > 0:
            if amount > 100_000:
                print(f"Deposit greater than 100_000: {amount}")
            self.__balance += amount

        # Withdrawal
        elif amount < 0:
            if self.__balance + amount < 0:
                raise AccountException("Insufficient balance!")

            if abs(amount) > 100_000:
                print(f"Withdrawal greater than 100_000: {abs(amount)}")

            self.__balance += amount
        else:
            print("No operation performed!")

    @balance.deleter
    def balance(self):
        if self.__balance > 0:
            raise AccountException('Can not delete account as long it is not empty')
        self.__balance = None



print("Creating an Account...")
account = Account()
print("Account created successfully!")

print("Account balance:", account.balance)

print("Setting the balance to 1000...")
account.balance += 1_000
print("Account balance:", account.balance)

try:
    print("Trying to set the balance to -200...")
    account.balance -= 1_200
    print("Account balance:", account.balance)
except AccountException as e:
    print(e)

try:
    print("Trying to set a new value for the account number...")
    account.account_number = 321
except AccountException as e:
    print(e)

print("Trying to deposit 1.000.000")
account.balance += 1_000_000
print("Account balance:", account.balance)

try:
    print("Trying to delete the account...")
    del account.balance
except AccountException as e:
    print(e)
