# Basic Unix Commands

## Basic Commands

### a) Display Commands :

1) Date

`$ date`

OUTPUT: `Fri May 19 01:08:26 PM IST 2023`

2) Month

`$ date +%m`

OUTPUT: `05`

3) Month Name

`$ date +%h`

OUTPUT: `May`

4) Month Day

`$ date +%d`

OUTPUT: `19`

5) Year

`$ date +%y`

OUTPUT: `23`

6) Hour

`$ date +%H`

OUTPUT: `13`

7) Minutes

`$ date +%M`

OUTPUT: `44`

8) Seconds

`$ date +%S`

OUTPUT: `12`

### b) Command: cal

`$ cal`

OUTPUT:
```
May 2023        
Su Mo Tu We Th Fr Sa  
1  2  3  4  5  6  
7  8  9 10 11 12 13  
14 15 16 17 18 19 20  
21 22 23 24 25 26 27  
28 29 30 31           

```

### c) echo

`$ echo HELLO`

OUTPUT: `HELLO`

### d) ls

`$ ls`

OUTPUT: `Documents/ Desktop/ Downloads/`

### e) man

`$ man ls`

### f) who

`$ who`

OUTPUT:
```
unknown     tty7         2023-05-19 09:37 (:0)
unknown     pts/0        2023-05-19 09:37 (:0)
unknown     pts/1        2023-05-19 09:37 (:0)
unknown     pts/3        2023-05-19 12:34 (:0)
unknown     pts/6        2023-05-19 12:37 (:0)
```

### g) whoami

`$ whoami`

OUTPUT: `root`

### h) uptime

`$ uptime`

OUTPUT: ` 13:20:42 up  3:42,  5 users,  load average: 0.93, 1.13, 1.06`

### i) uname

`$ uname -a`

OUTPUT: `Linux unknown 5.18.0-kali5-amd64 #1 SMP PREEMPT_DYNAMIC Debian 5.18.5-1kali6 (2022-07-07) x86_64 GNU/Linux`

### j) hostname

`$ hostname`

OUTPUT: `unknown`

### k) bc

`$ bc`

OUTPUT:
```
bc 1.07.1
Copyright 1991-1994, 1997, 1998, 2000, 2004, 2006, 2008, 2012-2017 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'.
4+1
5

```

### l) id

`$ id`

OUTPUT:
```
groups=1000(unknown),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),109(netdev),120(wireshark),121(bluetooth),126(lpadmin),139(scanner),143(kaboxer)
```
### m) clear

`$ clear`

OUTPUT: ` `

### n) finger

`$ finger`

OUTPUT:
```
Login     Name       Tty      Idle  Login Time   Office     Office Phone
unkown      unkown       tty7       12  May 19 16:40 (:0)
unkown      unkown       pts/0      12  May 19 16:40 (:0)
unkown      unkown      *pts/1          May 19 16:40 (:0)
unkown      unkown      *pts/2       1  May 19 16:51 (:0)

```

## FILE MANIPULATION COMMANDS

### a) cat

`$ cat file_name`

OUTPUT: `Hello`

### b) concatenate

`$ cat file1 file2 > file3`

OUTPUT: ` `

### c) grep

`$ grep anu student`

OUTPUT: ` `

### d) rm

`$ rm file_name`

OUTPUT: ` `

### e) touch

`$ touch file_name`

OUTPUT: ` `

### f) cp

`$ cp file copied_file`

OUTPUT: ` `

### g) mv

`$ mv file1 new_file_name`

OUTPUT: ` `

### h) cut

`$ cut -c 1 file1`

OUTPUT: `H`

### i) wc

`$ wc file1 -c`

OUTPUT: `6`

## DIRECTORY COMMANDS

### a) mkdir

`$ mkdir folder_name`

OUTPUT: ` `

### b) rmdir

`$ rmdir folder_name`

OUTPUT: ` `

### c) cd

`$ cd folder_name`

OUTPUT: ` `

### d) pwd

`$ pwd`

OUTPUT: `/home/unknown/`

## PROCESS COMMANDS

### a) exit

`$ exit`

OUTPUT: ` `

### b) kill

`$ kill %1`

OUTPUT: `[1]  + terminated  sleep 10`

### c) passwd

`$ passwd`

OUTPUT: ` `

### d) semicolon (;)

`$ who;date`

OUTPUT:
```
djoe     tty7         2023-05-19 16:40 (:0)
djoe     pts/0        2023-05-19 16:40 (:0)
djoe     pts/1        2023-05-19 16:40 (:0)
djoe     pts/2        2023-05-19 16:51 (:0)
Fri May 19 05:10:06 PM IST 2023

```

## FILTER COMMANDS

### a) head

`$ head file1`

OUTPUT:
```
In the realm of code, where laughter unfurls,
A whimsical program for boys and girls.
It starts with a greeting, a cheerful remark,
A "Hello World!" to light up the dark.

In lines of text, where humor takes hold,
Let's craft a poem, witty and bold.
With code as our paintbrush, we'll weave a tale,
Of bits and bytes, where jesters prevail.
```

### b) tail

`$ tail file1`

OUTPUT:
```
The code may be serious, complex, and grand,
But "Hello World!" brings humor to the land.
So let's celebrate this simple little phrase,
With giggles and chuckles that never cease.

For in the realm of code, where laughter unfurls,
A "Hello World!" poem can brighten the world.
So next time you program, don't forget the jest,
And greet the universe with a smile, at best!
```
### c) chmod

`$ chmod +x script`

OUTPUT: ` `
