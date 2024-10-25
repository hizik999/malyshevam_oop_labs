class Bank:
    def __init__(self):
        self.clients = {}

    def create_account(self, account_number, initial_balance):
        if account_number in self.clients:
            print("Уже существует счет с таким номером")
        else:
            self.clients[account_number] = initial_balance

    def make_deposit(self, account_number, amount):
        if account_number in self.clients:
            self.clients[account_number] += amount
        else:
            print("Счет с таким номером не существует")

    def make_withdrawal(self, account_number, amount):
        if account_number in self.clients:
            if self.clients[account_number] >= amount:
                self.clients[account_number] -= amount
            else:
                print("Недостаточно средств на счету")
        else:
            print("Счет с таким номером не существует")

    def check_balance(self, account_number):
        if account_number in self.clients:
            print(f"Текущий баланс счета {account_number} составляет: {self.clients[account_number]}")
        else:
            print("Счет с таким номером не существует")


bank = Bank()

print("Создаем учетные записи клиентов:")
bank.create_account(123456, 0)
bank.create_account(789012, 1000)
bank.create_account(345678, 500)

print("Вносим депозиты на счета клиентов:")
bank.make_deposit(123456, 500)
bank.make_deposit(123456, 500)
bank.make_deposit(123456, 500)
bank.make_deposit(123456, 500)
bank.make_deposit(789012, 100)
bank.make_deposit(345678, 200)

print("Снимаем средства со счетов клиентов:")
bank.make_withdrawal(123456, 200)
bank.make_withdrawal(789012, 50)
bank.make_withdrawal(345678, 150)

print("Проверяем баланс счетов клиентов:")
bank.check_balance(123456)
bank.check_balance(789012)
bank.check_balance(345678)