# 11. a. Develop a Shell program to generate Fibonacci Series.
# b. For the following table find the average waiting time and turnaround time using SJF CPU scheduling:

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
|  P0     |  0           |  8         |
|  P1     |  1           |  2         |
|  P2     |  2           |  3         |
|  P3     |  3           |  4         |

## a. Develop a Shell program to generate Fibonacci Series.

`$ bash fibo_series.sh`

OUTPUT:

```
Enter the range to be displayed
5
Fibonacci Series
0
1
1
2
3
5
```

## b. For the following table find the average waiting time and turnaround time using SJF CPU scheduling:

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
|  P0     |  0           |  8         |
|  P1     |  1           |  2         |
|  P2     |  2           |  3         |
|  P3     |  3           |  4         |


`$ cc sjf.c -o sjf`

`$ ./sjf`

OUTPUT:

```
SJF Scheduling..
Enter the number of processes: 4

Process 1: 8

Process 2: 2

Process 3: 3

Process 4: 4

Process Scheduling

Process Burst Time      Wait Time
2               2               0               2
3               3               2               3
4               4               5               4
1               8               9               8
total waiting time :16
average waiting time :4.000000
total turn around time :33
average turn around time: :8.250000 
```
