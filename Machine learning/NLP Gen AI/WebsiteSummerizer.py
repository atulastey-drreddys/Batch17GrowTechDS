import google.generativeai as genai
from newspaper import Article

genai.configure(api_key = "AIzaSyBHtrj9Py_7uS8o8tLBYOsh3Qw9I5NPWkA")
model = genai.GenerativeModel("gemini-2.5-flash")

def scrape_website_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text()
    except Exception as e:
        return e
    
def Summerize_with_gemini(content):
    promt = f"Summerize the following website content in a very simple "