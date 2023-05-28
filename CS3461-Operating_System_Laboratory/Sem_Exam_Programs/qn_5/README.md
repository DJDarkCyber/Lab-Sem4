# 5. a. Illustrate the following UNIX Commands: list the files and directories
# b. Develop a Shell program to find area and circumference of a circle.
# c. Write a C Program to implement First Fit Allocation Method for the following:

| Process | Size | Block | Size |
|---------|------|-------|------|
|  P0     |  90  |  B1   | 20   |
|  P1     |  52  |  B2   | 100  |
|  P2     |  30  |  B3   | 40   |
|  P3     |  40  |  B4   | 200  |
|         |      |  B5   | 10   |

## a. Illustrate the following UNIX Commands: list the files and directories

**To List Files and directories**

`$ ls -al`

OUTPUT:


```
drwxr-xr-x  2 unknown unknown  4096 May 20 15:28 Nothing
drwxr-xr-x  3 unknown unknown  4096 Apr  5 20:22 Something
drwxr-xr-x  2 unknown unknown  4096 Apr 27 17:41 Anything
-rw-------  1 unknown unknown 69884 Apr 16 07:14 idk.txt
```

## b. Develop a Shell program to find area and circumference of a circle.

`$ bash area_circ.sh`

OUTPUT:

```
Enter the radius of the cicle > 4
Area : 50.24
Circumference : 25.12
```

## c. Write a C Program to implement First Fit Allocation Method for the following:

| Process | Size | Block | Size |
|---------|------|-------|------|
|  P0     |  90  |  B1   | 20   |
|  P1     |  52  |  B2   | 100  |
|  P2     |  30  |  B3   | 40   |
|  P3     |  40  |  B4   | 200  |
|         |      |  B5   | 10   |


`$ cc first_fit.c -o first_fit`

`$ ./first_fit`

OUTPUT:

```
Memory Management Scheme - First Fit
Enter the number of blocks: 5
Enter the number of files: 4

Enter the size of the blocks:
Block 1: 20
Block 2: 100
Block 3: 40
Block 4: 200
Block 5: 10
Enter the size of the files:
File 1: 90
File 2: 52
File 3: 30
File 4: 40

File_no         File_size       Block_no        Block_size      Fragmentation
1               90              2               100             10
2               52              4               200             148
3               30              3               40              10
4               40              0               0               -30                                                                                                                                                                 

```
