import numpy as np
import time

LOG = False

# method 1
def function(cost: list[int]) -> int:
    cost_len = len(cost)
    cost_sum = 0
    i = 0
    while i < cost_len-3:
        candidates = [(cost[i],cost[i+1]), (cost[i],cost[i+2]), (cost[i+1],cost[i+2])]
        min_index = np.argmin([sum(c) for c in candidates])
        chosen = candidates[min_index][0]
        cost_sum += chosen
        i += min_index // 2 + 1

    cost_sum += min([cost[-2],cost[-1]])
    return cost_sum


# method 2 - array
def function_2(cost: list[int]) -> int:
    n = len(cost)
    result = [0 for _ in range(n+1)]
    result[0:2] = cost[0:2]
    
    for i in range(2, n+1):
        step_cost = 0 if i == n else cost[i]
        result[i] = min([val + step_cost for val in result[i-2:i]])

    return result[-1]

# method 3 - recursive
def recurse(step: int, cost: list[int], n: int, cache: dict) -> int:
    if step in cache:
        return cache[step]
    
    if step >= n:
        return 0
    
    result = min(cost[step] + recurse(step+1, cost, n, cache), cost[step] + recurse(step+2, cost, n, cache))
    cache[step] = result

    return result


def function_3(cost: list[int]) -> int:
    n = len(cost)
    cache = {}

    return min(recurse(0, cost, n, cache), recurse(1, cost, n, cache))




if __name__ == "__main__":
    # Ignore below code.
    timer = []
    for loop in range(500):

        start = time.time()
        with open("climb_stairs_example.txt") as file:

            line_counter = 0
            correct_counter = 0

            for line in file:

                line_counter += 1
                raw_input, raw_answer = line.replace('\n', '').split(', ')

                input = [int(val) for val in raw_input[1:-1].split(',')]
                answer = int(raw_answer)

                output = function(input)
                if LOG:
                    print(f"\nThe input was: {input}\nThe output was: {output}\nThe answer was: {answer}\n")

                if answer == output:
                    correct_counter += 1
                
            percentage_correct = (correct_counter / line_counter) * 100
            if LOG:
                print(f"{percentage_correct}% of answers were correct.\n")
        elapse = time.time() - start
        timer.append(elapse)
    
    print(f"Avg time elapsed: {sum(timer)/len(timer)}")
