```python
import functools
from logger import log_operation

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log_operation(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        log_operation(f"Function {func.__name__} completed")
        return result
    return wrapper

def error_handling_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_operation(f"Error occurred in function {func.__name__}: {str(e)}")
            raise e
    return wrapper

def memory_buffer_decorator(memory_buffer):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            memory_buffer.store(result)
            return result
        return wrapper
    return decorator
```