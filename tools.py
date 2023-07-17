```python
import glob
import os
from logger import Logger

logger = Logger(__name__)

def match_glob_pattern(pattern, path):
    """
    This function matches a given glob pattern in a given path.
    """
    logger.log_operation(f"Matching glob pattern: {pattern} in path: {path}")
    return glob.glob(os.path.join(path, pattern))

def read_file(file_path):
    """
    This function reads a file and returns its content.
    """
    logger.log_operation(f"Reading file: {file_path}")
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """
    This function writes content to a file.
    """
    logger.log_operation(f"Writing to file: {file_path}")
    with open(file_path, 'w') as file:
        file.write(content)

def run_command(command):
    """
    This function runs a shell command and returns its output.
    """
    logger.log_operation(f"Running command: {command}")
    stream = os.popen(command)
    output = stream.read()
    return output
```