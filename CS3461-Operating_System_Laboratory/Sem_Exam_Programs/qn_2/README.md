# 2. a. Illustrate the following UNIX Commands: Word Count in a File, List the Directory
# b. Develop a Shell program to find whether given number is even or odd.
# c. Implement IPC strategy using C.

## a. Illustrate the following UNIX Commands: Word Count in a File, List the Directory

**To Count words in a file**

`$ echo 'written something here' > my_file`

`$ wc my_file`

OUTPUT:

```
 1  3 23 my_file
```

**To list Directory**

`$ ls -l ~/Documents`

OUTPUT:

```
drwxr-xr-x  2 unknown unknown  4096 May 20 15:28 Nothing
drwxr-xr-x  3 unknown unknown  4096 Apr  5 20:22 Something
drwxr-xr-x  2 unknown unknown  4096 Apr 27 17:41 Anything
-rw-------  1 unknown unknown 69884 Apr 16 07:14 idk.txt
```

## b. Develop a Shell program to find whether given number is even or odd.

`$ bash even_or_odd.sh`

OUTPUT:
```
Enter a number
4
Even

Enter a number
3
Odd
```

## c. Implement IPC strategy using C.

`$ cc message_queue_writer.c -o message_queue_writer`

`$ cc message_queue_reader.c -o message_queue_reader`



OUTPUT:

`$ ./message_queue_writer`

```
Write Data : Test001
Data send is : Test001
```

`$ ./message_queue_reader`


```
Data Received is : Test001
```
