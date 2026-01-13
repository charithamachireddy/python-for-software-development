
balance = 1000  # initial balance

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your current balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount deposited successfully.")

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Please collect your cash.")
        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")
