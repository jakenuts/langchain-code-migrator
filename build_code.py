```python
import subprocess
from logger import log_operation

class BuildCode:
    def __init__(self, build_command):
        self.build_command = build_command

    @log_operation
    def run_build(self):
        try:
            build_process = subprocess.run(self.build_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return build_process.stdout.decode(), build_process.stderr.decode()
        except subprocess.CalledProcessError as e:
            return "", e.output.decode()
```