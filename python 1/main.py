def show_balance():
    print(f"Your balance is {balance:.2f}")
def deposit():
    global balance
    while True:
        amount = float(input("Enter an amount (1-10000):"))
        if 0 < amount <= 10000:
            balance += amount
            print(f"Deposit successful! Your new balance is: {balance:.2f}")
            break
        else:
            print("Please enter an amount from (1-10000):")

def withdraw():
    global balance
    while True:
        amount = float(input("Enter an amount to withdraw (1-10000):"))
        if 0 < amount <= 10000:
            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successful! Your new balance is: {balance:.2f}")
                break
            else:
                print("Insufficient funds!")
        else:
            print("Please enter an amount from (1-10000):")

balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input('Enter number(1-4):')

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Please enter a number from (1-4)")
        continue
