# 淘宝热门分类店铺的数量统计

from selenium import webdriver
from bs4 import BeautifulSoup

URI_host = "shopsearch.taobao.com"

# 认证后的cookie字符串
cookieStr = "your auth cookie"


# 根据cookie字符串，设置cookie
def setCookie(dirver, cookie):
    cookieList = []
    cookiesrr = cookie.split('; ')
    for cookieStrItem in cookiesrr:
        cookieItem = cookieStrItem.split('=')
        cookieList.append(
            {"name": cookieItem[0], "value": cookieItem[1]}
        )
    for cookie in cookieList:
        dirver.add_cookie({
            'domain': URI_host,
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })


def getTaobaoShopAmount():
    url = 'https://' + URI_host + '/search?app=shopsearch'
    driver = webdriver.Chrome('/Users/erwin/env/dirver/chromedriver89')
    driver.get('https://shopsearch.taobao.com/')
    setCookie(driver, cookieStr)

    driver.get(url)
    driver.implicitly_wait(3)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    hotShopList = soup.find_all('a', 'level-one-cat')

    print(hotShopList[0]['href'])

    shopCount = 0

    def countShopItem(hotShopItem):
        driver.get('https://' + URI_host + hotShopItem['href'])
        driver.implicitly_wait(5)
        pageItem = driver.page_source
        soupItem = BeautifulSoup(pageItem, 'lxml')
        countParentTag = soupItem.find('span', 'shop-count')
        return int(countParentTag.b.string)

    for item in hotShopList:
        shopCount += countShopItem(item)

    print('统计的淘宝热门类目的店铺数是：' + shopCount)


getTaobaoShopAmount()
