# 14. a. Develop a Shell program to find area and circumference of a circle.
# b. Write a C Program to implement Best Fit Allocation Method for the following:

| Process | Size | Block | Size |
|---------|------|-------|------|
|  P0     |  40  |  B1   |  100 |
|  P1     |  10  |  B2   |  50  |
|  P2     |  30  |  B3   |  20  |
|  P3     |  60  |  B4   |  120 |
|         |      |  B5   |  35  |


## a. Develop a Shell program to find area and circumference of a circle.

`$ bash area_circ.sh`

OUTPUT:

```
Enter the radius of the cicle > 4
Area : 50.24
Circumference : 25.12
```

## b. Write a C Program to implement Best Fit Allocation Method for the following:

| Process | Size | Block | Size |
|---------|------|-------|------|
|  P0     |  40  |  B1   |  100 |
|  P1     |  10  |  B2   |  50  |
|  P2     |  30  |  B3   |  20  |
|  P3     |  60  |  B4   |  120 |
|         |      |  B5   |  35  |

`$ cc best_fit.c -o best_fit`

`$ ./best_fit`

OUTPUT:

```
Memory Management Scheme - Best Fit
Enter the number of blocks: 5
Enter the number of files: 4

Enter the size of the blocks:
Block 1: 100
Block 2: 50
Block 3: 20
Block 4: 120
Block 5: 35
Enter the size of the files:
File 1: 40
File 2: 10
File 3: 30
File 4: 60

File No File Size       Block No        Block Size      Fragment
1               40              2               50              10
2               10              3               20              10
3               30              5               35              5
4               60              1               100             40  
```
