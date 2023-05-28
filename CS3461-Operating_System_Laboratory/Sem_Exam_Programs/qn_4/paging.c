#include<stdio.h>

void main() {
  int memsize=15;
  int pagesize,nofpage;
  int p[100];
  int frameno,offset;
  int logadd,phyadd;
  int i;
  int choice=0;
  printf("\nYour Memory Size is %d ",memsize);
  printf("\nEnter Page Size:");
  scanf("%d",&pagesize);
  nofpage=memsize/pagesize;
  for(i=0;i<nofpage;i++) {
    printf("\nEnter the Frame of Page%d:",i+1);
    scanf("%d",&p[i]);
  }
  do {
    printf("\nEnter a logical address:");
    scanf("%d",&logadd);
    frameno=logadd/pagesize;
    offset=logadd%pagesize;
    phyadd=(p[frameno]*pagesize)+offset;
    printf("\nPhysical address is:%d",phyadd);
    printf("\nDo you want to continue(1/0)?:");
    scanf("%d",&choice);
  } while(choice==1);
}
