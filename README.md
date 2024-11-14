Dokumentacja aplikacji do przetwarzania artykułów z użyciem OpenAI API
# Opis projektu

Aplikacja służy do przetwarzania plików tekstowych z artykułami, generowania strukturalnego HTML za pomocą OpenAI API oraz pobierania odpowiednich grafik na podstawie opisów. Wygenerowany HTML jest zapisywany jako `artykul.html`.

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

Przed uruchomieniem aplikacji należy zainstalować wymagane biblioteki:

```sh
pip install -r requirements.txt
```

Plik `requirements.txt` zawiera:

- `openai==1.54.4`
- `tenacity==9.0.0`
- `beautifulsoup4==4.12.3`
- `requests==2.32.3`

## Ustawienia środowiskowe

Aby aplikacja mogła korzystać z OpenAI API, ustaw klucz API:

```sh
export OPENAI_API_KEY="twój_klucz_api"
```

Zastąp `"twój_klucz_api"` swoim rzeczywistym kluczem API. To polecenie ustawia zmienną środowiskową `OPENAI_API_KEY`, która jest wykorzystywana przez aplikację do uwierzytelnienia się w API OpenAI.

## Instalacja zależności

Zainstaluj wymagane moduły, uruchamiając poniższe polecenie:

```sh
pip install -r requirements.txt
```

## Uruchamianie aplikacji

Gdy spełnione są wszystkie wymagania, uruchom aplikację:

```sh
python main.py
```

Aplikacja przetworzy plik `file.txt`, wygeneruje HTML, stworzy grafiki i zapisze końcowy plik `artykul.html` w katalogu projektu.

## Szczegółowy opis działania

1. **Inicjalizacja**: `main.py` inicjalizuje `FileManager` i `ApiManager`.
2. **Odczyt pliku**: Artykuł jest odczytywany z `file.txt` przy użyciu `file_manager.read_file`.
3. **Generowanie HTML**: OpenAI API tworzy HTML z miejscami na grafiki za pomocą metody `api_manager.generate_html`.
4. **Tworzenie grafik**: Na podstawie tagów alt generowane są obrazy przy użyciu `api_manager.generate_image_url`.
5. **Pobieranie obrazów**: Pobierane obrazy są zapisywane lokalnie za pomocą `file_manager.download_image`.
6. **Zamiana placeholderów**: Zamieniane są znaczniki `<img>` na rzeczywiste ścieżki plików graficznych za pomocą `file_manager.replace_image_placeholders`.
7. **Zapisanie HTML**: Gotowy HTML jest zapisywany jako `artykul.html` przy użyciu `file_manager.write_file`.

## Wykorzystane biblioteki

- `openai` – interfejs do komunikacji z OpenAI API.
- `tenacity` – umożliwia obsługę ponownych prób połączenia z API w przypadku błędów.
- `beautifulsoup4` – używana do parsowania i edycji struktury HTML.
- `requests` – używana do pobierania obrazów z URL.

Dodatkowo, pliki `ApiManager.py` oraz `FileManager.py` zawierają klasę `ApiManager` oraz `FileManager` z odpowiednimi metodami, które obsługują komunikację z API oraz operacje na plikach.