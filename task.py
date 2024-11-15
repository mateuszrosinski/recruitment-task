import openai
import requests
from dotenv import load_dotenv
import os

# Ustaw klucz API OpenAI
load_dotenv()
# Klucz api ze względów bezpieczeństwa nie zostanie wysłany na repozytorium. Są to wrażliwe dane.
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

# Pobierz treść artykułu
ARTICLE_URL = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"
article_response = requests.get(ARTICLE_URL)

if article_response.status_code != 200:
    raise Exception("Nie udało się pobrać artykułu.")

article_content = article_response.text

# Przygotowanie promptu dla OpenAI
prompt = f'''
Przekształć poniższy artykuł na kod HTML zgodny z następującymi wytycznymi:
1. Pierwsze zdanie artykułu powinno zostać zawarte w tagu <h1>.
   - Pod nagłówkiem <h1> umieść opis w postaci paragrafu oraz obraz w tagu <img>, gdzie:
     - Atrybut src="image_placeholder.jpg" wskazuje na miejsce obrazu.
     - Atrybut alt zawiera prompt opisujący grafikę.
2. Tagi <h2> powinny zostać użyte dla sekcji zatytułowanych: "Wyzwania etyczne i społeczne" oraz "Automatyzacja i przyszłość rynku pracy".
   - Pod każdym <h2> dodaj akapity z treścią oraz obraz w tagu <img> (z atrybutami src i alt).
3. Akapity treści nieprzypisane do <h1> lub <h2> pozostaw jako zwykłe paragrafy <p>.
4. Nie dodawaj żadnego stylu CSS ani JavaScript.
5. Kod powinien zawierać wyłącznie zawartość, którą należy umieścić pomiędzy <body> i </body>. Nie generuj tagów <head> ani <body>.
6. Konieczne jest wyświetlanie polskich znaków(UTF-8).

Artykuł:
{article_content}
'''

# Wysłanie zapytania do OpenAI
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # Lub "gpt-4", jeśli masz dostęp
    messages=[
        {"role": "system", "content": "Jesteś asystentem pomagającym generować kod HTML zgodny z podanymi wytycznymi."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=3000,
    temperature=0.7
)

# Zapisanie wygenerowanego kodu HTML
html_content = response.choices[0].message.content.strip()

html_content = html_content.replace("```html", "").replace("```", "").strip()
with open("artykul.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print(html_content)
print("Plik artykul.html został wygenerowany.")