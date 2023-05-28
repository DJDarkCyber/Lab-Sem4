# 1. a. Illustrate the following UNIX Commands: create a directory, create a file and view it.
# b. Develop a Shell program to generate Fibonacci Series.
# c. For the following table find the average waiting time and turnaround time using FCFS CPU scheduling:


| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
|  P0     |  1           |  5         |
|  P1     |  1           |  3         |
|  P2     |  2           |  8         |
|  P3     |  3           |  6         |

## a. Illustrate the following UNIX Commands: create a directory, create a file and view it.

**Creating a Directory**

`$ mkdir sample_dir`

**Creating a file**

`$ touch my_file`

**To view Created File,**

`$ ls`

OUTPUT:
```
my_file  sample_dir
```

## Develop a Shell program to generate Fibonacci Series.

`bash fibonacci_series.sh`

OUTPUT:

```
└─$ bash fibonacci_series.sh
Enter the range to be displayed
7
Fibonacci Series
0
1
1
2
3
5

```

## c. For the following table find the average waiting time and turnaround time using FCFS CPU scheduling:

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
|  P0     |  1           |  5         |
|  P1     |  1           |  3         |
|  P2     |  2           |  8         |
|  P3     |  3           |  6         |

`$ cc fcfs.c -o fcfs`

`$ ./fcfs`

OUTPUT:

```

 fcfs scheduling...
enter the no of process > 4

 burst time of the process > 5

 burst time of the process > 3

 burst time of the process > 8

 burst time of the process > 6

 waiting time for process 0
 turn around time for process 0

 waiting time for process 1
 turn around time for process 1

 waiting time for process 2
 turn around time for process 2

 waiting time for process 3
 turn around time for process 3

 total waiting time : 29
 average waiting time : 7.250000
 total turn around time : 51
 average turn around time: 12.750000                                                                                                                                                                 
```
In FCFS scheduling, the arrival time is not considered for determining the execution order of processes.
