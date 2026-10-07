#!/usr/bin/python3
import threading
import time
import random

num_filosofos = 5
multiplex = threading.Semaphore(num_filosofos - 1)
palillos = [threading.Semaphore(1) for i in range(num_filosofos)]

def piensa(n):
    print(' ' * n + f'🙂{n}: Pensando')
    #time.sleep(random.random())
    print(' ' * n + f'🙂{n}: Hmmm... ¡Hace hambre!')

def come(n):
    levanta_palillo(n, n)
    levanta_palillo(n, (n+1) % num_filosofos )
    print(' '*n + f'🍚{n} ¡A comer!')
    #time.sleep(random.random())
    print(' '*n + f'🍚{n} ¡Qué satisfactorio!')
    suelta_palillo(n, n)
    suelta_palillo(n, (n+1) % num_filosofos)

def levanta_palillo(num_fil, n):
    palillos[n].acquire()
    print(' '*num_fil + f'🥢{num_fil} levantó el palillo {n}')

def suelta_palillo(num_fil, n):
    palillos[n].release()
    print(' '*num_fil + f'🥢{num_fil} soltó el palillo {n}')

def filosofo(n):
    while True:
        piensa(n)
        with multiplex:
            come(n)

for i in range(num_filosofos):
    threading.Thread(target=filosofo,args=[i]).start()
