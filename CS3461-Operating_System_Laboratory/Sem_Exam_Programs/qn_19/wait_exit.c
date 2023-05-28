#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
    pid_t child_pid;
    int status;

    // Create a child process
    child_pid = fork();

    if (child_pid < 0) {
        // Fork failed
        fprintf(stderr, "Failed to create child process\n");
        exit(1);
    } else if (child_pid == 0) {
        // Child process

        printf("Child process running...\n");
        sleep(2); // Simulating some work

        printf("Child process exiting\n");
        exit(0);
    } else {
        // Parent process

        printf("Parent process waiting for child...\n");

        // Wait for the child process to exit
        wait(&status);

        if (WIFEXITED(status)) {
            int exit_status = WEXITSTATUS(status);
            printf("Child process exited with status: %d\n", exit_status);
        } else {
            printf("Child process terminated abnormally\n");
        }
    }

    return 0;
}
