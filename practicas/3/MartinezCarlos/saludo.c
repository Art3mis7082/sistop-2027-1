#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc > 1) {
        printf("¡Hola, %s! Bienvenido al sistema.\n", argv[1]);
    } else {
        printf("¡Hola, usuario anónimo!\n");
    }
    return 0;
}
