import random
import math

from threading import Thread

def main():
    pi = 0
    pt = 100000000

    print("\nCalculo do PI Iniciado\n")

    for i in range(0, pt):
        # Generate random x, y in [0, 1].
        x2 = random.random()**2
        y2 = random.random()**2
        # Increment if inside unit circle.
        if math.sqrt(x2 + y2) < 1.0:
            pi += 1

    pi = (float(pi) / pt) * 4

    print("\nPI é igual a: %f \n"%pi)

t = Thread(target=main, args=())
t.start()