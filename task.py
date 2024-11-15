import openai
import requests
from dotenv import load_dotenv
import os

# Ustaw klucz API OpenAI
load_dotenv()
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
1. Użyj odpowiednich tagów HTML do strukturyzacji treści.
2. W miejscach, gdzie warto wstawić grafiki, oznacz je tagiem <img> z atrybutem src="image_placeholder.jpg".
   Dodaj atrybut alt z dokładnym promptem opisującym grafikę oraz podpis pod grafiką.
3. Nie dodawaj CSS ani JavaScript. 
4. Kod powinien zawierać wyłącznie zawartość do wstawienia pomiędzy <body> i </body>. Nie generuj meta tagów <head></head> oraz <body></body>

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