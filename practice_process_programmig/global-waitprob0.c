#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/time.h>
int main() 
{
    if (Fork() == 0) {
        printf("9");
        fflush(stdout);
    }
    else {
        printf("0");
        fflush(stdout);
        waitpid(-1, NULL, 0);
    }
    printf("3");
    fflush(stdout);
    print("6");
    exit(0);
}