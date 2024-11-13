# import asyncio
# import threading

# async def async_task():
#     for i in range(3):
#         print(f"Async task iteration {i} in thread {threading.current_thread().name}")
#         await asyncio.sleep(1)  # Non-blocking wait

# async def main():
#     await async_task()

# asyncio.run(main())


import asyncio
import random
import time

def blocking_io():
    print("Start blocking IO operation")
    time.sleep(2)  # Simulate blocking I/O
    print("End blocking IO operation")

# async def main_before():
#     loop = asyncio.get_running_loop()
#     with ThreadPoolExecutor() as pool:
#         await loop.run_in_executor(pool, blocking_io)

async def task(name, duration):
    print(f"Task {name} started, will take {duration} seconds.")
    await asyncio.sleep(duration)  # Simulates an asynchronous operation (e.g., I/O)
    print(f"Task {name} completed.")

async def main():
    # Define multiple tasks with different durations
    tasks = [
        task("A", random.uniform(1, 3)),  # Random duration between 1 and 3 seconds
        task("B", random.uniform(1, 3)),
        task("C", random.uniform(1, 3)),
        asyncio.to_thread(blocking_io)
    ]
    
    # Run all tasks concurrently
    await asyncio.gather(*tasks)

# Run the event loop
asyncio.run(main())