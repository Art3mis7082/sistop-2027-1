#!/usr/bin/python3
import os
import time
import signal

def manejador(sig, frame):
    print(f'Recibí una señal {sig}')
    if sig == signal.SIGCLD:
        res = os.waitpid(-1, os.WNOHANG)
        print(f'Venía del proceso: {res}. Ya la procesé.')
    elif sig == signal.SIGINT or sig == signal.SIGKILL:
        print('Me enviaron una señal de interrupción (SIGINT)')
        print('Me voy limpiamente.')
        exit(1)
    elif sig == signal.SIGWINCH:
        print('Cambió el tamaño de la pantalla. Seguimos normal.')

signal.signal(signal.SIGCLD, manejador)
signal.signal(signal.SIGINT, manejador)
signal.signal(signal.SIGWINCH, manejador)
signal.signal(signal.SIGKILL, manejador)

mi_pid = os.getpid()
print(f'Mi PID es: {mi_pid}')

# Separamos el flujo de proceso en dos: un “padre” y un “hijo”
otro_pid = os.fork()

if otro_pid == 0:
    # Proceso hijo
    print(f'Este es el proceso hijo. Mi PID es {os.getpid()}')
    time.sleep(5)
    print('Y como no tengo nada más que hacer... ¡Me voy!')
    exit(0)

elif otro_pid > 0:
    # Proceso padre
    print(f'Este es el proceso padre. Mi PID es {os.getpid()}. El hijo es {otro_pid}')
    print('Te doy tiempo para que hagas tu demostración...')
    time.sleep(60)

else: # otro_pid < 0
    # Si el resultado de fork() es < 0, indica error.
    print(f'!!! ERROR ejecutando el fork: {otro_pid}')

