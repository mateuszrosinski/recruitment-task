# recruitment-task
Rozwiązanie zadania rekrutacyjnego

Aplikacja Generująca Plik HTML na podstawie podlinkowanego artykułu z wykorzystaniem API OpenAI.

Opis projektu
Aplikacja pobiera artykuł z podanego URL, przekształca jego treść na strukturę HTML zgodnie z określonymi wytycznymi i zapisuje wynikowy kod HTML w pliku artykul.html.

Główne funkcjonalności
Pobieranie treści artykułu z URL.
Przetwarzanie treści za pomocą OpenAI API.
Generowanie kodu HTML zgodnego z wytycznymi i zapisanie go do pliku artykul.html.
Bezpieczne przechowywanie klucza API w pliku .env.(ze względów bezpieczeństwa mój plik z kodem dostępu do API platformy OPENAI nie jest przechowywany w repozytorium)
Dla chętnych:
Aplikacja tworzy plik szablon.html z którego odczytujemy treść pliku artykul.html, dodajemy do niego style CSS.
Zawiera również plik podglad.html, który prezentuje artykuł wprowadzony do pliku szablon.html.

Wymagania potrzebne do korzystania z aplikacji:
Aby uruchomić aplikację, upewnij się, że masz zainstalowane:

Python 3.9+
Pakiety Python wymienione w requirements.txt(plik znajduje się w repozytorium):
openai
requests
python-dotenv

Instrukcja instalacji:
Krok 1: Sklonowanie repozytorium
By pobrać repozytorium z aplikacją na swój komputer, wprowadź poniższą komendę w edytorze kodu:

# paste it in bash or powershell
git clone https://github.com/mateuszrosinski/recruitment-task.git

Przejdź do folderu: 
cd recruitment-task

Krok 2: Utwórz środowisko wirtualne:

# paste it in bash or powershell
python -m venv venv

Aktywuj środowisko:

Jeśli używasz Windows:

venv\Scripts\activate

Jeśli używasz Linux/MacOS:

source venv/bin/activate

Krok 3: Instalacja zależności

#code
pip install -r requirements.txt

Krok 4: Konfiguracja klucza API OpenAI
1. Utwórz plik .env w katalogu głównym projektu.
2. Wprowadź swój klucz do API z platformy Open Ai
# w pliku .env
OPENAI_API_KEY="Twój_klucz_API"

Krok 5: Uruchomienie aplikacji

Uruchom aplikację za pomocą:

python task.py
