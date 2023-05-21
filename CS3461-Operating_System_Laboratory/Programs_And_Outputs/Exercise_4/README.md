# INTER PROCESS COMMUNICATION

## Message Queue For Writing Process

`$ cc message_queue_writing_process.c -o message_queue_writing_process`

`$ ./message_queue_writing_process`

OUTPUT:

```
Write Data : 3
Data send is : 3
```

## Message Queue For Reader Process

`$ cc message_queue_reader.c -o message_queue_reader`

`$ ./message_queue_reader`

OUTPUT:

```
Data Received is : 3
```
