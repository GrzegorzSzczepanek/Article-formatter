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


def main() -> None:
    parser = argparse.ArgumentParser(description="A CLI tool to generate HTML and images for articles.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Sub-commands')

    
    parser_html = subparsers.add_parser('generate-html', help='Generate artykul.html from file.txt')
    parser_html.add_argument(
        '--input',
        type=str,
        default='file.txt',
        help='Input text file containing the article (default: file.txt)'
    )
    parser_html.add_argument(
        '--output',
        type=str,
        default='artykul.html',
        help='Output HTML file (default: artykul.html)'
    )

    
    parser_images = subparsers.add_parser('generate-images', help='Generate images for existing artykul.html')
    parser_images.add_argument(
        '--html',
        type=str,
        default='artykul.html',
        help='HTML file to process (default: artykul.html)'
    )

    args = parser.parse_args()

    file_manager = FileManager()
    api_manager = ApiManager()

    if args.command == 'generate-html':
        generate_html(file_manager, api_manager, args.input, args.output)
    elif args.command == 'generate-images':
        generate_images(file_manager, api_manager, args.html)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
