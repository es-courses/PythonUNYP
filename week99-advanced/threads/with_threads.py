
from time import sleep, time
import random 
from threading import Thread

def counter(name):
    for i in range(1, 6):
        print(f"{name}: {i}")
        sleep(random.randint(2, 5))



names = ["A", "B", "C", "D"]

threads = []

start = time()
for name in names:
    th = Thread(target=counter, args=name)
    threads.append(th)
    th.start()

for th in threads:
    th.join()
end = time()

print(f"Time elapled: {end - start}")