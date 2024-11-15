

import logging
import argparse
import os
from file_manager import FileManager
from api_manager import ApiManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_html(file_manager: FileManager, api_manager: ApiManager, input_file: str, output_file: str) -> None:
    """
    Generates HTML content from an input file and writes it to an output file.
    This function reads the content of an input file using the provided FileManager,
    generates HTML content with image placeholders using the provided ApiManager,
    and writes the generated HTML content to an output file.
    Args:
        file_manager (FileManager): An instance of FileManager to handle file operations.
        api_manager (ApiManager): An instance of ApiManager to generate HTML content.
        input_file (str): The path to the input file containing the article content.
        output_file (str): The path to the output file where the generated HTML content will be saved.
    Raises:
        Exception: If an error occurs during the process, it will be logged.
    """
    try:
        article_content = file_manager.read_file(input_file)
        logger.info(f"Successfully read the article from '{input_file}'.")

        logger.info("Generating initial HTML content with image placeholders...")
        initial_html = api_manager.generate_html(article_content)
        logger.info("Initial HTML content generated successfully.")

        file_manager.write_file(output_file, initial_html)
        logger.info(f"Final HTML content written to '{output_file}' successfully.")

    except Exception as e:
        logger.error(f"An error occurred while generating HTML: {e}")

def generate_images(file_manager: FileManager, api_manager: ApiManager, html_file: str) -> None:
    """
    Generates images based on the alt texts found in an HTML file and replaces the image placeholders
    in the HTML with the generated image filenames.
    Args:
        file_manager (FileManager): An instance of FileManager to handle file operations.
        api_manager (ApiManager): An instance of ApiManager to handle API requests for image generation.
        html_file (str): The path to the HTML file containing image placeholders.
    Returns:
        None
    Raises:
        Exception: If an error occurs during the image generation process.
    """
    try:
        if not os.path.exists(html_file):
            logger.error(f"The file '{html_file}' does not exist. Please generate HTML first.")
            return

        html_content = file_manager.read_file(html_file)
        logger.info(f"Successfully read the HTML content from '{html_file}'.")

        logger.info("Extracting image alt texts from the HTML...")
        image_alts = file_manager.extract_image_alts(html_content)
        logger.info(f"Extracted {len(image_alts)} image alt texts.")

        if not image_alts:
            logger.info("No image alt texts found. No images to generate.")
            return

        image_filenames = []
        for idx, alt in enumerate(image_alts, start=1):
            if not alt.strip():
                logger.warning(f"Image {idx} has an empty alt text. Skipping image generation.")
                continue
            logger.info(f"Generating image {idx} based on alt text: '{alt}'")
            image_url = api_manager.generate_image_url(alt)
            
            
            image_filename = f"image_placeholder_{idx}.jpg"
            save_path = f"{image_filename}"
            file_manager.download_image(image_url, save_path)
            logger.info(f"Image {idx} downloaded and saved as '{image_filename}'.")
            image_filenames.append(image_filename)

        if not image_filenames:
            logger.info("No images were generated.")
            return

        logger.info("Replacing image placeholders in HTML with actual image filenames...")
        final_html = file_manager.replace_image_placeholders(html_content, image_filenames)
        logger.info("Image placeholders replaced successfully.")

        file_manager.write_file(html_file, final_html)
        logger.info(f"Updated HTML content written to '{html_file}' successfully.")

    except Exception as e:
        logger.error(f"An error occurred while generating images: {e}")
        

def create_podglad(file_manager: FileManager, szablon_file: str, artykul_file: str, podglad_file: str) -> None:
    """
    Creates podglad.html by inserting the content of artykul.html into the body of szablon.html.
    """
    try:
        logger.info(f"Rozpoczynanie tworzenia podglądu HTML. Szablon: '{szablon_file}', Artykuł: '{artykul_file}', Podgląd: '{podglad_file}'.")
        
        if not os.path.exists(szablon_file):
            logger.error(f"Plik szablonu '{szablon_file}' nie istnieje.")
            return
        if not os.path.exists(artykul_file):
            logger.error(f"Plik artykułu '{artykul_file}' nie istnieje.")
            return

        szablon_content = file_manager.read_file(szablon_file)
        artykul_content = file_manager.read_file(artykul_file)
        logger.info("Pomyślnie odczytano zawartość szablonu i artykułu.")

        logger.info("Wstawianie zawartości artykułu do sekcji <body> szablonu...")
        podglad_content = file_manager.insert_content_into_body(szablon_content, artykul_content)
        logger.info("Zawartość artykułu została pomyślnie wstawiona do szablonu.")

        file_manager.write_file(podglad_file, podglad_content)
        logger.info(f"Plik podglądu został zapisany jako '{podglad_file}'.")
    except Exception as e:
        logger.error(f"Wystąpił błąd podczas tworzenia podglądu HTML: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Narzędzie CLI do generowania HTML i obrazów dla artykułów.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Polecenia podrzędne')

    parser_html = subparsers.add_parser('generate-html', help='Generuj artykul.html z pliku tekstowego')
    parser_html.add_argument(
        '--input',
        type=str,
        default='file.txt',
        help='Plik wejściowy zawierający artykuł (domyślnie: file.txt)'
    )
    parser_html.add_argument(
        '--output',
        type=str,
        default='artykul.html',
        help='Plik wyjściowy HTML (domyślnie: artykul.html)'
    )

    parser_images = subparsers.add_parser('generate-images', help='Generuj obrazy dla istniejącego artykul.html')
    parser_images.add_argument(
        '--html',
        type=str,
        default='artykul.html',
        help='Plik HTML do przetworzenia (domyślnie: artykul.html)'
    )

    parser_podglad = subparsers.add_parser('create-podglad', help='Tworzy podglad.html na podstawie szablonu i artykułu')
    parser_podglad.add_argument(
        '--szablon',
        type=str,
        default='szablon.html',
        help='Plik szablonu HTML (domyślnie: szablon.html)'
    )
    parser_podglad.add_argument(
        '--artykul',
        type=str,
        default='artykul.html',
        help='Plik artykułu HTML (domyślnie: artykul.html)'
    )
    parser_podglad.add_argument(
        '--podglad',
        type=str,
        default='podglad.html',
        help='Plik wyjściowy podglądu HTML (domyślnie: podglad.html)'
    )

    args = parser.parse_args()

    file_manager = FileManager()
    api_manager = ApiManager()

    if args.command == 'generate-html':
        generate_html(file_manager, api_manager, args.input, args.output)
    elif args.command == 'generate-images':
        generate_images(file_manager, api_manager, args.html)
    elif args.command == 'create-podglad':
        create_podglad(file_manager, args.szablon, args.artykul, args.podglad)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
