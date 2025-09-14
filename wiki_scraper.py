import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(topic):
    url =f"https://en.wikipedia.org/wiki/{topic}"
    response= requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    paragraph = soup.find("p")
    if paragraph : 
        return paragraph.get_text()
    else :
        return "No paragraph found."



if __name__ == "__main__":
    topic = "Artificial_intelligence"
    text = scrape_wikipedia(topic)
    with open("ai_intro.txt","w",encoding ="utf-8")as f:
        f.write(text)
        print("Paragraph saved to ai_intro.txt")