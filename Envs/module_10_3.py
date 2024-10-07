from random import randint
import threading
import time


class Bank():

    def __init__(self):
        self.balance = int(0)
        self.lock = threading.Lock()

    def deposit(self):
        count_transaction = 100
        for _ in range(count_transaction + 1):
            try:
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                else:
                    num = randint(50, 500)
                    self.balance = self.balance + num
                    print(f"Пополнение: {num}. Баланс: {self.balance}")
                    time.sleep(0.001)
            finally:
                self.lock.release()


    def take(self):
        count_transaction = 100
        for _ in range(count_transaction + 1):
            num = randint(50, 500)
            print(f"Запрос на {num}")
            with self.lock:
                if num <= self.balance:
                    self.balance = self.balance - num
                    print(f"Снятие: {num}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
