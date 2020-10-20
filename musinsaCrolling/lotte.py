from urllib.request import urlopen,urlretrieve

from urllib.parse import quote_plus #아스키 코드로 변환해준다

from bs4 import BeautifulSoup

from selenium import webdriver #selenium 크롤링 크롬드라이버 

import time

#urllib.request.urlretrieve( "http:"+reallink[i],"./lotte이미지/"+ "("+str(n)+")"+".jpg") 저장경로
# https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q= 롯데 url
 

#해당 페이지를 크롤링 i가 페이지번호

#해당 페이지를 크롤링 i가 페이지번호

def lotteproduct():
    reallink1 = []#이미지 저장소
    reallink2 = []#제목 저장소
    reallink3 = []#가격 저장소
    reallink4 = []#구매 페이지 저장소

    baseUrl = 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q='

    baseUrl1 = '&page='
    plusUrl = "여성 아우터"
    url = baseUrl + quote_plus(plusUrl) + baseUrl1 + str(1)

    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(3)  # 위에서 불러오고 1초 기다린후에 분석을 시작

 

    pageString = driver.page_source

    soup = BeautifulSoup(pageString, features="html.parser")

 

    LotteProductList = soup.find(name = 'ul', attrs ={'class':'srchProductList'}) #롯데 상품리스트
    
    Lotteimageurl = LotteProductList.find_all("div", class_ = "srchThumbImageWrap") #이미지 URL
   
    print(str(Lotteimageurl))
    Lottebuyurl = LotteProductList.find_all("a",class_="srchGridProductUnitLink srchNoProductOrderInfo")
    # print(Lottebuyurl)
    Lottetitle = LotteProductList.find_all("div",class_="srchProductUnitTitle")
    # print(Lottetitle)
    Lotteprice = LotteProductList.find_all("div", class_="srchProductUnitPriceArea")
    # print(Lotteprice)
    # print("두번째"+str(Lottetitle))
    # print("두번째"+str(Lotteprice))
    n=1
    for i,b,t,p in zip(Lotteimageurl,Lottebuyurl,Lottetitle,Lotteprice):
    # for i in Lotteimageurl:
        try:
            print(str(n)+"번째")
            n=n+1
            image = i.select_one("img")
            image2 = image.attrs['src']
            print("이미지"+str(image2))
            reallink1.append(image2)
           
            buyurl = b.attrs['href']
            print("구매링크"+str(buyurl))
            reallink2.append(buyurl)

            Lottetitle = t.get_text()
            print("상품 이름"+str(Lottetitle))
            reallink3.append(Lottetitle)

            Lotteprice = p.select_one("span.srchCurrentPrice").get_text()
            print("가격"+str(Lotteprice))
            reallink4.append(Lotteprice)
            print()
           
        except:
            continue

 

    

    driver.close()
lotteproduct()
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
 

 

# plusUrl = "여성 아우터"

# reallink1 = []#이미지 저장소
# reallink2 = []#제목 저장소
# reallink3 = []#가격 저장소
# reallink4 = []#구매 페이지 저장소

# baseUrl = 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q='

# baseUrl1 = '&page=1'

# url = baseUrl + quote_plus(plusUrl) + baseUrl1

# driver = webdriver.Chrome()

# driver.get(url)

# time.sleep(3) #위에서 불러오고 3초 기다린후에 분석을 시작

# pageString = driver.page_source

# soup = BeautifulSoup(pageString, features="html.parser")

# # pageNum = int((soup.find("span",{"class" : "totalPagingNum"})).text) #페이지 수라 상관없음

# # print(pageNum)

# driver.close()

# for i in range(1,2):

#     lotteproduct(i)


# # print('title = ' + title)

# n=1
# print(len(reallink1))
# for i in range(0,len(reallink1)):
    
#     urlretrieve(reallink1[i],"./lotte이미지"+ "("+str(n)+")"+".jpg")
#     n+=1

   