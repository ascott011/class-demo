from bank_account import Account

def main():
    acct = Account('Alex', 100)
    acct.withdraw(10)
    print(f"Alex's balance is {acct.balance}")

if __name__ == "__main__":
    main()
