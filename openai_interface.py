```python
import openai
from logger import Logger

class OpenAIInterface:
    def __init__(self, api_key):
        self.api_key = api_key
        self.logger = Logger(__name__)
        openai.api_key = self.api_key

    def generate_code(self, prompt, max_tokens=100):
        try:
            response = openai.Completion.create(
                engine="davinci-codex",
                prompt=prompt,
                max_tokens=max_tokens
            )
            self.logger.log_operation(f"Generated code with prompt: {prompt}")
            return response.choices[0].text.strip()
        except Exception as e:
            self.logger.log_operation(f"Error in generating code: {str(e)}")
            return None
```