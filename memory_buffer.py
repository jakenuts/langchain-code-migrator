```python
import threading
from collections import deque
from logger import Logger

class MemoryBuffer:
    def __init__(self, max_size=100):
        self.buffer = deque(maxlen=max_size)
        self.lock = threading.Lock()
        self.logger = Logger(__name__)

    def add(self, item):
        with self.lock:
            self.buffer.append(item)
            self.logger.log_operation(f"Added item to memory buffer: {item}")

    def get(self):
        with self.lock:
            if len(self.buffer) == 0:
                return None
            item = self.buffer.popleft()
            self.logger.log_operation(f"Retrieved item from memory buffer: {item}")
            return item

    def size(self):
        with self.lock:
            return len(self.buffer)

    def is_empty(self):
        with self.lock:
            return len(self.buffer) == 0
```