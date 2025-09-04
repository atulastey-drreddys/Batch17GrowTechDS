import google.generativeai as genai
from newspaper import Article

genai.configure(api_key = "Enter your API key")
model = genai.GenerativeModel("gemini-2.5-flash")

def scrape_website_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"Error Fetching content : {str(e)}"
    
def Summerize_with_gemini(content):
    prompt = f"Summerize the following website content in a very simple point : \n\n{content}"
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    url = input("Enter the website URL : ")
    content = scrape_website_content(url)
    if "Error" in content:
        print(content)
    else:
        print("Website content summary")
        summary = Summerize_with_gemini(content)
        print(summary)