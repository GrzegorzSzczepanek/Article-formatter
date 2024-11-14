import logging
from FileManager import FileManager
from ApiManager import ApiManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main() -> None:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    file_manager = FileManager()
    api_manager = ApiManager()
    
    input_file = "file.txt"
    output_file = "artykul.html"

    try:
        article_content = file_manager.read_file(input_file)
        logger.info(f"Successfully read the article from '{input_file}'.")

        logger.info("Generating initial HTML content with image placeholders...")
        initial_html = api_manager.generate_html(article_content)
        logger.info("Initial HTML content generated successfully.")

        logger.info("Extracting image alt texts from the HTML...")
        image_alts = file_manager.extract_image_alts(initial_html)
        logger.info(f"Extracted {len(image_alts)} image alt texts.")

        image_filenames = []
        for idx, alt in enumerate(image_alts, start=1):
            logger.info(f"Generating image {idx} based on alt text: '{alt}'")
            image_url = api_manager.generate_image_url(alt)
            image_filename = f"image_placeholder.jpg"
            save_path = f"{image_filename}"
            file_manager.download_image(image_url, save_path)
            logger.info(f"Image {idx} downloaded and saved as '{image_filename}'.")
            image_filenames.append(image_filename)

        logger.info("Replacing image placeholders in HTML with actual image filenames...")
        final_html = file_manager.replace_image_placeholders(initial_html, image_filenames)
        logger.info("Image placeholders replaced successfully.")

        file_manager.write_file(output_file, final_html)
        logger.info(f"Final HTML content written to '{output_file}' successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()