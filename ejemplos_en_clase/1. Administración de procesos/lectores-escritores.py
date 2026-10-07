#!/usr/bin/python3
import threading
import time
import random

num_lectores = 30
num_escritores = 2

pizarron = ''
pizarron_mutex = threading.Semaphore(1)
cont_lect = 0
mutex_cont = threading.Semaphore(1)
torniquete = threading.Semaphore(1)

def lector(num):
    global pizarron
    global cont_lect
    while True:
        torniquete.acquire()
        torniquete.release()
        print(f'    L{num}: Pasado el umbral de la puerta...')

        time.sleep(2*random.random())
        mutex_cont.acquire()
        cont_lect += 1
        if cont_lect == 1:
            pizarron_mutex.acquire()
            print(f'    L{num}: Soy el primero. ¡Prendo la luz!')
        mutex_cont.release()

        print(f'    L{num}: Entrando a clase...')
        print(f'    L{num}: Copiando del pizarrón: {pizarron}. Hay {cont_lect} lectores.')
        time.sleep(random.random())

        mutex_cont.acquire()
        cont_lect -= 1
        if cont_lect == 0:
            print(f'    L{num}: Soy el último. ¡Apago la luz!')
            pizarron_mutex.release()
        mutex_cont.release()
        print(f'    L{num}: A disfrutar de una hora libre')
        time.sleep(5*random.random())


def escritor(num):
    global pizarron
    textos = ['Una gran verdad', 'Mucha sabiduría', 'Ideas muy interesantes',
              'Alguna tontería ocasional']
    while True:
        # Obtiene el mutex sobre el pizarrón y lo modifica
        print(f'E{num}: Entrando')
        torniquete.acquire()
        print(f'E{num}: Tengo el torniquete')
        pizarron_mutex.acquire()
        print(f'E{num}: Escribiendo')
        time.sleep(random.random())
        pizarron = f'E{num}: {random.choice(textos)}'
        pizarron_mutex.release()
        torniquete.release()

        # Hora de tomar un café...
        print(f'E{num}: ¡Al café!')
        time.sleep(random.random() * 5)

for i in range(num_lectores):
    threading.Thread(target=lector, args=[i]).start()

for i in range(num_escritores):
    threading.Thread(target=escritor, args=[i]).start()

