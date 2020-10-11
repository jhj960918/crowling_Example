from urllib.request import urlopen,urlretrieve

from urllib.parse import quote_plus #아스키 코드로 변환해준다

from bs4 import BeautifulSoup

from selenium import webdriver #selenium 크롤링 크롬드라이버 

import time

#urllib.request.urlretrieve( "http:"+reallink[i],"./lotte이미지/"+ "("+str(n)+")"+".jpg") 저장경로
# https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q= 롯데 url
 

#해당 페이지를 크롤링 i가 페이지번호

#해당 페이지를 크롤링 i가 페이지번호

def Crawling(pageNum):

    baseUrl = 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q='

    baseUrl1 = '&page='

    url = baseUrl + quote_plus(plusUrl) + baseUrl1 + str(pageNum)

    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(3)  # 위에서 불러오고 1초 기다린후에 분석을 시작

 

    pageString = driver.page_source

    soup = BeautifulSoup(pageString, features="html.parser")

 

    LotteProductList = soup.find(name = 'ul', attrs ={'class':'srchProductList'}) #롯데 상품리스트
    
    Lotteimageurl = LotteProductList.find_all(name = "img") #이미지 URL
    Lottebuyurl = LotteProductList.find_all(name = "a")
    # print(Lottebuyurl)
    Lottetitle = LotteProductList.find_all("div", class_="srchProductUnitTitle")
    # print(Lottetitle)
    Lotteprice = LotteProductList.find_all("span", class_="srchCurrentPrice")
    # print(Lotteprice)
    # print("두번째"+str(Lottetitle))
    # print("두번째"+str(Lotteprice))

    for i,b,t,p in zip(Lotteimageurl,Lottebuyurl,Lottetitle,Lotteprice):
    # for i in Lotteimageurl:
        try:
            image = i.attrs['src']
            reallink1.append(image)
            # print(image)
            buyurl = b.attrs['href']
            print("구매링크"+str(buyurl))
            reallink2.append(buyurl)
            Lottetitle = t.get_text()
            print(Lottetitle)
            reallink3.append(Lottetitle)
            Lotteprice = p.get_text()
            print(Lotteprice)
            reallink4.append(Lotteprice)
           
        except:
            continue

 

    

    driver.close()
#  try:
#             image = i.attrs['src']
#             reallink1.append(image)
#             title = t.get_text()
#             print(title)
#             reallink2.append(title)
#             price= p.get_text()
#             print(price)
#             reallink2.append(price)
#         except:
#             continue
 

 

plusUrl = "여성 가방"

reallink1 = []#이미지 저장소
reallink2 = []#제목 저장소
reallink3 = []#가격 저장소
reallink4 = []#구매 페이지 저장소

baseUrl = 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q='

baseUrl1 = '&page=1'

url = baseUrl + quote_plus(plusUrl) + baseUrl1

driver = webdriver.Chrome()

driver.get(url)

time.sleep(3) #위에서 불러오고 3초 기다린후에 분석을 시작

pageString = driver.page_source

soup = BeautifulSoup(pageString, features="html.parser")

# pageNum = int((soup.find("span",{"class" : "totalPagingNum"})).text) #페이지 수라 상관없음

# print(pageNum)

driver.close()

for i in range(1,2):

    Crawling(i)


# print('title = ' + title)

n = 1
print(len(reallink1))
for i in range(0,len(reallink1)):
    
    urlretrieve(reallink1[i],"./lotte이미지/"+ "("+str(n)+")"+".jpg")

    n +=1
