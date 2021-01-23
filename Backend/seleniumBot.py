import selenium
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from time import sleep

from firebase import *

browser = Chrome('./webdrivers/windows/chromedriver.exe')
browser.implicitly_wait(10)

def scrape(url, count = 10):
    browser.get(url)
    raw = browser.page_source
    total = re.findall(r"href=\"(/watch\?v=\w+)\"", raw) #find all of type [href="/watch?v=]
    out = []
    for v in total:
        if v not in out:
            out.append(v)
            if(len(out) >= count):
                return list(map(lambda x: "https://www.youtube.com"+x, out))
    return list(map(lambda x: "https://www.youtube.com"+x, out))
        

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

def toJson(title, thumbnail, views):
    return {"title":title, "thumbnail":thumbnail, "views":views}

def getJsonFromUrl(url):
    browser.get(url)
    # sleep(3)

    elem = browser.find_element_by_xpath("//*[@id=\"count\"]/yt-view-count-renderer/span[1]")
    views = int("".join([c for c in elem.text if c.isnumeric()]))

    elem = browser.find_element_by_xpath("//*[@id=\"container\"]/h1/yt-formatted-string")
    title = elem.text

    # https://www.youtube.com/watch?v=hPjfkQg0Ygs
    # http://i3.ytimg.com/vi/hPjfkQg0Ygs/maxresdefault.jpg
    extension = url[url.index("?v=")+3:]

    thumbnailUrl = f"http://i3.ytimg.com/vi/{extension}/maxresdefault.jpg"

    return toJson(title, thumbnailUrl,views)

def populateFromQuery(query, count=10):
    urls = scrape(paramToUrl(query), count=count)
    print(urls)
    for url in urls:
        pushJson(getJsonFromUrl(url))



if __name__ == '__main__':
    populateFromQuery("lets play",count=10)
    browser.quit()