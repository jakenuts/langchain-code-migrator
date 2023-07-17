```python
from functools import wraps
from logger import logger

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.log_operation(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        logger.log_operation(f"Function {func.__name__} completed")
        return result
    return wrapper

def error_handling_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.log_operation(f"Error occurred in function {func.__name__}: {str(e)}")
            raise e
    return wrapper
```