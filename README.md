Dokumentacja aplikacji do przetwarzania artykułów z użyciem OpenAI API
Ta aplikacja CLI automatyzuje process formatowania

# Dokumentacja aplikacji do przetwarzania artykułów z użyciem OpenAI API

## Opis projektu

Aplikacja służy do przetwarzania plików tekstowych z artykułami, generowania strukturalnego HTML za pomocą OpenAI API oraz pobierania odpowiednich grafik na podstawie opisów. Wygenerowany HTML jest zapisywany jako `artykul.html`. Dodatkowo, aplikacja umożliwia wygenerowanie podglądu artykułu w pliku `podglad.html` na podstawie szablonu `szablon.html` oraz wygenerowanego artykułu `artykul.html`.


## Szczegółowy opis działania

1. **Inicjalizacja**: `main.py` inicjalizuje `FileManager` i `ApiManager`.
2. **Odczyt pliku**: Artykuł jest odczytywany z `file.txt` przy użyciu `file_manager.read_file`.
3. **Generowanie HTML**: OpenAI API tworzy HTML z miejscami na grafiki za pomocą metody `api_manager.generate_html`.
4. **Tworzenie grafik**: Na podstawie tagów alt generowane są obrazy przy użyciu `api_manager.generate_image_url`.
5. **Pobieranie obrazów**: Pobierane obrazy są zapisywane lokalnie za pomocą `file_manager.download_image`.
6. **Zamiana placeholderów**: Zamieniane są znaczniki `<img>` na rzeczywiste ścieżki plików graficznych za pomocą `file_manager.replace_image_placeholders`.
7. **Zapisanie HTML**: Gotowy HTML jest zapisywany jako `artykul.html` przy użyciu `file_manager.write_file`.
8. **Tworzenie podglądu**: Plik `podglad.html` jest generowany na podstawie szablonu `szablon.html` i artykułu `artykul.html` za pomocą `main.py`.


## Struktura plików

- **main.py** - Główna logika programu, odpowiedzialna za przepływ całego procesu: odczyt artykułu, generowanie HTML, tworzenie grafik oraz zapisanie gotowego pliku HTML.
- **ApiManager.py** - Moduł odpowiedzialny za komunikację z OpenAI API:
    - Klasa `ApiManager` zawiera metody:
        - `generate_html` - generuje HTML na podstawie treści artykułu.
        - `generate_image_url` - generuje obraz na podstawie opisu zawartego w tagu alt.
        - `get_completions` - opcjonalna metoda do pobierania odpowiedzi tekstowych.
- **FileManager.py** - Moduł do operacji na plikach:
    - Klasa `FileManager` zawiera metody:
        - `read_file` - odczytuje treść artykułu.
        - `write_file` - zapisuje wygenerowany HTML.
        - `extract_image_alts` - wyodrębnia tagi alt z HTML.
        - `replace_image_placeholders` - zamienia znaczniki `<img>` na faktyczne ścieżki do plików graficznych.
        - `download_image` - pobiera obrazy z URL na podstawie wygenerowanych promptów.
- **requirements.txt** - Plik zawierający listę wymaganych bibliotek wraz z wersjami.

## Wymagania

Przed uruchomieniem aplikacji należy stworzyć środowisko wirtualne i zainstalować wymagane biblioteki:

> Mac/Linux
```sh
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
> Windows
```cmd
py -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Plik `requirements.txt` zawiera:

- `openai==1.54.4`
- `beautifulsoup4==4.12.3`
- `requests==2.32.3`

## Ustawienia środowiskowe

Aby aplikacja mogła korzystać z OpenAI API, ustaw klucz API:

```sh
export OPENAI_API_KEY="twój_klucz_api"
```


```cmd
set OPENAI_API_KEY="twój_klucz_api"
```

Zastąp `"twój_klucz_api"` swoim rzeczywistym kluczem API. To polecenie ustawia zmienną środowiskową `OPENAI_API_KEY`, która jest wykorzystywana przez aplikację do uwierzytelnienia się w API OpenAI.

## Instalacja bibliotek

Zainstaluj wymagane moduły, uruchamiając poniższe polecenie:

```sh
pip install -r requirements.txt
```

## Korzystanie z interfejsu wiersza poleceń (CLI)

Aplikacja oferuje interfejs wiersza poleceń (CLI) z dwoma głównymi komendami:
1. `generate-html`: Generuje plik HTML `artykul.html` na podstawie treści z pliku tekstowego.
2. `generate-images`: Generuje obrazy na podstawie tagów `<img>` z atrybutami `alt` w istniejącym pliku `artykul.html`.

Poniżej znajduje się instrukcja krok po kroku do uruchomienia pełnego procesu.

### Generowanie pliku HTML

Aby wygenerować plik `artykul.html` z pliku tekstowego `file.txt`, użyj polecenia:

> Mac/Linux
```sh
python3 main.py generate-html --input file.txt --output artykul.html
```

> Windows

```cmd
py main.py generate-html --input file.txt --output artykul.html
```

Parametry opcjonalne:

- `--input`: Określa plik tekstowy z artykułem (domyślnie `file.txt`).
- `--output`: Określa nazwę pliku wyjściowego HTML (domyślnie `artykul.html`).

### Generowanie obrazów

Po wygenerowaniu pliku `artykul.html`, można użyć poniższego polecenia, aby wygenerować obrazy na podstawie atrybutów `alt` w tagach `<img>`:

> Mac and Windows
```sh
python3 main.py generate-images --html artykul.html
```

Parametr opcjonalny:

- `--html`: Określa plik HTML do przetworzenia (domyślnie `artykul.html`).

### Uruchomienie pełnego procesu

Aby wygenerować zarówno HTML, jak i obrazy w jednym procesie, można użyć następujących poleceń razem:

> Linux/macOS:

```sh
python main.py generate-html --input file.txt --output artykul.html && python main.py generate-images --html artykul.html
```

> Windows:

```sh
py main.py generate-html --input file.txt --output artykul.html & py main.py generate-images --html artykul.html
```

### Generowanie podglądu

Aby wygenerować plik `podglad.html` na podstawie szablonu `szablon.html` i artykułu `artykul.html`, użyj polecenia:

> Mac/Linux
```sh
python3 main.py create-podglad --szablon szablon.html --artykul artykul.html --podglad podglad.html
```

> Windows
```cmd
py main.py create-podglad --szablon szablon.html --artykul artykul.html --podglad podglad.html
```

Parametry:

- `--szablon`: Określa plik HTML z szablonem.
- `--artykul`: Określa plik HTML z artykułem.
- `--podglad`: Określa nazwę pliku wyjściowego HTML z podglądem.

Po wykonaniu tego polecenia, plik `podglad.html` będzie zawierał wygenerowany podgląd artykułu na podstawie szablonu.

Po wykonaniu tych kroków, plik `artykul.html` będzie zawierał wygenerowane obrazy oraz odpowiednio zaktualizowane ścieżki do nich.

## Wykorzystane biblioteki

- `openai` – interfejs do komunikacji z OpenAI API.
- `beautifulsoup4` – używana do parsowania i edycji struktury HTML.
- `requests` – używana do pobierania obrazów z URL.
- `os` - Uzywana do działania na plikach.

Dodatkowo, pliki `ApiManager.py` oraz `FileManager.py` zawierają klasę `ApiManager` oraz `FileManager` z odpowiednimi metodami, które obsługują komunikację z API oraz operacje na plikach.