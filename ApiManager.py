import openai
import os
import logging
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class ApiManager:
    def __init__(self):
        self.api_key = self.get_api_key()
        openai.api_key = self.api_key

    def get_api_key(self) -> str:
        """
        Get the OpenAI API key from environment variables
        """
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key is None:
            raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
        return api_key
    
    # @retry(
    #     wait=wait_exponential(multiplier=1, min=4, max=10),
    #     stop=stop_after_attempt(1),
    #     retry=retry_if_exception_type(Exception)
    # )
    
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
    
    # @retry(
    #     wait=wait_exponential(multiplier=1, min=4, max=10),
    #     stop=stop_after_attempt(1),
    #     retry=retry_if_exception_type(Exception)
    # )
    
    def generate_html(self, article_content: str) -> str:
        """
        Generate HTML content from the article using OpenAI's GPT model.

        Args:
            article_content (str): The content of the article.

        Returns:
            str: The generated HTML content.

        Raises:
            Exception: If the API call fails.
        """
        prompt = (
            "Przekształć poniższy artykuł w czysty kod HTML, używając odpowiednich tagów "
            "do strukturyzacji treści. Określ miejsca, gdzie warto wstawić grafiki, oznaczając "
            "je tagiem <img> z atrybutem src=\"image_placeholder.jpg\" oraz dodaj atrybut alt "
            "z dokładnym opisem promptu, który można wykorzystać do wygenerowania grafiki. "
            "Atrybut alt powinien zawierać opis będący bezpośrednim odniesieniem do treści artykułu. "
            "Umieść podpisy pod grafikami używając odpowiednich tagów HTML. Nie używaj CSS ani JavaScript. "
            "Zwróć tylko sformatowaną zawartość, bez znaczników <html>, <head> i <body>, "
            "<head> ani <body>.\n\nOto Artykuł:\n"
            f"{article_content}"
        )

        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert in converting articles to structured HTML."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.3,
            )
            html_content = response.choices[0].message.content.strip()
            return html_content
        except Exception as e:
            raise Exception(f"An error occurred while generating HTML: {e}")
        
    def generate_image_url(self, prompt: str, size: str = "256x256") -> str:
        """
        Generate an image URL using OpenAI's DALL-E API based on the provided prompt.

        Args:
            prompt (str): The description of the image to generate.
            size (str, optional): The size of the image. Defaults to "256x256".

        Returns:
            str: The URL of the generated image.

        Raises:
            Exception: If the API call fails.
        """
        try:
            response = openai.images.generate(
                prompt=prompt,
                n=1,
                size=size
            )
            image_url = response.data[0].url
            return image_url
        except Exception as e:
            logger.error(f"Unexpected error during image generation: {e}")
            raise
    
    
if __name__ == "__main__":
    api_manager = ApiManager()
    article_content = "This is a test article."
    html_content = api_manager.generate_html(article_content)
    print(html_content)
    image_alt = "A colorful abstract painting"
    image_url = api_manager.generate_image_url(image_alt)
    print(image_url)
    completions = api_manager.get_completions("What is the capital of France?")
    for completion in completions:
        print(completion.message.content)