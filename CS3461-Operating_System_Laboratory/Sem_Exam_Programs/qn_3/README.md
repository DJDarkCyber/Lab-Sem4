# 3. a. Illustrate the following System Calls: Fork()
# b. Develop a Shell program to find whether given number is Armstrong.
# c. Implement Banker’s Algorithm using C.

## a. Illustrate the following System Calls: Fork()

`$ cc fork.c -o fork`

`$ ./fork`

OUTPUT:

```
the parent process ID is 23652

the child process ID is 23653
```

## b. Develop a Shell program to find whether given number is Armstrong.

`$ bash armstrong_num.sh`

OUTPUT:

```
Enter a Number
01234
01234 is not an armstrong number
```

## c. Implement Banker’s Algorithm using C.

`$ cc bankers_algo.c -o bankers_algo`

`$ ./bankers_algo`

OUTPUT:

```
Enter the no of Processes : 3


Enter the no of Resources : 2


Enter the Max Matrix for each Process :
For Process 1 : 1
4

For Process 2 : 2
3

For Process 3 : 3
2


Enter the allocation for each Process :
For Process 1 : 3
2

For Process 2 : 1
3

For Process 3 : 2
3


Enter the Available Resources : 3
2

 Max Matrix:    Allocation Matrix:
1 4             3 2
2 3             1 3
3 2             2 3

Process 1 runs to Completion!
 Max Matrix:    Allocation Matrix:
0 0             0 0
2 3             1 3
3 2             2 3

Process 2 runs to Completion!
 Max Matrix:    Allocation Matrix:
0 0             0 0
0 0             0 0
3 2             2 3

Process 3 runs to Completion!
The system is in a Safe State!!
Safe Sequence : < 1 2 3 >

```
