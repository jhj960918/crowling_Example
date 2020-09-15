from django.shortcuts import render, redirect,get_object_or_404
from .models import musinsaData


# from django.contrib.auth.models import User
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,urlretrieve
from urllib.parse import quote_plus

# Create your views here.
def musinsa_Data(searchtitle,detail_url,musinsa_path,musinsa_image_name):
    musin = musinsaData()
    musin.search_musinsa =searchtitle
    musin.musinsaUrl = detail_url
    image_url = 'images/'+musinsa_image_name
    musin.musinsaImage = image_url
    musin.save()
    

def crowling(request):
    if request.method =='POST':
        search_Image = request.POST['search']
        baseUrl = 'https://store.musinsa.com/app/product/search?search_type=1&q='
        counting_search =2
        plusUrl = search_Image 
        crawl_num = counting_search
        
        url = baseUrl + quote_plus(plusUrl) # 한글 검색 자동 변환
        html = urlopen(url)
        soup = bs(html, "html.parser")
        img = soup.find_all(class_='lazyload lazy')
        # print(img)
        n = 1
        urlist=[]
        for i in img:
            imgUrl = i['data-original']
            urllist = imgUrl.split('/')
            musinsa_image_name =str(urllist[6]) +'.jpg'#이미지 이름
            urlretrieve("http:"+imgUrl,'media/images/' + musinsa_image_name)
            searchtitle = search_Image+str(n)#검색어 
            detail_url =  "https://store.musinsa.com/app/product/detail/"+urllist[6]
            musinsa_path = 'media/images/' #이미지 저장할 경로
   
            musinsa_Data(searchtitle,detail_url,musinsa_path,musinsa_image_name)
            
            n += 1
            if n > crawl_num:
                break
        
            
    return render(request, 'app/crowling.html')

