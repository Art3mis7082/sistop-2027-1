#include <stdio.h>
char nombre[20];

int main(){
	printf("Hi , esta es la primera parte de la practica 3 de SO.\n");
	printf("Por favor ingresa tu nombre:");
	fgets(nombre, sizeof(nombre),stdin);
	printf("Mucho gusto, %s",nombre);
return 0;
}