#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define max 1024

void usage() {
  printf("./grep filename search_String");
}

int main(int argc, char *argv[]) {
  FILE *fp;
  char fline[max];
  int count;
  if (argc != 3) {
    usage();
    exit(1);
  }

  if (!(fp = fopen(argv[1], "r"))) {
    printf("Unable to open file: %s", argv[1]);
    exit(1);
  }

  while(fgets(fline, max, fp) != NULL) {
    count++;
    if (strstr(fline, argv[2]) != NULL) {
      printf("%s: %d %s\n", argv[1], count, fline);
    }
  }
  return 0;
}
