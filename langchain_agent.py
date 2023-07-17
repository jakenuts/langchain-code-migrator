```python
import glob
from langchain import LangchainAgent, LangchainMemoryBuffer
from langchain_decorators import log_operation
from openai_interface import OpenAIInterface
from tools import refactor_code
from build_code import build_code
from logger import Logger

class CodeRefactorAgent(LangchainAgent):
    def __init__(self, languages, glob_pattern, build_tool):
        super().__init__()
        self.languages = languages
        self.glob_pattern = glob_pattern
        self.build_tool = build_tool
        self.memory_buffer = LangchainMemoryBuffer()
        self.openai_interface = OpenAIInterface()
        self.logger = Logger()

    @log_operation
    def review_source_code(self):
        for language in self.languages:
            files = glob.glob(f'**/*.{language}', recursive=True)
            for file in files:
                with open(file, 'r') as f:
                    code = f.read()
                    self.memory_buffer.store(code)

    @log_operation
    def refactor_source_code(self, user_request):
        for language in self.languages:
            files = glob.glob(f'**/*.{language}', recursive=True)
            for file in files:
                with open(file, 'r+') as f:
                    code = f.read()
                    refactored_code = refactor_code(code, user_request)
                    f.seek(0)
                    f.write(refactored_code)
                    f.truncate()

    @log_operation
    def build_project(self):
        build_result = build_code(self.build_tool)
        if build_result['status'] == 'error':
            self.logger.log(build_result['message'])
            return False
        return True

    @log_operation
    def run(self, user_request):
        self.review_source_code()
        self.refactor_source_code(user_request)
        build_success = self.build_project()
        if not build_success:
            self.run(user_request)
        else:
            self.logger.log('Refactoring and build successful.')
```