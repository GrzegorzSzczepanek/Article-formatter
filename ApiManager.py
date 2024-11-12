import openai
import os

class ApiManager:
    def __init__(self):
        openai._api_key = self.get_api_key()

    def get_api_key(self):
        """
        Get the OpenAI API key from environment variables
        """
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key is None:
            raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
        return api_key
    
    def get_completions(self, prompt: str, max_tokens: int = 100):
        """
        Get completions from the OpenAI API using ChatCompletion
        """
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens
        )
        return completion.choices