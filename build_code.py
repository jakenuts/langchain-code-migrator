```python
import subprocess
from logger import Logger

class BuildCode:
    def __init__(self):
        self.logger = Logger(__name__)

    def build_project(self, build_command):
        try:
            self.logger.log_operation(f"Running build command: {build_command}")
            process = subprocess.Popen(build_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()

            if process.returncode != 0:
                self.logger.log_operation(f"Build failed with error: {error.decode('utf-8')}")
                return False, error.decode('utf-8')
            else:
                self.logger.log_operation("Build succeeded")
                return True, output.decode('utf-8')

        except Exception as e:
            self.logger.log_operation(f"Exception occurred during build: {str(e)}")
            return False, str(e)
```