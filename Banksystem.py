# Task 03 - Banking Console Application
# Kiran Academy - Python

# starting balance
balance = 10000

print("Welcome to Kiran Bank")
print("Opening Balance: ₹" + str(balance))

# menu keeps repeating until user chooses 4
while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        # just show the balance
        print("Current Balance: ₹" + str(balance))

    elif choice == "2":
        amount = input("Enter deposit amount: ")

        # check if the user typed a proper number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                balance = balance + amount
                print("Deposit successful.")
                print("Updated Balance: ₹" + str(balance))
            else:
                print("Invalid amount. Amount must be greater than 0.")
        else:
            print("Invalid amount. Please enter a positive number.")

    elif choice == "3":
        amount = input("Enter withdrawal amount: ")

        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print("Invalid amount. Amount must be greater than 0.")
            elif amount > balance:
                # not enough money, balance stays the same
                print("Transaction failed: Insufficient balance.")
                print("Current Balance: ₹" + str(balance))
            else:
                balance = balance - amount
                print("Withdrawal successful.")
                print("Updated Balance: ₹" + str(balance))
        else:
            print("Invalid amount. Please enter a positive number.")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")