import threading
import time
import random

NUM_PHILOSOPHERS = 5

forks = []
for i in range(NUM_PHILOSOPHERS):
    forks.append(threading.Semaphore(1))

dining_limit = threading.Semaphore(NUM_PHILOSOPHERS - 1)

class Philosopher:
    def __init__(self, philosopher_id):
        self.philosopher_id = philosopher_id

    def think(self):
        think_duration = random.choice(range(1, 4))
        print("Philosopher {} is thinking for {} seconds.\n".format(self.philosopher_id, think_duration))
        time.sleep(think_duration)

    def eat(self):
        eat_duration = random.choice(range(1, 4))
        print("Philosopher {} is eating for {} seconds.\n".format(self.philosopher_id, eat_duration))
        time.sleep(eat_duration)

    def perform_actions(self):
        while True:
            self.think()

            dining_limit.acquire()

            if self.philosopher_id % 2 == 0:
                forks[self.philosopher_id].acquire()
                print("Philosopher {} picked up left fork {}.\n".format(self.philosopher_id, self.philosopher_id))
                forks[(self.philosopher_id + 1) % NUM_PHILOSOPHERS].acquire()
                print("Philosopher {} picked up right fork {}.\n".format(self.philosopher_id, (self.philosopher_id + 1) % NUM_PHILOSOPHERS))
            else:
                forks[(self.philosopher_id + 1) % NUM_PHILOSOPHERS].acquire()
                print("Philosopher {} picked up right fork {}.\n".format(self.philosopher_id, (self.philosopher_id + 1) % NUM_PHILOSOPHERS))
                forks[self.philosopher_id].acquire()
                print("Philosopher {} picked up left fork {}.\n".format(self.philosopher_id, self.philosopher_id))

            self.eat()

            forks[self.philosopher_id].release()
            print("Philosopher {} put down left fork {}.\n".format(self.philosopher_id, self.philosopher_id))
            forks[(self.philosopher_id + 1) % NUM_PHILOSOPHERS].release()
            print("Philosopher {} put down right fork {}.\n".format(self.philosopher_id, (self.philosopher_id + 1) % NUM_PHILOSOPHERS))

            dining_limit.release()

if __name__ == "__main__":
    philosopher_threads = []
    for philosopher_index in range(NUM_PHILOSOPHERS):
        philosopher = Philosopher(philosopher_index)
        thread = threading.Thread(target=philosopher.perform_actions)
        philosopher_threads.append(thread)
        thread.start()

    for thread in philosopher_threads:
        thread.join()