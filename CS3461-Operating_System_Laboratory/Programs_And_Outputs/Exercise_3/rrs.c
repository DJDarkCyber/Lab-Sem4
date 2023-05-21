#include<stdio.h>
#include<stdlib.h>

struct rr {
    int pno, btime, sbtime, wtime, lst;
};

int main() {
    int pp = -1, ts, flag, count, ptm = 0, i, n, twt = 0, totttime = 0;
    printf("\n Round Robin Scheduling...\n");
    printf("Enter the number of processes: ");
    scanf("%d", &n);
    printf("Enter the time slice: ");
    scanf("%d", &ts);
    printf("Enter the burst time:\n");

    struct rr *p = (struct rr*)malloc(n * sizeof(struct rr)); // Memory allocation

    for (i = 0; i < n; i++) {
        printf("\n Process %d: ", i + 1);
        scanf("%d", &p[i].btime);
        p[i].wtime = p[i].lst = 0;
        p[i].pno = i + 1;
        p[i].sbtime = p[i].btime;
    }

    printf("Scheduling...\n");

    do {
        flag = 0;
        for (i = 0; i < n; i++) {
            count = p[i].btime;
            if (count > 0) {
                flag = -1;
                count = (count >= ts) ? ts : count;
                printf("\n Process %d from %d to %d", p[i].pno, ptm, ptm + count);
                ptm += count;
                p[i].btime -= count;
                if (pp != i) {
                    pp = i;
                    p[i].wtime += ptm - p[i].lst - count;
                    p[i].lst = ptm;
                }
            }
        }
    } while (flag == -1);

    printf("\n\n Process\tWaiting Time\n");
    for (i = 0; i < n; i++) {
        printf(" %d\t\t%d\n", p[i].pno, p[i].wtime);
        twt += p[i].wtime;
        totttime += p[i].sbtime + p[i].wtime;
    }

    printf("\n Total Waiting Time: %d", twt);
    printf("\n Average Waiting Time: %f", (float)twt / n);
    printf("\n Total Turnaround Time: %d", totttime);
    printf("\n Average Turnaround Time: %f", (float)totttime / n);

    free(p); // Memory deallocation

    return 0;
}
