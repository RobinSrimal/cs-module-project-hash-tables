# Your code here
import random
import math

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


cache = {1:1}

def factorial(x):
    
    if x in cache:
        
        return cache[x]
    
    else:

        for i in range(int(max(cache.keys())) + 1, int(x) + 1):

            cache[i] = i * cache[i-1]

        return cache[x]

    
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    lookup = {}

    for i in range(2,15):

        for k in range(3,7):

            v = math.pow(i, k)
            v = factorial(v)
            v //= (i + k)
            v %= 982451653

            lookup[(i,k)] = v
            print(lookup)
    print(lookup[(x,y)])
    return lookup[(x,y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
