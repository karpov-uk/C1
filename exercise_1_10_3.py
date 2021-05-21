class Client:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def get_client(self):
        return print(f'Клиент "{self.name}" - Баланс:{self.money} руб.')


clitnt1 = Client('Иван Петров', 50)
clitnt1.get_client()