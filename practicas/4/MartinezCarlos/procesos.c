#include <stdio.h>
#include <unistd.h>

int main(void) {
    printf("PID actual: %d, PPID: %d\n", getpid(), getppid());
    return 0;
}
