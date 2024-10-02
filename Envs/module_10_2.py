import time
from threading import Thread, Lock

class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.enemy = 100
        self.day = 0


    def run(self):
        while self.enemy > 0:
            self.day += 1
            self.enemy -= self.power
            print(f"{self.name} сражается {self.day} день(дня)..., осталось {self.enemy} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {self.day} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")