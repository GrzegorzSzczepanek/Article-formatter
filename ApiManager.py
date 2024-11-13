import openai
import os

class ApiManager:
    def __init__(self):
        openai._api_key = self.get_api_key()

    def get_api_key(self) -> str:
        """
        Get the OpenAI API key from environment variables
        """
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key is None:
            raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
        return api_key
    
    def get_completions(self, prompt: str, max_tokens: int = 100) -> list:
        """
        Get completions from the OpenAI API using ChatCompletion.

            prompt (str): The input prompt to generate completions for.
            max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 100.

        Returns:
            list: A list of completion choices from the OpenAI API.
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
    
    def generate_image(self, prompt: str, n: int = 1, size: str = "1024x1024") -> list:
        """
        Generate images from the OpenAI API using DALL-E.

            prompt (str): The input prompt to generate images for.
            n (int, optional): The number of images to generate. Defaults to 1.
            size (str, optional): The size of the generated images. Defaults to "1024x1024".

        Returns:
            list: A list of URLs of the generated images from the OpenAI API.
        """
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size
        )
        return [image['url'] for image in response['data']]