# Bankers Algorithm for Deadlock Prevention


`$ cc bankers_algo.c -o bankers_algo`

`$ ./bankers_algo`

OUTPUT:

```
Enter the no of Processes : 2


Enter the no of Resources : 1


Enter the Max Matrix for each Process :
For Process 1 : 2

For Process 2 : 1


Enter the allocation for each Process :
For Process 1 : 2

For Process 2 : 1


Enter the Available Resources : 2

 Max Matrix:    Allocation Matrix:
2               2
1               1

Process 1 runs to Completion!
 Max Matrix:    Allocation Matrix:
0               0
1               1

Process 2 runs to Completion!
The system is in a Safe State!!
Safe Sequence : < 1 2 >

```
