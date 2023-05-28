#include<stdio.h>
#include<stdlib.h>

typedef struct {
  int pid;
  int btime;
  int wtime;
} sp;

int main() {
  int i, j, n, tbm = 0, towtwtime = 0, totttime;
  sp* p, t;
  printf("\n SJF Scheduling..\n");
  printf("Enter the number of processes: ");
  scanf("%d", &n);

  p = (sp*)malloc(n * sizeof(sp));

  for(i=0; i<n; i++) {
    printf("\n Process %d: ", i+1);
    scanf("%d", &p[i].btime);
    p[i].pid = i + 1;
    p[i].wtime = 0;
  }

  for(i=0; i<n; i++)
    for(j=i+1; j<n; j++) {
      if(p[i].btime > p[j].btime) {
        t = p[i];
        p[i] = p[j];
        p[j] = t;
      }
    }
    printf("\n Process Scheduling\n");
    printf("\nProcess\tBurst Time\tWait Time");
    for(i=0; i<n; i++) {
      towtwtime += p[i].wtime = tbm;
      tbm += p[i].btime;
      printf("\n%d\t\t%d", p[i].pid, p[i].btime);
      printf("\t\t%d\t\t%d", p[i].wtime, p[i].btime);
    }
    totttime = tbm + towtwtime;
    printf("\n total waiting time :%d", towtwtime );
    printf("\n average waiting time :%f",(float)towtwtime/n);
    printf("\n total turn around time :%d",totttime);
    printf("\n average turn around time: :%f",(float)totttime/n);

    free(p);

    return 0;
}
