import urllib.request

from urllib.parse import quote_plus #아스키 코드로 변환해준다

from bs4 import BeautifulSoup

from selenium import webdriver

import time

 

 

#해당 페이지를 크롤링 i가 페이지번호

def musinsaCrawling(pageNum):

    baseUrl = 'https://store.musinsa.com/app/product/search?search_type=1&q='

    baseUrl1 = '&page='

    url = baseUrl + quote_plus(plusUrl) + baseUrl1 + str(pageNum)

    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(3)  # 위에서 불러오고 1초 기다린후에 분석을 시작

 

    pageString = driver.page_source

    soup = BeautifulSoup(pageString, features="html.parser")

 

    result1 = soup.find(name = 'ul', attrs ={'class':'snap-article-list boxed-article-list article-list center list goods_small_media8'})

    result2 = result1.find_all(name = "img")

 

    for i in result2:

        try:

            image = i.attrs['data-original']

            reallink.append(image)

        except:

            continue

 

    print(reallink)

    driver.close()

 

 

plusUrl = input('검색할 옷을 입력하시오: ')

reallink = []

 

 

baseUrl = 'https://store.musinsa.com/app/product/search?search_type=1&q='

baseUrl1 = '&page=1'

url = baseUrl + quote_plus(plusUrl) + baseUrl1

driver = webdriver.Chrome()

driver.get(url)

 

time.sleep(3) #위에서 불러오고 3초 기다린후에 분석을 시작

 

 

pageString = driver.page_source

soup = BeautifulSoup(pageString, features="html.parser")

pageNum = int((soup.find("span",{"class" : "totalPagingNum"})).text)

print(pageNum)

driver.close()

 

 

 

for i in range(1,pageNum+1):

    musinsaCrawling(i)

 

 

print(reallink)

 

 

if plusUrl == '스몰로고맨투맨':

    title = 'small logo sweatshir'

elif plusUrl == '빅로고맨투맨':

    title = 'big logo sweatshir'

elif plusUrl =='스트라이프맨투맨':

    title = 'stripe sweatshir'

 

 

print('title = ' + title)

n = 1

for i in range(0,len(reallink)):
    print("씨발련이좃같네")
    urllib.request.urlretrieve( "http:"+reallink[i],"./image/" +title + "("+str(n)+")"+".jpg")

    n +=1

 