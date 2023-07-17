```python
import glob
import os
from langchain import Refactor
from logger import log_operation

@log_operation
def get_files(pattern, language):
    """
    Get all files in the current directory that match the given glob pattern and language.
    """
    files = glob.glob(pattern)
    return [file for file in files if file.endswith(language)]

@log_operation
def refactor_file(file, refactor_request):
    """
    Refactor a given file according to the user's request.
    """
    refactor = Refactor(file)
    refactor.apply(refactor_request)
    refactor.save()

@log_operation
def get_refactor_request():
    """
    Get the user's request for refactoring.
    """
    refactor_request = input("Enter your refactoring request: ")
    return refactor_request

@log_operation
def ask_continue():
    """
    Ask the user if they want to continue refactoring.
    """
    continue_request = input("Do you want to continue refactoring? (yes/no): ")
    return continue_request.lower() == "yes"
```