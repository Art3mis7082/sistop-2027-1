#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{

pid_t pid = fork();

if (pid == 0) 
{
	printf("Soy el hijo: PID %d, mi padre es %d\n", getpid(), getppid());
}
else
{
	wait(NULL);
	printf("Soy el padre: PID %d, mi hijo fue %d\n", getpid(), pid);
}
return 0;

}
