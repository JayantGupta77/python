import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            print(f"Philosopher {self.index} is thinking.")
            time.sleep(random.uniform(1, 3))
            print(f"Philosopher {self.index} is hungry.")
            self.dine()

    def dine(self):
        fork1, fork2 = self.left_fork, self.right_fork

        # Prevent deadlock by ordering fork acquisition
        if self.index % 2 == 0:
            fork1, fork2 = fork2, fork1

        with fork1:
            print(f"Philosopher {self.index} picked up fork {fork1}")
            with fork2:
                print(f"Philosopher {self.index} picked up fork {fork2}")
                print(f"Philosopher {self.index} is eating.")
                time.sleep(random.uniform(2, 4))
                print(f"Philosopher {self.index} finished eating.")

# Number of philosophers
n = 5
forks = [threading.Semaphore(1) for _ in range(n)]
philosophers = [Philosopher(i, forks[i], forks[(i + 1) % n]) for i in range(n)]

for p in philosophers:
    p.start()