#include <stdio.h>
#include <unistd.h>

int main(void)
{
    printf("PID del proceso actual: %d\n", getpid());
    return 0;
}
