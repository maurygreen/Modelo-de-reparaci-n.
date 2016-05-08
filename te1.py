import random
import math


def fail_simulation(n,s):
    t = 0
    r = 0
    trep = 2**64-1 # officialy INF
    t_list = []
    for _ in xrange(n):
        t_list.append(random.expovariate(1))

    t_list.sort()

    while True:
        # t1 < tmax
        t1 = t_list[0]
        
        if t1 < trep:
            t = t1
            r += 1
            if r == s+1:
                return t
            elif r < s+1:
                x = random.expovariate(1)
                t_list.pop(0)
                t_list.append(t+x)
                t_list.sort()
            if r == 1:
                y = random.expovariate(8)
                trep = t + y
        else:
            t = trep
            r -= 1
            if r > 0:
                y = random.expovariate(8)
                trep = t + y
            elif r == 0:
                trep = 2**64-1


def fail_simulation2(n,s):
    t = 0
    r = 0
    trep = [2**64-1, 2**64-1]
    t_list = []
    for _ in xrange(n):
        t_list.append(random.expovariate(1))

    t_list.sort()

    while True:
        # t1 < tmax
        t1 = t_list[0]
        mint = min(trep)
        if t1 < mint:
            t = t1
            r += 1
            if r == s+1:
                return t
            elif r < s+1:
                x = random.expovariate(1)
                t_list.pop(0)
                t_list.append(t+x)
                t_list.sort()
            if r <= 2 and r > 0:
                if trep[0] == 2**64-1:
                    y = random.expovariate(8)
                    trep[0] = t + y
                elif trep[1] == 2**64-1:
                    y = random.expovariate(8)
                    trep[1] = t + y 
        else:
            t = mint
            r -= 1
            if r > 1:
                y = random.expovariate(8)
                trep[trep.index(mint)] = t + y
            elif r <= 1: 
                trep[trep.index(mint)] = 2**64-1


def esp(n,s,nz):
    e = 0
    v = 0
    for _ in xrange(nz):
        x = fail_simulation(n,s)
        e += x
        v += x**2

    e = e/nz
    v = v/nz
    return (e,v-e**2)


def esp2(n,s,nz):
    e = 0
    v = 0
    for _ in xrange(nz):
        x = fail_simulation2(n,s)
        e += x
        v += x**2
    e = e/nz
    v = v/nz
    return (e,v-e**2)


