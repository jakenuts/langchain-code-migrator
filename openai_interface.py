```python
import openai
from logger import log_operation

class OpenAIInterface:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    @log_operation
    def generate_code(self, prompt, max_tokens=100):
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()

    @log_operation
    def translate_code(self, code, target_language):
        prompt = f"Translate the following {code['language']} code to {target_language}:\n{code['content']}"
        translated_code = self.generate_code(prompt)
        return translated_code
```