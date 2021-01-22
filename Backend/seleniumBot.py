import selenium
import re
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import firebase

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
                return list(map(lambda x: "youtube.com"+x, out))
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

def getViews(url):
    browser.get(url)
    rgx = r"\"viewCount\":\"(\d+)\""
    rgx = r"\"viewCount\":"
    
    print(re.match(rgx,browser.page_source))

def getTitle(url):
    browser.get(url)
    title = browser.find_element_by_name("content")
    print(title)
    

def toJson(title, thumbnail, views):
    return {"title":title, "thumbnail":thumbnail, "views":views}

if __name__ == '__main__':
    # json = (toJson("test", "img.com", 4))
    getViews("https://www.youtube.com/watch?v=_nf0CEiXhv4")
    # firebase.pushJson(json)
    # query = input("Enter a search query:\n > ")
    # urls = scrape(paramToUrl(query))
    # print(urls)
    # print([getThumbnailUrl(url) for url in urls])
    # getTitle("https://www.youtube.com/watch?v=eWF8jiOB9Lo")