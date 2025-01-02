# Application Documentation for Processing Articles Using the OpenAI API (Polish CLI)

This CLI application automates the process of formatting text files into structured HTML using the OpenAI API. It also downloads relevant images based on alt text prompts.

---

## **Project Description**

This application processes text files containing articles, generates structural HTML with OpenAI API calls, and downloads the corresponding graphics based on descriptions. The generated HTML is saved as `artykul.html`. Additionally, the application can create an article preview in `podglad.html` based on the `szablon.html` template and the newly generated `artykul.html`.

---

## **Detailed Operation**

1. **Initialization**: `main.py` initializes `FileManager` and `ApiManager`.
2. **Reading the File**: The article is read from `file.txt` using `file_manager.read_file`.
3. **Generating HTML**: The OpenAI API creates HTML with placeholders for images using the `api_manager.generate_html` method.
4. **Creating Images**: Images are generated based on alt tags using `api_manager.generate_image_url`.
5. **Downloading Images**: The downloaded images are saved locally via `file_manager.download_image`.
6. **Replacing Placeholders**: The `<img>` tags are replaced with real file paths for images using `file_manager.replace_image_placeholders`.
7. **Saving HTML**: The finished HTML is saved as `artykul.html` using `file_manager.write_file`.
8. **Creating the Preview**: A `podglad.html` file is generated based on the `szablon.html` template and `artykul.html` using `main.py`.

---

## **File Structure**

- **main.py**  
  The main program logic, responsible for the entire process: reading the article, generating HTML, creating images, and saving the final HTML file.

- **ApiManager.py**  
  A module for handling communication with the OpenAI API:
  - **`ApiManager` class** provides methods:
    - `generate_html` – generates HTML from the article content.
    - `generate_image_url` – generates an image based on the description in the alt tag.
    - `get_completions` – an optional method to fetch text-based completions.

- **FileManager.py**  
  A module for file operations:
  - **`FileManager` class** provides methods:
    - `read_file` – reads the article content.
    - `write_file` – saves the generated HTML.
    - `extract_image_alts` – extracts alt tags from HTML.
    - `replace_image_placeholders` – replaces `<img>` placeholders with actual file paths for images.
    - `download_image` – downloads images from a URL based on generated prompts.

- **requirements.txt**  
  A file containing the list of required libraries along with their versions.

---

## **Requirements**

Before running the application, create a virtual environment and install the required libraries:

> **Mac/Linux**
```bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

> **Windows**
```cmd
py -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

The `requirements.txt` file contains:

- `openai==1.54.4`
- `beautifulsoup4==4.12.3`
- `requests==2.32.3`

---

## **Environment Settings**

To enable the application to use the OpenAI API, set your API key:

```bash
export OPENAI_API_KEY="your_api_key"
```

```cmd
set OPENAI_API_KEY="your_api_key"
```

Replace `"your_api_key"` with your actual OpenAI API key. This command sets the `OPENAI_API_KEY` environment variable, which the application uses for authenticating with the OpenAI API.

---

## **Installing Libraries**

Install the required modules by running:

```bash
pip install -r requirements.txt
```

---

## **Using the Command-Line Interface (CLI)**

The application offers a command-line interface (CLI) with two main commands:

1. **`generate-html`**: Generates the `artykul.html` file from a text file.
2. **`generate-images`**: Generates images based on the `<img>` tags (with `alt` attributes) found in the existing `artykul.html` file.

Below is a step-by-step guide for running the full process.

### **Generating an HTML File**

To generate the `artykul.html` file from the text file `file.txt`, use:

> **Mac/Linux**
```bash
python3 main.py generate-html --input file.txt --output artykul.html
```

> **Windows**
```cmd
py main.py generate-html --input file.txt --output artykul.html
```

**Optional parameters**:

- `--input`: Specifies the text file containing the article (defaults to `file.txt`).
- `--output`: Specifies the name of the output HTML file (defaults to `artykul.html`).

---

### **Generating Images**

After generating `artykul.html`, you can create images based on `alt` attributes in `<img>` tags:

> **Mac/Linux and Windows**
```bash
python3 main.py generate-images --html artykul.html
```

**Optional parameter**:

- `--html`: Specifies the HTML file to process (defaults to `artykul.html`).

---

### **Running the Full Process**

To generate both the HTML file and images in a single sequence:

> **Linux/macOS**
```bash
python main.py generate-html --input file.txt --output artykul.html && python main.py generate-images --html artykul.html
```

> **Windows**
```cmd
py main.py generate-html --input file.txt --output artykul.html & py main.py generate-images --html artykul.html
```

---

### **Generating a Preview**

To generate `podglad.html` from the `szablon.html` template and `artykul.html`, run:

> **Mac/Linux**
```bash
python3 main.py create-podglad --szablon szablon.html --artykul artykul.html --podglad podglad.html
```

> **Windows**
```cmd
py main.py create-podglad --szablon szablon.html --artykul artykul.html --podglad podglad.html
```

**Parameters**:

- `--szablon`: Specifies the HTML file with the template.
- `--artykul`: Specifies the HTML file containing the article.
- `--podglad`: Specifies the name of the output HTML preview file.

After executing these steps, the `artykul.html` file will contain the newly generated images and updated paths to them. The `podglad.html` file will show a preview of the final article based on the given template.

---

## **Used Libraries**

- **`openai`** – interface for communicating with the OpenAI API.
- **`beautifulsoup4`** – used for parsing and editing HTML structure.
- **`requests`** – used to download images from a URL.
- **`os`** – used for file operations.

Additionally, `ApiManager.py` and `FileManager.py` include the `ApiManager` and `FileManager` classes with corresponding methods for API communication and file operations.
