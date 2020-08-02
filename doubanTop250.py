import requests
from pyquery import PyQuery as pq

baseUrl = "https://movie.douban.com/top250"

reqParams = {"header": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
}}

doubanList = []


def get_douban_html():
    return requests.get(baseUrl, headers=reqParams["header"])

def parseHtm():
    doubanHtml = get_douban_html().text
    dHtml = pq(doubanHtml)
    dHtml.attr( class_='grid_view')
    childrenList = dHtml.children().items('.hd')
    for index, cl in enumerate(childrenList):
          for ccIndex, ccl in enumerate(cl.find('a').children().items()):
            if ccIndex == 0:
                doubanList.append({"No":index+1,"cName":ccl.text()})


if __name__ == '__main__':
    parseHtm()
    print(doubanList)
