```python
import logging

class Logger:
    def __init__(self, filename="app.log"):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_operation(self, message, level=logging.INFO):
        if level == logging.CRITICAL:
            self.logger.critical(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.INFO:
            self.logger.info(message)
        else:
            self.logger.debug(message)
```