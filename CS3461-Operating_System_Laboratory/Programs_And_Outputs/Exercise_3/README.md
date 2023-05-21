# CPU SCHEDULING ALGORITHMS

## 1. FIRST COME FIRST SERVED (FCFS) SCHEDULING

`$ cc fcfs.c -o fcfs`

`$ ./fcfs`

OUTPUT:
```
fcfs scheduling...
enter the no of process3

burst time of the process2

burst time of the process3

burst time of the process1

waiting time for process
turn around time for process

waiting time for process
turn around time for process

waiting time for process
turn around time for process

total waiting time :7
average waiting time :2.333333
total turn around time :13
average turn around time: :4.333333                                                                                                                                                                                                                                           
```

## 2. SHORTEST JOB FIRST (SJF) SCHEDULING

`$ cc sjf.c -o sjf.c`

`$ ./sjf`

OUTPUT:


```

 SJF Scheduling..
Enter the number of processes: 3

 Process 1: 2

 Process 2: 1

 Process 3: 2

 Process Scheduling

Process Burst Time      Wait Time
2               1               0               1
1               2               1               2
3               2               3               2
 total waiting time :4
 average waiting time :1.333333
 total turn around time :9
 average turn around time: :3.000000                                                                                                                                                                                                                                           
```

## 3. PRIORITY SCHEDULING

`$ cc ps.c -o ps`

`$ ./ps`

OUTPUT:

```

 PRIORITY SCHEDULING.

 enter the no of process....
3
enter the burst time and priority:
process1: 1
3
process2: 2
3
process3: 2
1

 process        bursttime       waiting time    turnaround time

3               2               0               2
2               2               2               4
1               1               4               5
 total waiting time: 6
 average waiting time: 2.000000
 total turnaround time: 11
 avg turnaround time: 3.666667                                                                                                                                                                                                                                            

```

## 4. ROUND ROBIN SCHEDULING

`$ cc rrs.c -o rrs`

`$ ./rrs`

OUTPUT:

```

 Round Robin Scheduling...
Enter the number of processes: 3
Enter the time slice: 4
Enter the burst time:

 Process 1: 2

 Process 2: 1

 Process 3: 32
Scheduling...

 Process 1 from 0 to 2
 Process 2 from 2 to 3
 Process 3 from 3 to 7
 Process 3 from 7 to 11
 Process 3 from 11 to 15
 Process 3 from 15 to 19
 Process 3 from 19 to 23
 Process 3 from 23 to 27
 Process 3 from 27 to 31
 Process 3 from 31 to 35

 Process        Waiting Time
 1              0
 2              2
 3              3

 Total Waiting Time: 5
 Average Waiting Time: 1.666667
 Total Turnaround Time: 40
 Average Turnaround Time: 13.333333                                                                                                                                                                                                                                            

```
