<h2>Concurrency vs. Parallelism</h2>

**Concurrency:** Handling multiple tasks at the same time, but not necessarily running them simultaneously. The system quickly switches between tasks — this can happen even on a single CPU core.

    Analogy: A barista is handling multiple coffee orders. They start making one coffee, then pause it to start another, and keep switching — they’re juggling tasks, but doing one thing at a time.

**Parallelism:** Actually running multiple tasks at the same exact time. This requires multiple CPU cores or processors.

    Analogy: Two baristas, each with their own coffee machine, both making coffee at the same time. Tasks are truly simultaneous.


**Why does it matter?**
- in asynchronous programming (async/await in JavaScript, asyncio in Python)
- in multi-threaded or multi-process systems
- in performance tuning:
    - Use concurrency for I/O-bound tasks (e.g. web scraping, database queries)
    - Use parallelism for CPU-bound tasks (e.g. number crunching, image processing)


<h3>Examples:</h3>

Concurrency with asyncio (Single-threaded, I/O-bound tasks)
```python
import asyncio
import time

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay} sec")

async def main():
    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 3),
        task("Task 3", 1)
    )

start = time.time()
asyncio.run(main())
print(f"Total time: {time.time() - start:.2f} sec")

```
The above script has several tasks that run concurrently, but not at the same instant. Total time is close to the longest task (3s), not their sum (6s).

Parallelism with multiprocessing (CPU-bound tasks)
```python
from multiprocessing import Process
import time

def cpu_task(name):
    print(f"{name} started")
    count = 0
    for _ in range(10**7):
        count += 1
    print(f"{name} finished")

if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=cpu_task, args=("Process 1",))
    p2 = Process(target=cpu_task, args=("Process 2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(f"Total time: {time.time() - start:.2f} sec")
```
The above one has two tasks that run parallel, using separate CPU cores. Total time is much shorter than running them one ofter the other.