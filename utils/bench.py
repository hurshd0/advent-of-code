import time
import psutil
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        process = psutil.Process()
        start_memory = process.memory_info().rss / 1024 / 1024  # Memory usage in MB
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        end_memory = process.memory_info().rss / 1024 / 1024  # Memory usage in MB
        cpu_time = process.cpu_times().user + process.cpu_times().system
        print(f"Execution time for '{func.__name__}': {execution_time:.6f} seconds")
        print(f"CPU execution time for '{func.__name__}': {cpu_time:.6f} seconds")
        print(f"Memory usage for '{func.__name__}': {end_memory - start_memory:.6f} MB")
        return result
    return wrapper