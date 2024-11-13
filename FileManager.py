
class FileManager:
    def __init__(self):
        pass

    def read_file(self, file_path: "str") -> str:
        """
        Read the contents of a file
        Args:
            file_path (str): The path to the file
        """
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(self, file_path, content: str) -> None:
        """
        Write content to a file
        Args:
            file_path (str): The path to the file
            content (str): The content to write to the file
        """
        with open(file_path, 'w') as file:
            file.write(content)
            
    def read_as_paragraphs(self, file_path: str) -> list[str]:
        """
        Read the contents of a file and split it into paragraphs
        Args:
            file_path (str): The path to the file
        """
        with open(file_path, 'r') as file:
            return file.read().split("\n\n")