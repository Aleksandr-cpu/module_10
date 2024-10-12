import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            num= random.randint(50, 500)
            self.balance += num
            print(f"Пополнение: {num}. Баланс: {self.balance}")

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)
    def take(self):
        for _ in range(100):
            num = random.randint(50, 500)
            print(f"Запрос на {num}")
            if num >= self.balance:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            else:
                self.balance -= num
                print(f"Снятие: {num}. Баланс: {self.balance}")


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
