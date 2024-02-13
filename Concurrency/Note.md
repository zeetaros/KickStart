## Multi-threading

### Daemon thread
A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. 

When the main thread finishes, the programme exit whether or not there are on-going daemon threads.

```py
t = threading.Thread(target=time.sleep, args=(seconds,), daemon=True)
```

__Usage__  
Some threads do background tasks, like sending keepalive packets, or performing periodic garbage collection, or whatever. These are only useful when the main program is running, and it's okay to kill them off once the other, non-daemon, threads have exited.

Without daemon threads, you'd have to keep track of them, and tell them to exit, before your program can completely quit. By setting them as daemon threads, you can let them run and forget about them, and when your program quits, any daemon threads are killed automatically.

(*ref: https://stackoverflow.com/questions/190010/daemon-threads-explanation*)

### What is the benefit of multi-threading in Python if GIL exists?

**Global Interpreter Lock (GIL)** allows only one thread to hold the control of the Python interpreter. This means that only one thread can be in a state of execution at any point in time. 

In short, for CPU intensive tasks, implementing multi-threading in Python has minimal gains because of GIL. However, there are still still performance improvements in some other cases; and in these scenarios, the GIL will be released allowing other threads in the multi-threading implementation to utilise the CPU resource. The GIL does not prevent these operations from running in parallel:

- I/O operations, such as sending & receiving network data or reading/writing to a file.
- Heavy built-in CPU bound operations, such as hashing or compressing.
- Some C extension operations, such as numpy calculations.

In fact, in a lot of programmes the majority of runtime is taken up by the network/communications. While waiting for send & receive, the other threads can start working.  
  
Moreover, at least for networking, other methodologies are more prevalent these days such as `asyncio` which offers cooperative multi-tasking on the same thread.

(*ref: https://stackoverflow.com/questions/52507601/whats-the-point-of-multithreading-in-python-if-the-gil-exists*)

<br>

## Asynchronisation
Async is running on 1 thread on 1 core. Different from multi-threading and multi-processing, it achieves higher performance via more efficient scheduling and management of resources.

Async has **less overhead** than multi-threading beacause it doesn't need to create and manage threads. 
Web applications use a lot of async pattern to avoid blocking communications.  