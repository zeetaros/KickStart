# How To Speech Up

## Aspects to consider
1. communication
2. load balance
3. overhead

### Communication
The cost of communication is high. Reduce the number of times that data needs to be transferred.

Having said that, communication can happen when waiting for independent large task to finish. For example, `Process 4` is assigned tasks [a, b, c, d, e, f] with increasing complexity. When it got the output of a, b, c, d and waiting for e, but e is going to take long to finish, then we can consider communicate the result of a, b, c, d back to the main process first while waiting for e to finish.

### Load Balance
Make sure the workloads are split as evenly as possible across all processes.

Batch processing can be leverage to find the right balance between 
- the amount of data being transferred each time
- number of transfers/comms happening

### Overhead
This is the cost of the cold start which has complexity $O(1)$. Multiprocessing is most effective if there is sufficiently large number of tasks.

## Benchmarking

### Speedup ratio
- How many times quicker the code is in parallel relative to the serial code (i.e. run on a single core)
- Increase linearly at the start.

$$ \mathbf{S} = \frac{T_1}{T_N} $$ 
*where $N$ is the number of cores.*

### Parallel Efficiency
- How fast is the code relative to an ideal speedup.
- Sometimes when go from 1 core to 2 cores, the efficiency becomes lower due to the overhead of parallelisation, but it should gradually climb up as cores increases.
- The parallel efficiency will start to drop off if you keep increasing the number of cores. 

$$ \mathbf{E} = \frac{T_1}{N T_N} = \frac{\mathbf{S}}{N}$$

