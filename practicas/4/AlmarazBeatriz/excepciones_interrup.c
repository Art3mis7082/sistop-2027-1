#include <stdio.h>
#include <signal.h>
#include <stdlib.h>

// Manejador de interrupción (simulada con señal SIGINT)
void manejador_interrupcion(int sig) {
    printf("\n[Interrupción] Señal recibida: %d (Ctrl+C)\n", sig);
    printf("El flujo del programa fue interrumpido externamente.\n");
    exit(0); // Terminamos el programa
}

int main() {
    // Registrar el manejador para la señal SIGINT
    signal(SIGINT, manejador_interrupcion);

    printf("=== Comparación Excepciones vs Interrupciones ===\n");

    //Se debe de comentar las líneas de la 22 a la 26 para poder 
    //ejecutar el ejemplo de interrupción

    // Ejemplo de excepción: división por cero (en tiempo de ejecución)
    int a = 10, b = 0;
    printf("\n[Excepción] Intentando dividir %d entre %d...\n", a, b);

    int c = a / b; 
    printf("Resultado: %d\n", c);

    
    // Ejemplo de interrupción: esperar señal externa
    printf("\n[Interrupción] Programa en espera. Presiona Ctrl+C para interrumpir.\n");
    while (1) {
        // Loop infinito esperando la señal
    }

    return 0;
}
