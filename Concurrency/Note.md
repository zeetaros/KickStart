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
