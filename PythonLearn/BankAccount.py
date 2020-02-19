Customer1 = {'First Name': 'Fillip', 'Last Number': 'Keitaro', 'Account Number': '00001', 'Balance': 5, 'age': 18,
             'contact': 'filip@gmail.com'}

print(Customer1)

def check_Balance(customerDict):
    print("The Balance is: {}".format(customerDict['Balance']))


def Deposit(customerDict, Amount):
    customerDict['Balance'] += Amount
    print('New Balance is: {}'.format(customerDict['Balance']))


def Withdrawal(customerDict, Amount):
    if Amount > customerDict['Balance']:
        print('You do not have enough money. Input Amount smaller or equal: {}'.format(customerDict['Balance']))
    else:
        print('Withdrawal successfully!!!!')

check_Balance(Customer1)
Deposit(Customer1, 1)
Withdrawal(Customer1,2)
