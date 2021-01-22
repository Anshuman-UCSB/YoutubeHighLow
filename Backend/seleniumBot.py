import selenium
import re
from selenium.webdriver import Chrome

browser = Chrome('./webdrivers/windows/chromedriver.exe')

def scrape(url, count = 10):
    browser.get(url)
    raw = browser.page_source
    print(re.findall(r"href=\"/watch\?v=\w+\"", raw)) #find all of type [href="/watch?v=]
    
def paramToUrl(query):
    base = "https://www.youtube.com/results?search_query="
    out = ""
    for c in query:
        if c == ' ':
            out+="+"
        if c.isalnum():
            out+=c
    return base+out


if __name__ == '__main__':
    print(paramToUrl("I want to goog42l1e this!"))
    # scrape("https://www.youtube.com/results?search_query=drama")
