from time import sleep, time
import random 

def counter(name):
    for i in range(1, 6):
        print(f"{name}: {i}")
        sleep(random.randint(2, 5))



names = ["A", "B", "C", "D"]

start = time()
for name in names:
    counter(name)
end = time()

print(f"Time elapled: {end - start}")