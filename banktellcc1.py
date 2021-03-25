checking_balance = 0
savings_balance = 0


def check_balance(account_type, checking_balance, savings_balance):
    if account_type == 'checking':
        balance = savings_balance

    elif account_type == 'savings':
        balance = checking_balance
    else:
        print('Unsuccessful, please enter \"checking\" or \"savings\'')

    balance_statement = 'Your ' + account_type + ' balance is ' + str(balance)
    return balance_statement


print(check_balance('checking', checking_balance, savings_balance))

print(check_balance('savings', checking_balance, savings_balance))


def make_deposit(account_type, amount, checking_balance, savings_balance):
    deposit_status: str = ''
    if amount <= 0:
        print("unsuccessful, please enter an amount greater than 0")
    else:
        if account_type == 'savings':
            savings_balance += amount
            deposit_status = 'succesfull'

        elif account_type == 'checking':
            checking_balance += amount
            deposit_status = 'successful'
        else:
            print("Unsuccessful, please enter \"checking\" or \"savings\"")

    deposit_statement = 'Deposit of ' + str(amount) + ' to your ' + account_type + ' account ' + deposit_status
    print(deposit_statement)
    return checking_balance, savings_balance


savings_balance, checking_balance = make_deposit('savings', 1, checking_balance, savings_balance)

print(check_balance('savings', checking_balance, savings_balance))

savings_balance, checking_balance = make_deposit('checking', 2000, checking_balance, savings_balance)
print(check_balance('checking', checking_balance, savings_balance))
