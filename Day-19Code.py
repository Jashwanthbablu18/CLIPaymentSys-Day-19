# Day 19 - Polymorphism & Encapsulation: Payment System


# This is a UserWallet class with name and balance params. This encapsulates the balance.
class UserWallet:
    def __init__(self, name, balance):
        self.name = name

        # This encapsulates the balance attr. An attribute/method in python can be encapsulated through the convention of using '_' or '__' as a prefix to attribute/method.
        self.__balance = balance  # encapsulated
    
    # This method is used to return the current balance of an account
    def get_balance(self):
        return self.__balance

    # This method is used to deduct the amount from an account
    def deduct(self, amount):
        # It will deduct the amount if there is less than or equal to balance, else won't deducts.
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    # This method is used to display the current account balance with nicely formatted string format.
    def show_balance(self):
        print(f"💰 {self.name}'s Wallet Balance: ₹{self.__balance}")


# This is the base class and in that wallet parameter is expecting to be an instance of UserWallet class and amount was initialized as float
# And by calling this method raises error, this is used only for overriding purpose only. 
class PaymentMethod:
    def pay(self, wallet: UserWallet, amount: float):
        raise NotImplementedError("Subclasses must override this method")


# Polymorphic subclasses

# The UPIPayment class is inheriting the PaymentMethod class and implementing the pay() method which will deduct amount from wallet
class UPIPayment(PaymentMethod):
    def pay(self, wallet: UserWallet, amount: float):
        print("🔄 Paying via UPI...")
        if wallet.deduct(amount):
            print(f"✅ UPI Payment of ₹{amount} successful.")
        else:
            print("❌ UPI Payment failed: Insufficient balance.")

# The CardPayment class is inheriting the PaymentMethod class and implementing the pay() method which will deduct amount from wallet
class CardPayment(PaymentMethod):
    def pay(self, wallet: UserWallet, amount: float):
        print("💳 Paying via Card...")
        if wallet.deduct(amount):
            print(f"✅ Card Payment of ₹{amount} successful.")
        else:
            print("❌ Card Payment failed: Insufficient balance.")


# main
def main():
    print("💸 Day 19 - Payment System using Polymorphism & Encapsulation\n")

    # Creates instance of UserWallet class
    wallet = UserWallet("Jayesh", 2000)

    # Calls show_balance() to display balance
    wallet.show_balance()

    # Polymorphic behavior by creating instances for UPIPayment and CardPayment.
    upi = UPIPayment()
    card = CardPayment()

    # deducting 500/- from wallet via upi and displaying balance
    print("\n--- UPI Transaction ---")
    upi.pay(wallet, 500)
    wallet.show_balance()

    # deducting 1800/- from wallet via card and displaying balance (But fails)
    print("\n--- Card Transaction ---")
    card.pay(wallet, 1800)  # will fail
    wallet.show_balance()

    # deducting 1300/- from wallet via card and displaying balance
    print("\n--- Card Transaction (retry) ---")
    card.pay(wallet, 1300)
    wallet.show_balance()


# calling main() to starting execution of program
if __name__ == "__main__":
    main()
