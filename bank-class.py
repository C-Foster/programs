class Account:
    def __init__(self, name, pin, balance, overdraft):
        self.name = name
        self.pin = str(pin)
        self.balance = float(balance)
        self.overdraft = float(overdraft)

    def credit(self, deposit):
        deposit = float(deposit)
        self.balance += deposit

    def debit(self, withdrawal):
        withdrawal = float(withdrawal)
        if float(self.balance - withdrawal) >= 0.00:
            self.balance -= withdrawal

    def get_balance(self):
        return self.balance

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_pin(self, new_pin):
        self.pin = new_pin

    def get_pin(self):
        return self.pin
    
    def set_overdraft(self, overdraft):
        self.overdraft = float(overdraft)

    def get_overdraft(self):
        return self.overdraft


# functions
def validate_names(f, s):
    """ Check for valid name inputs """
    
    if f.isalpha() and s.isalpha():
        if len(f) > 1 and len(s) > 1:
            return True
    return False


def validate_deposit(amt):
    """ Checks for a valid deposit """
    
    if type(amt) == float and amt > 0:
        return True
    else:
        return False


def validate_overdraft(amt):
    """ Checks for valid overdraft """
    
    if amt < 0.00 or amt > 250.00:
        return False
    elif amt == 0.00:
        return True
    elif amt % 10 == 0:
        return True


def check_withdrawal(bal, amt):
    """ Checks for a valid withdrawal as a multiple of £10.00 """
    
    if float(bal - amt) > 0.00 and amt % 10 == 0:
        return True
    else:
        return False


def create_account():
    """ Creates an account object from user inputs """
    
    forename = ''
    surname = ''
    pin = "x"
    init_deposit = 0.00
    init_overdraft = -1.00
    
    while not validate_names(forename, surname):
        forename = input("Enter your forename: ").title()
        surname = input("Enter your surname: ").title()
        if not validate_names(forename, surname):
            print("Invalid inputs.")

    full_name = "{} {}".format(forename, surname)

    while len(pin) != 4 and not pin.isnumeric():
        pin = input("Enter your desired 4-digit PIN: ")
        if len(pin) != 4 or not pin.isnumeric():
            print("Invalid input.")

    while not validate_deposit(init_deposit):
        init_deposit = float(input("Enter your inital deposit: "))
        if not validate_deposit(init_deposit):
            print("Invalid input.")

    while not validate_overdraft(init_overdraft):
        init_overdraft = float(input("Enter your desired overdraft.\n(Must be a multiple of £10 between £10 and £250) : "))
        if not validate_overdraft(init_overdraft):
            print("Invalid input")
    
    new_account = Account(full_name, pin, init_deposit, init_overdraft)
    # all_accounts.append(new_account)

    return new_account


def login():
    pass


# all_accounts = []

if __name__ == '__main__':
    main_running = True
    while main_running:
        menu_one = "Choose Operation:\n1. Create new account\n2. Login to existing account\n'Exit' to close\n"
        choice = input(menu_one).upper()

        if choice == "EXIT":
            break
        elif choice == "1":
            user_account = create_account()
        elif choice == "2":
            user_account = login()

        menu_two = "Choose operation:\n1. Deposit\n2. Withdraw\n3. Change name\n4. Change pin\n5. Change overdraft\n'Exit' to close\n"
        choice = input(menu_two).upper()

        if choice == "EXIT":
            break
        elif choice == "1":
            user_account.deposit(user_deposit)
        elif choice == "2":
            user_account.withdraw(user_withdrawal)
        elif choice == "3":
            user_account.set_name(user_new_name)
        elif choice == "4":
            user_account.set_pin(user_new_pin)
        elif choice == "5":
            user_account.set_overdraft(user_new_overdraft)
