import math
import balayage

def fonction(x):

    return x**2 -1
interval = balayage(fonction, 2,3,h=0.1)

print(interval)

