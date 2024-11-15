import logging
import os
from bs4 import BeautifulSoup
import requests


class FileManager:
    def __init__(self):
        pass

    def read_file(self, file_path: str) -> str:
        """
        Read the contents of a file.
        Args:
            file_path (str): The path to the file.

        Returns:
            str: The content of the file.

        Raises:
            FileNotFoundError: If the file does not exist.
            IOError: If the file cannot be read.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except IOError as e:
            raise IOError(
                f"An error occurred while reading the file '{file_path}': {e}"
            )

    def write_file(self, file_path: str, content: str) -> None:
        """
        Write content to a file.
        Args:
            file_path (str): The path to the file.
            content (str): The content to write to the file.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
        except IOError as e:
            raise IOError(
                f"An error occurred while writing to the file '{file_path}': {e}"
            )

    def extract_image_alts(self, html_content: str) -> list[str]:
        """
        Extract all alt texts from <img> tags in the provided HTML content.

        Args:
            html_content (str): The HTML content to parse.

        Returns:
            List[str]: A list of alt texts in the order they appear in the HTML.
        """
        soup = BeautifulSoup(html_content, "html.parser")
        img_tags = soup.find_all("img")
        alts = [img.get("alt", "") for img in img_tags]
        return alts

    def replace_image_placeholders(
        self, html_content: str, image_filenames: list[str]
    ) -> str:
        """
        Replace image placeholders in the HTML content with actual image filenames.

        Args:
            html_content (str): The original HTML content with placeholders.
            image_filenames (List[str]): A list of image filenames to replace the placeholders.

        Returns:
            str: The updated HTML content with actual image filenames.
        """
        soup = BeautifulSoup(html_content, "html.parser")
        img_tags = soup.find_all("img")

        for img_tag, filename in zip(img_tags, image_filenames):
            img_tag["src"] = filename

        return str(soup)

    def download_image(self, url: str, save_path: str) -> None:
        """
        Download an image from a URL and save it to the specified path.

        Args:
            url (str): The URL of the image to download.
            save_path (str): The local path where the image will be saved.

        Raises:
            Exception: If the image cannot be downloaded.
        """
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(save_path, "wb") as out_file:
                for chunk in response.iter_content(chunk_size=8192):
                    out_file.write(chunk)
        except Exception as e:
            raise Exception(
                f"An error occurred while downloading the image from '{url}': {e}"
            )

    def insert_content_into_body(self, template_html: str, content_html: str) -> str:
        """
        Insert content into the <body> section of a template HTML.

        Args:
            template_html (str): The HTML template with an empty <body> section.
            content_html (str): The HTML content to insert into the <body>.

        Returns:
            str: The combined HTML content.
        """
        try:
            soup = BeautifulSoup(template_html, "html.parser")
            body = soup.body
            if body is None:
                raise ValueError("Szablon HTML nie zawiera sekcji <body>.")
            
            body.clear()
            logger = logging.getLogger(__name__)
            logger.info("Wstawianie zawartości artykułu do szablonu...")

            article_soup = BeautifulSoup(content_html, "html.parser")
            body.append(article_soup)
            return str(soup)
        except Exception as e:
            raise Exception(f"An error occurred while inserting content into body: {e}")
        
        
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info("This is an INFO log.")
    logger.warning("This is a WARNING log.")
    logger.error("This is an ERROR log.")

