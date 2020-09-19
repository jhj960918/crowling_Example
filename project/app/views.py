from django.shortcuts import render, redirect,get_object_or_404
from .models import musinsaData
from .models import CustomUser#유저
from django.contrib.auth import login, authenticate
from django.contrib import auth
from .forms import UserForm
# from django.contrib.auth.models import User
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,urlretrieve
from urllib.parse import quote_plus

# Create your views here.
def musinsa_Data(searchtitle,detail_url,musinsa_path,musinsa_image_name,M_title,M_price,product_dir):
    musin = musinsaData()
    musin.search_musinsa =searchtitle
    musin.musinsaUrl = detail_url
    image_url = 'images/'+product_dir+musinsa_image_name
    musin.musinsaImage = image_url
    musin.musinName = M_title
    musin.musinPrice = M_price
    musin.save()
    

def crowling(request):
    if request.method =='POST':
        search_Image = request.POST['search']
        product_dir = str(search_Image+'/')
        print(product_dir)
        baseUrl = 'https://store.musinsa.com/app/product/search?search_type=1&q='
        counting_search =2
        plusUrl = search_Image
        crawl_num = counting_search
        
        url = baseUrl + quote_plus(plusUrl) # 한글 검색 자동 변환
        html = urlopen(url)

        soup = bs(html, "html.parser")
        print(type(html))
        
        img = soup.find_all(class_='lazyload lazy')
        title = soup.find_all(class_='list_info')
        price = soup.find_all(class_='price')
        
        # print(img)
        n = 1
        urlist=[]
        for i,t,p in zip(img,title,price):#이미지 , 상품 이름 , 상품 가격  변수
            
            
            #상품 가격 가져오는 구문 :  문자열 html 코드 가격이외에 자르는 처리 코드
            pp = str(p).replace(',','')
            tmp = []
            ttt = False
            for char in pp:
                if char.isdigit():
                    if not ttt:
                        ttt = True
                        ts = char
                    else:
                        ts+=char
                elif ttt:
                    tmp.append(ts)
                    ttt = False
          
            if len(tmp) >1:
                M_price = str(tmp[0]+"원 --> "+tmp[1]+"원")
            else:
                M_price =str(tmp[0]+"원")
                
        
            a=t.select_one("p > a")#상품명 html태그에 title속성 가져오기
            M_title = a['title']#상품명 출력
            
            imgUrl = i['data-original']#이미지 속성 data-original
            urllist = imgUrl.split('/')
            musinsa_image_name =str(urllist[6]) +'.jpg'#이미지 이름
            urlretrieve("http:"+imgUrl,'media/images/'+product_dir + musinsa_image_name)
            searchtitle = search_Image+str(n)#검색어 
            detail_url =  "https://store.musinsa.com/app/product/detail/"+urllist[6]
            musinsa_path = 'media/images/' #이미지 저장할 경로
            musinsa_Data(searchtitle,detail_url,musinsa_path,musinsa_image_name,M_title,M_price,product_dir)
            
            
            n += 1
            if n > crawl_num:
                break
    


    musinsa = musinsaData.objects.all()
    return render(request, 'app/crowling.html',{'musinsa': musinsa } )
            



def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('crowling')
        else:
            return render(request, 'app/signin.html')
    else:
        return render(request, 'app/signin.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            name = form.cleaned_data['name'],
            address = form.cleaned_data['address'],
            phone_number = form.cleaned_data['phone_number'],
            gender = form.cleaned_data['gender'])
            login(request, new_user)
            return redirect('crowling')
    else:
        form = UserForm()
        return render(request, 'app/signup.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('crowling')