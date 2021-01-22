import selenium
import re
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

browser = Chrome('./webdrivers/windows/chromedriver.exe')

def scrape(url, count = 10):
    browser.get(url)
    raw = browser.page_source
    out = re.findall(r"href=\"(/watch\?v=\w+)\"", raw)[:count] #find all of type [href="/watch?v=]
    return list(map(lambda x: "youtube.com"+x, out))

def paramToUrl(query):
    base = "https://www.youtube.com/results?search_query="
    out = ""
    for c in query:
        if c == ' ':
            out+="+"
        if c.isalnum():
            out+=c
    return base+out

def getThumbnailUrl(url):
    browser.get("http://www.get-youtube-thumbnail.com/")
    elem = browser.find_element_by_id("youtubeLink")
    elem.send_keys(url)
    button = browser.find_element_by_id("get")
    button.click()
    imgUrl = browser.find_element_by_id("copyimageURL")
    return imgUrl.get_attribute("value")

if __name__ == '__main__':
    query = input("Enter a search query:\n > ")
    urls = scrape(paramToUrl(query))
    print(urls)
    
    print(getThumbnailUrl("youtube.com/watch?v=bzp3vt5aGDo"))