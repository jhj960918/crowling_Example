from django.shortcuts import render, redirect,get_object_or_404
from .models import lotteData ,CartItem
from .models import CustomUser#유저
from django.contrib.auth import login, authenticate
from django.contrib import auth
from .forms import UserForm
# from django.contrib.auth.models import User
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,urlretrieve
from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# def lotte_Data(searchtitle,detail_url,lotte_path,lotte_image_name,M_title,M_price,product_dir):
#     lotte = lotteData()
#     lotte.search_lotte =searchtitle
#     lotte.lotteUrl = detail_url
#     image_url = 'images/'+product_dir+lotte_image_name
#     lotte.lotteImage = image_url
#     lotte.lotteName = M_title
#     lotte.lottePrice = M_price
#     lotte.save()
    

def crowling(request):
    if request.method =='POST':
        search_Image = request.POST['search']
        product_dir = str(search_Image+'/')
        
        baseUrl = 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q='
        counting_search =2
        plusUrl = search_Image
        crawl_num = counting_search
        
        url = baseUrl + quote_plus(plusUrl) # 한글 검색 자동 변환
        html = urlopen(url)

        soup = bs(html, "html.parser")
        print(soup.prettify())
        title = soup.find_all(class_='srchProductUnitTitle')
        price = soup.find_all(class_='srchOriginalPrice')
        img = ''
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
            lotte_image_name =str(urllist[6]) +'.jpg'#이미지 이름
            urlretrieve("http:"+imgUrl,'media/images/'+product_dir + lotte_image_name)
            searchtitle = search_Image+str(n)#검색어 
            detail_url =  "https://store.lotte.com/app/product/detail/"+urllist[6]
            lotte_path = 'media/images/' #이미지 저장할 경로
            
            # lotte_Data(searchtitle,detail_url,lotte_path,lotte_image_name,M_title,M_price,product_dir)
            
            
            n += 1
            if n > crawl_num:
                break
    
    lotte = lotteData.objects.all().order_by('-id')
    return render(request, 'app/crowling.html',{'lotte': lotte } )
        

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

#장바구니 
def add_cart(request, product_pk):
	# 상품을 담기 위해 해당 상품 객체를 product 변수에 할당
    product = lotteData.objects.get(pk=product_pk)

    try:
    	# 장바구니는 user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
        cart = CartItem.objects.get(product__id=product.pk, user__id=request.user.pk)
        if cart:
            if cart.product.lotteName == product.lotteName:
                cart.quantity += 1
                cart.save()
    except CartItem.DoesNotExist:
        user = CustomUser.objects.get(pk=request.user.pk)
        cart = CartItem(
            user=user,
            product=product,
            quantity=1,
        )
        cart.save()
    return redirect('my_cart')
     
def delete_cart_item(request, product_pk):
    
    cart_item = CartItem.objects.filter(product__id=product_pk)
    product = lotteData.objects.get(pk=product_pk)
    cart_item.delete()
    return redirect('my_cart')
    
    

#각 유저의 장바구니
def my_cart(request):
    
    cart_item = CartItem.objects.filter(user__id=request.user.pk)
    # 장바구니에 담긴 상품의 총 합계 가격
    # total_price = 0
    # for loop 를 순회하여 각 상품 * 수량을 total_price 에 담는다
    # for each_total in cart_item:
    #     total_price += each_total.product.price * each_total.quantity
    if cart_item is not None:
        context = {
        	# 없으면 없는대로 빈 conext 를 템플릿 변수에서 사용
            'cart_item': cart_item,
            # 'total_price': total_price,
        }
        return render(request, 'app/cart.html', {'cart_item': cart_item,})
    return redirect('my_cart')