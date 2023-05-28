#include <stdio.h>
#include <pthread.h>

typedef struct {
    int count;
    pthread_mutex_t mutex;
    pthread_cond_t condition;
} Semaphore;

void semaphore_init(Semaphore* semaphore, int initial_count) {
    semaphore->count = initial_count;
    pthread_mutex_init(&semaphore->mutex, NULL);
    pthread_cond_init(&semaphore->condition, NULL);
}

void semaphore_wait(Semaphore* semaphore) {
    pthread_mutex_lock(&semaphore->mutex);
    while (semaphore->count <= 0) {
        pthread_cond_wait(&semaphore->condition, &semaphore->mutex);
    }
    semaphore->count--;
    pthread_mutex_unlock(&semaphore->mutex);
}

void semaphore_signal(Semaphore* semaphore) {
    pthread_mutex_lock(&semaphore->mutex);
    semaphore->count++;
    pthread_cond_signal(&semaphore->condition);
    pthread_mutex_unlock(&semaphore->mutex);
}

void* thread_function(void* arg) {
    Semaphore* semaphore = (Semaphore*)arg;

    printf("Thread started\n");
    semaphore_wait(semaphore);
    printf("Thread inside critical section\n");
    // Perform operations inside the critical section
    printf("Thread exiting critical section\n");
    semaphore_signal(semaphore);

    return NULL;
}

int main() {
    Semaphore semaphore;
    semaphore_init(&semaphore, 1);

    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, thread_function, &semaphore);
    pthread_create(&thread2, NULL, thread_function, &semaphore);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    return 0;
}
