# zadanie

1. Łączy się z API OpenAI;
2. Odczytuje plik tekstowy z artykułem – tu znajdziesz plik do pobrania;
3. Treść artykułu wraz z promptem przekazuje do OpenAI w celu obróbki (opisane poniżej);
4. Zapisuje otrzymany od OpenAI kod w pliku artykul.html.

## Dodawanie klucza API

Aby dodać klucz API, użyj poniższego polecenia w terminalu:

```sh
export OPENAI_API_KEY="twój_klucz_api"
```

Upewnij się, że zastąpiłeś `"twój_klucz_api"` swoim rzeczywistym kluczem API. To polecenie ustawi zmienną środowiskową `OPENAI_API_KEY`, która będzie używana przez aplikację do uwierzytelniania się w API OpenAI.
