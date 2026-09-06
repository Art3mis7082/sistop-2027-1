package main

import (
    "fmt"
    "os"
)

func main() {
    // Si hay más de un argumento, el índice 1 es el nombre que pasó el usuario
    if len(os.Args) > 1 {
        fmt.Printf("¡Hola, %s!\n", os.Args[1])
    } else {
        fmt.Println("¡Hola mundo!")
    }
}
