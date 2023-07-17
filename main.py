```python
import sys
from langchain_agent import LangchainAgent
from logger import Logger
from openai_interface import OpenAIInterface
from build_code import BuildCode
from memory_buffer import MemoryBuffer

def main():
    logger = Logger()
    memory_buffer = MemoryBuffer()
    openai_interface = OpenAIInterface()
    build_code = BuildCode()
    langchain_agent = LangchainAgent(logger, memory_buffer, openai_interface, build_code)

    while True:
        logger.log("Enter the language of the source code files (typescript, python, c#): ")
        language = input()
        logger.log("Enter the glob pattern to match: ")
        glob_pattern = input()
        logger.log("Enter the refactoring task: ")
        refactoring_task = input()

        try:
            langchain_agent.review_and_refactor_source_code_files(language, glob_pattern, refactoring_task)
        except Exception as e:
            logger.log(f"An error occurred: {str(e)}")
            sys.exit(1)

        logger.log("Do you want to perform another refactoring task? (yes/no): ")
        user_response = input()
        if user_response.lower() != 'yes':
            break

    logger.log("Application has ended successfully.")

if __name__ == "__main__":
    main()
```