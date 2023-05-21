# C programs to simulate UNIX commands like cp, ls, grep

## PROGRAM FOR SIMULATION OF CP UNIX COMMANDS

`$ cc cp.c -o cp`

`$ ./cp ~/acts.txt`

OUTPUT: `No of spaces 2`

## PROGRAM FOR SIMULATION OF LS UNIX COMMANDS

`$ cc ls.c -o ls`

`$ ./ls .`

OUTPUT:

```
The contents of the . are
.
grep.c
grep
..
README.md
cp
cp.c
ls.c
ls

```

## PROGRAM FOR SIMULATION OF GREP UNIX COMMANDS

`$ cc grep.c -o grep`

`$ ./grep ~/ww3 peace`

OUTPUT:

```
/home/djoe/ww3: 13 Fingers on triggers, a fragile peace undone,

/home/djoe/ww3: 33 They stood for peace, for love, for unity,

/home/djoe/ww3: 48 May we strive for peace, in every land and shore,
```
