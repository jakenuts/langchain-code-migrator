```python
from langchain.memory import MemoryBuffer
from logger import log_operation

class CustomMemoryBuffer(MemoryBuffer):
    def __init__(self):
        super().__init__()

    @log_operation
    def store(self, key, value):
        super().store(key, value)

    @log_operation
    def retrieve(self, key):
        return super().retrieve(key)

    @log_operation
    def delete(self, key):
        super().delete(key)

    @log_operation
    def clear(self):
        super().clear()
```