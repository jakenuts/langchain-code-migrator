```python
import sys
from langchain import Langchain
from langchain_decorators import langchain_decorator
from openai_interface import OpenAIInterface
from memory_buffer import MemoryBuffer
from tools import glob_match, refactor_request
from langchain_agent import LangchainAgent
from build_code import BuildCode
from logger import Logger

def main():
    logger = Logger()
    memory_buffer = MemoryBuffer()
    langchain = Langchain()
    openai_interface = OpenAIInterface()
    build_code = BuildCode()
    langchain_agent = LangchainAgent(langchain, openai_interface, memory_buffer, logger)

    while True:
        logger.log_operation("Requesting refactoring task")
        task = refactor_request()
        if not task:
            logger.log_operation("No refactoring task provided. Exiting.")
            break

        source_files = glob_match(task['glob_pattern'])
        for file in source_files:
            logger.log_operation(f"Processing file: {file}")
            try:
                langchain_agent.refactor_code(file, task['refactoring'])
                build_code.build_project(task['build_tool'])
            except Exception as e:
                logger.log_operation(f"Error occurred: {str(e)}")
                continue

        logger.log_operation("Refactoring task completed")

if __name__ == "__main__":
    main()
```