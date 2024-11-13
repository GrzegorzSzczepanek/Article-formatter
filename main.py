from FileManager import FileManager
from ApiManager import ApiManager

def main() -> None:
    file_manager = FileManager()
    file_path = "file.txt"
    file_content = file_manager.read_file(file_path)
    api_manager = ApiManager()
    print(api_manager.get_completions(file_path=file_path))
    print(file_manager.read_as_paragraphs(file_path)[1])
    
if __name__ == "__main__":
    main()
