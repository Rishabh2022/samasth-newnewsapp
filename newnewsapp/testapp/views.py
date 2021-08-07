from django.shortcuts import render,redirect
from django.contrib.auth .decorators import login_required
from django.contrib.auth import logout
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from testapp.models import signup,Bookmark
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from newsapi.newsapi_client import NewsApiClient
from django.contrib import messages
from django.urls import reverse
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.http import JsonResponse


# Create your views here.s


def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        if request.method=='POST':
            user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                print(user)
                # a={"un":username}
                return redirect('/home/')
    return render( request,'registration/login.html/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/home/")
    
def usersignup(request):
    if(request.method=='POST'):
        firstname=request.POST['names']
        username=request.POST['username']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password=request.POST['password']
        sign=signup.objects.create_user(name=firstname,username=username,mobile=mobile,email=email,password=password)
        # myuser=User.objects.create_user(username,password)
        # myuser.save()
        sign.save()
        return HttpResponseRedirect("/accounts/login/")
    return render(request,'testapp/signin.html')

#*******************************************************************************home*************************************************************
#*******************************************************************************home*************************************************************
#*******************************************************************************home*************************************************************
#*******************************************************************************home*************************************************************
#*******************************************************************************home*************************************************************
#*******************************************************************************home*************************************************************
#*******************************************************************************home*************************************************************


def home(request):
    return render(request,"testapp/spin.html")


def process(request):
    newsapi = NewsApiClient(api_key='bb456701776c49a383d06ff36aceb6c8')
    # bb456701776c49a383d06ff36aceb6c8    680381b7da6f46a8833923dbc433f2c8    cfb1e8488b584a83ad88fd6cff03f7b3  2e3ac8ae932e4e7c805bf8f5fc8132af
    top= newsapi.get_top_headlines(country="in")
    top_business=newsapi.get_top_headlines(country="in",category="business")
    election=newsapi.get_everything(q='politics',sort_by='publishedAt')
    climate=newsapi.get_everything(q='climate',sort_by='publishedAt')
    corona=newsapi.get_everything(q='Covid19',sort_by='publishedAt')
    jobs=newsapi.get_everything(q='Jobs',sort_by='publishedAt')
    inflation=newsapi.get_everything(q='prices',sort_by='publishedAt')
    latest= newsapi.get_top_headlines()
    # videos
    opt=Options()
    opt.headless=True
    browser=webdriver.Chrome("C:/Users/DELL/chromedriver.exe",chrome_options=opt)
    browser.get("https://www.youtube.com/channel/UCIvaYmXn910QMdemBG3v1pQ")
    anchor=[]
    videos=browser.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    for video in videos:
        a=video.find_elements_by_xpath('.//*[@id="video-title"]')
        anchor.append(a)
    homehref=[]
    hometitle=[]
    for j in anchor:
        h=j[0].get_attribute('href')
        t=j[0].get_attribute('title')
        k='https://www.youtube.com/'+'embed/'+h[32:]
        homehref.append(k)
        hometitle.append(t)
    homevod=list(zip(homehref,hometitle))
    # election list
    elec=election['articles']
    ed=[]
    ei=[]
    et=[]
    er=[]
    electionlist=[]
    for i in range(len(elec)):
        ed.append(elec[i]['description'])
        et.append(elec[i]['title'])
        ei.append(elec[i]['urlToImage'])
        er.append(elec[i]['url'])
    electionlist=list(zip(et,ed,ei,er))
    #climate
    cli=climate['articles']
    cd=[]
    ci=[]
    ct=[]
    cr=[]
    climatelist=[]
    for i in range(len(cli)):
        cd.append(cli[i]['description'])
        ct.append(cli[i]['title'])
        ci.append(cli[i]['urlToImage'])
        cr.append(cli[i]['url'])
    climatelist=list(zip(ct,cd,ci,cr))
    #corona
    cor=corona['articles']
    cood=[]
    cooi=[]
    coot=[]
    coor=[]
    coronalist=[]
    for i in range(len(cor)):
        cood.append(cor[i]['description'])
        coot.append(cor[i]['title'])
        cooi.append(cor[i]['urlToImage'])
        coor.append(cor[i]['url'])
    coronalist=list(zip(coot,cood,cooi,coor))
    #jobs
    jbs=jobs['articles']
    jd=[]
    ji=[]
    jt=[]
    jr=[]
    joblist=[]
    for i in range(len(jbs)):
        jd.append(jbs[i]['description'])
        jt.append(jbs[i]['title'])
        ji.append(jbs[i]['urlToImage'])
        jr.append(jbs[i]['url'])
    joblist=list(zip(jt,jd,ji,jr))
    #inflation
    inf=inflation['articles']
    infd=[]
    infi=[]
    inft=[]
    infr=[]
    inflationlist=[]
    for i in range(len(inf)):
        infd.append(inf[i]['description'])
        inft.append(inf[i]['title'])
        infi.append(inf[i]['urlToImage'])
        infr.append(inf[i]['url'])
    inflationlist=list(zip(inft,infd,infi,infr))
    #latest
    lat=latest['articles']
    ld=[]
    li=[]
    lt=[]
    lr=[]
    latestlist=[]
    for i in range(len(lat)):
        ld.append(lat[i]['description'])
        lt.append(lat[i]['title'])
        li.append(lat[i]['urlToImage'])
        lr.append(lat[i]['url'])
    latestlist=list(zip(lt,ld,li,lr))
    json=top['articles']
    desc=[]
    img=[]
    title=[]
    mylist=[]
    readmore=[]
    for i in range(len(json)):
        desc.append(json[i]['description'])
        title.append(json[i]['title'])
        img.append(json[i]['urlToImage'])
        readmore.append(json[i]['url'])
    mylist=list(zip(title,desc,img,readmore))
    json1 = top_business['articles']
    desc1 = []
    img1 = []
    title1 = []
    mylist1 = []
    readmore1 = []
    for i in range(len(json1)):
        desc1.append(json1[i]['description'])
        title1.append(json1[i]['title'])
        img1.append(json1[i]['urlToImage'])
        readmore1.append(json1[i]['url'])
    mylist1 = list(zip(title1, desc1, img1, readmore1))
    top_sports = newsapi.get_top_headlines(country="in", category="sports")
    json2 = top_sports['articles']
    desc2 = []
    img2 = []
    title2 = []
    mylist2 = []
    readmore2 = []
    for i in range(len(json2)):
        desc2.append(json2[i]['description'])
        title2.append(json2[i]['title'])
        img2.append(json2[i]['urlToImage'])
        readmore2.append(json2[i]['url'])
    mylist2 = list(zip(title2, desc2, img2, readmore2))
    top_entertainment = newsapi.get_top_headlines(country="in", category="entertainment")
    json3 = top_entertainment['articles']
    desc3 = []
    img3 = []
    title3 = []
    mylist3 = []
    readmore3 = []
    for i in range(len(json3)):
        desc3.append(json3[i]['description'])
        title3.append(json3[i]['title'])
        img3.append(json3[i]['urlToImage'])
        readmore3.append(json3[i]['url'])
    mylist3 = list(zip(title3, desc3, img3, readmore3))
    top_health = newsapi.get_top_headlines(country="in", category="health")
    json4 = top_health['articles']
    desc4 = []
    img4 = []
    title4 = []
    mylist4 = []
    readmore4 = []
    for i in range(len(json4)):
        desc4.append(json4[i]['description'])
        title4.append(json4[i]['title'])
        img4.append(json4[i]['urlToImage'])
        readmore4.append(json4[i]['url'])
    mylist4 = list(zip(title4, desc4, img4, readmore4))
    top_science = newsapi.get_top_headlines(country="in", category="science")
    json5 = top_science['articles']
    desc5 = []
    img5 = []
    title5 = []
    mylist5 = []
    readmore5 = []
    for i in range(len(json5)):
        desc5.append(json5[i]['description'])
        title5.append(json5[i]['title'])
        img5.append(json5[i]['urlToImage'])
        readmore5.append(json5[i]['url'])
    mylist5 = list(zip(title5, desc5, img5, readmore5))

    top_technology = newsapi.get_top_headlines(country="in", category="technology")
    json6 = top_technology['articles']
    desc6 = []
    img6 = []
    title6 = []
    mylist6 = []
    readmore6 = []
    for i in range(len(json6)):
        desc6.append(json6[i]['description'])
        title6.append(json6[i]['title'])
        img6.append(json6[i]['urlToImage'])
        readmore6.append(json6[i]['url'])
    mylist6 = list(zip(title6, desc6, img6, readmore6))

    intr= newsapi.get_everything(sort_by='publishedAt',q="international")
    json7= intr['articles']
    desc7 = []
    img7 = []
    title7 = []
    mylist7 = []
    readmore7 = []
    for i in range(len(json7)):
        desc7.append(json7[i]['description'])
        title7.append(json7[i]['title'])
        img7.append(json7[i]['urlToImage'])
        readmore7.append(json7[i]['url'])
    mylist7= list(zip(title7, desc7, img7, readmore7))
    

    context={'row':mylist[4:],'row1':mylist[:4],'business':mylist1,'sports':mylist2,'entertainment':mylist3,'health':mylist4,'science':mylist5,'technology':mylist6,"electionlist":electionlist[1:5],"climatelist":climatelist[:4],"coronalist":coronalist[:4],"joblist":joblist[:4],"inflationlist":inflationlist[:4],"latestlist":latestlist[:4],"vod":homevod[1:10],"readhere":mylist7[:8]}
    result=render_to_string("testapp/index.html",context,request=request)
    data={'data':result}
    return JsonResponse(data)
def base(request):
    return render(request,"testapp/base.html")


#*****************************************************************************business*************************************************************
#*****************************************************************************business*************************************************************
#*****************************************************************************business*************************************************************
#*****************************************************************************business*************************************************************
#*****************************************************************************business*************************************************************
#*****************************************************************************business*************************************************************
#*****************************************************************************business*************************************************************

@login_required
def business(request):
    newsapi = NewsApiClient(api_key='680381b7da6f46a8833923dbc433f2c8')
    businessheadline=newsapi.get_top_headlines(category='business',country='in')
    business=businessheadline['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
   
    for i in range(len(business)):
        desc.append(business[i]['description'])
        title.append(business[i]['title'])
        img.append(business[i]["urlToImage"])
        readmore.append(business[i]['url'])
    indbusiness=list(zip(title,desc,img,readmore))

    international=newsapi.get_top_headlines(category='business',country='us')
    business=international['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(business)):
        desc.append(business[i]['description'])
        title.append(business[i]['title'])
        img.append(business[i]["urlToImage"])
        readmore.append(business[i]['url'])
    international=list(zip(title,desc,img,readmore))

    related=newsapi.get_top_headlines(category='business')
    business=related['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(business)):
        desc.append(business[i]['description'])
        title.append(business[i]['title'])
        img.append(business[i]["urlToImage"])
        readmore.append(business[i]['url'])
    related=list(zip(title,desc,img,readmore))
    

    topcoperate=newsapi.get_top_headlines(category='business',q='corporate')
    business=topcoperate['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(business)):
        desc.append(business[i]['description'])
        title.append(business[i]['title'])
        img.append(business[i]["urlToImage"])
        readmore.append(business[i]['url'])
    topcoperate=list(zip(title,desc,img,readmore))

    
    economy=newsapi.get_top_headlines(category='business',q='economy')
    business=economy['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(business)):
        desc.append(business[i]['description'])
        title.append(business[i]['title'])
        img.append(business[i]["urlToImage"])
        readmore.append(business[i]['url'])
    economy=list(zip(title,desc,img,readmore))

    startup=newsapi.get_top_headlines(category='business',q='startup')
    business=startup['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(business)):
        desc.append(business[i]['description'])
        title.append(business[i]['title'])
        img.append(business[i]["urlToImage"])
        readmore.append(business[i]['url'])
    startup=list(zip(title,desc,img,readmore))


    opt=Options()
    opt.headless=True
    browser=webdriver.Chrome("C:/Users/DELL/chromedriver.exe",chrome_options=opt)
    browser.get("https://www.youtube.com/channel/UCYfdidRxbB8Qhf0Nx7ioOYw")
    anchor=[]
    videos=browser.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    for video in videos:
        a=video.find_elements_by_xpath('.//*[@id="video-title"]')
        anchor.append(a)
    href=[]
    title=[]
    for j in anchor:
        h=j[0].get_attribute('href')
        t=j[0].get_attribute('title')
        k='https://www.youtube.com/'+'embed/'+h[32:]
        href.append(k)
        title.append(t)
    vod=list(zip(href,title))
    
    return render(request,'testapp/business.html',{'mylist':indbusiness[:2],"international":international,"related":related,"startup":startup[:3],"economy":economy[:3],"coporate":topcoperate[:3],"category":indbusiness[1:5],"yt":vod[:4]})



#*******************************************************************************entertainment*****************************************************
#*******************************************************************************entertainment*****************************************************
#*******************************************************************************entertainment*****************************************************
#*******************************************************************************entertainment*****************************************************
#*******************************************************************************entertainment*****************************************************




@login_required
def Entertainment(request):
    newsapi = NewsApiClient(api_key='bb456701776c49a383d06ff36aceb6c8')
    entertainmentheaadlines=newsapi.get_top_headlines(category='entertainment',country='in')
    enter=entertainmentheaadlines['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(enter)):
        desc.append(enter[i]['description'])
        title.append(enter[i]['title'])
        img.append(enter[i]["urlToImage"])
        readmore.append(enter[i]['url'])
    front=list(zip(title,desc,img,readmore))

    international=newsapi.get_top_headlines(category='entertainment',country='us')
    interenter=international['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(interenter)):
        desc.append(interenter[i]['description'])
        title.append(interenter[i]['title'])
        img.append(interenter[i]["urlToImage"])
        readmore.append(interenter[i]['url'])
    international=list(zip(title,desc,img,readmore))

    related=newsapi.get_top_headlines(category="entertainment")
    enterrel=related['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(enterrel)):
        desc.append(enterrel[i]['description'])
        title.append(enterrel[i]['title'])
        img.append(enterrel[i]["urlToImage"])
        readmore.append(enterrel[i]['url'])
    related=list(zip(title,desc,img,readmore))
    

    bollywood=newsapi.get_top_headlines(category='entertainment',q='bollywood')
    bolywoodenter=bollywood['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(bolywoodenter)):
        desc.append(bolywoodenter[i]['description'])
        title.append(bolywoodenter[i]['title'])
        img.append(bolywoodenter[i]["urlToImage"])
        readmore.append(bolywoodenter[i]['url'])
    enterbolywood=list(zip(title,desc,img,readmore))
    print(enterbolywood)

    
    hollywood=newsapi.get_top_headlines(category='entertainment',q='hollywood')
    holyenter=hollywood['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(holyenter)):
        desc.append(holyenter[i]['description'])
        title.append(holyenter[i]['title'])
        img.append(holyenter[i]["urlToImage"])
        readmore.append(holyenter[i]['url'])
    enterholly=list(zip(title,desc,img,readmore))

    film=newsapi.get_top_headlines(category='entertainment',q='film')
    filmes=film['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(filmes)):
        desc.append(filmes[i]['description'])
        title.append(filmes[i]['title'])
        img.append(filmes[i]["urlToImage"])
        readmore.append(filmes[i]['url'])
    enterfilm=list(zip(title,desc,img,readmore))


    opt=Options()
    opt.headless=True
    browser=webdriver.Chrome("C:/Users/DELL/chromedriver.exe",chrome_options=opt)
    browser.get("https://www.youtube.com/channel/UCiiEf9oJvxfMfyJisqyD3BA/featured")
    anchor=[]
    videos=browser.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    for video in videos:
        a=video.find_elements_by_xpath('.//*[@id="video-title"]')
        anchor.append(a)
    href=[]
    title=[]
    for j in anchor:
        h=j[0].get_attribute('href')
        t=j[0].get_attribute('title')
        k='https://www.youtube.com/'+'embed/'+h[32:]
        href.append(k)
        title.append(t)
    vod=list(zip(href,title))
    
    return render(request,'testapp/entertainment.html',{'mylist':front[:2],"international":international,"related":related[3:],"bolywood":enterbolywood[:3],"hollywood":enterholly[:3],"film":enterfilm[:3],"category":front[3:7],"yt":vod[:4]})


#*******************************************************************************Sports*****************************************************
#*******************************************************************************Sports*****************************************************
#*******************************************************************************Sports*****************************************************
#*******************************************************************************Sports*****************************************************
#*******************************************************************************Sports*****************************************************

def Sports(request):
    newsapi = NewsApiClient(api_key='bb456701776c49a383d06ff36aceb6c8')
    sportsheadline=newsapi.get_top_headlines(category='sports',country='in')
    sports=sportsheadline['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    for i in range(len(sports)):
        desc.append(sports[i]['description'])
        title.append(sports[i]['title'])
        img.append(sports[i]["urlToImage"])
        readmore.append(sports[i]['url'])
    sportstop=list(zip(title,desc,img,readmore))

    international=newsapi.get_top_headlines(category='sports',country='us')
    sports=international['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    for i in range(len(sports)):
        desc.append(sports[i]['description'])
        title.append(sports[i]['title'])
        img.append(sports[i]["urlToImage"])
        readmore.append(sports[i]['url'])
    international=list(zip(title,desc,img,readmore))

    related=newsapi.get_top_headlines(category='sports')
    sports=related['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(sports)):
        desc.append(sports[i]['description'])
        title.append(sports[i]['title'])
        img.append(sports[i]["urlToImage"])
        readmore.append(sports[i]['url'])
    related=list(zip(title,desc,img,readmore))
    

    cricket=newsapi.get_top_headlines(category='sports',q='cricket')
    sports=cricket['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(sports)):
        desc.append(sports[i]['description'])
        title.append(sports[i]['title'])
        img.append(sports[i]["urlToImage"])
        readmore.append(sports[i]['url'])
    cricketnews=list(zip(title,desc,img,readmore))

    
    hockey=newsapi.get_top_headlines(category='sports',q='hockey')
    sports=hockey['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(sports)):
        desc.append(sports[i]['description'])
        title.append(sports[i]['title'])
        img.append(sports[i]["urlToImage"])
        readmore.append(sports[i]['url'])
    hokeynews=list(zip(title,desc,img,readmore))

    tournament=newsapi.get_top_headlines(category='sports',q='tournament')
    sports=tournament['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(sports)):
        desc.append(sports[i]['description'])
        title.append(sports[i]['title'])
        img.append(sports[i]["urlToImage"])
        readmore.append(sports[i]['url'])
    tournament=list(zip(title,desc,img,readmore))


    opt=Options()
    opt.headless=True
    browser=webdriver.Chrome("C:/Users/DELL/chromedriver.exe",chrome_options=opt)
    browser.get("https://www.youtube.com/channel/UCEl0qh9X3kuL1RdFHng497Q")
    anchor=[]
    videos=browser.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    for video in videos:
        a=video.find_elements_by_xpath('.//*[@id="video-title"]')
        anchor.append(a)
    href=[]
    title=[]
    for j in anchor:
        h=j[0].get_attribute('href')
        t=j[0].get_attribute('title')
        k='https://www.youtube.com/'+'embed/'+h[32:]
        href.append(k)
        title.append(t)
    vod=list(zip(href,title))
    
    return render(request,'testapp/sports.html',{'mylist':sportstop[:2],"international":international,"related":related,"cricket":cricketnews[:3],"hockey":hokeynews[:3],"tournament":tournament[:3],"category":sportstop[1:5],"yt":vod[:4]})



#*******************************************************************************Health*************************************************************
#*******************************************************************************Health*************************************************************
#*******************************************************************************Health*************************************************************
#*******************************************************************************Health*************************************************************
#*******************************************************************************Health*************************************************************
#*******************************************************************************Health*************************************************************
#*******************************************************************************Health*************************************************************
@login_required
def Health(request):
    newsapi = NewsApiClient(api_key='680381b7da6f46a8833923dbc433f2c8')
    healthheadline=newsapi.get_top_headlines(category='health',country='in')
    health=healthheadline['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
   
    for i in range(len(health)):
        desc.append(health[i]['description'])
        title.append(health[i]['title'])
        img.append(health[i]["urlToImage"])
        readmore.append(health[i]['url'])
    indhealth=list(zip(title,desc,img,readmore))

    international=newsapi.get_top_headlines(category='health',country='us')
    health=international['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(health)):
        desc.append(health[i]['description'])
        title.append(health[i]['title'])
        img.append(health[i]["urlToImage"])
        readmore.append(health[i]['url'])
    international=list(zip(title,desc,img,readmore))

    related=newsapi.get_top_headlines(category='health')
    health=related['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(health)):
        desc.append(health[i]['description'])
        title.append(health[i]['title'])
        img.append(health[i]["urlToImage"])
        readmore.append(health[i]['url'])
    related=list(zip(title,desc,img,readmore))
    

    heartnews=newsapi.get_top_headlines(category='health',q='heart')
    health=heartnews['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(health)):
        desc.append(health[i]['description'])
        title.append(health[i]['title'])
        img.append(health[i]["urlToImage"])
        readmore.append(health[i]['url'])
    heart=list(zip(title,desc,img,readmore))

    
    cancernews=newsapi.get_top_headlines(category='health',q='cancer')
    health=cancernews['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(health)):
        desc.append(health[i]['description'])
        title.append(health[i]['title'])
        img.append(health[i]["urlToImage"])
        readmore.append(health[i]['url'])
    cancer=list(zip(title,desc,img,readmore))

    diabetesnews=newsapi.get_top_headlines(category='health',q='diabetes')
    health=diabetesnews['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(health)):
        desc.append(health[i]['description'])
        title.append(health[i]['title'])
        img.append(health[i]["urlToImage"])
        readmore.append(health[i]['url'])
    diabetes=list(zip(title,desc,img,readmore))


    opt=Options()
    opt.headless=True
    browser=webdriver.Chrome("C:/Users/DELL/chromedriver.exe",chrome_options=opt)
    browser.get("https://www.youtube.com/channel/UC6ixzODPAdgVdY9aoSlPPew")
    anchor=[]
    videos=browser.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    for video in videos:
        a=video.find_elements_by_xpath('.//*[@id="video-title"]')
        anchor.append(a)
    href=[]
    title=[]
    for j in anchor:
        h=j[0].get_attribute('href')
        t=j[0].get_attribute('title')
        k='https://www.youtube.com/'+'embed/'+h[32:]
        href.append(k)
        title.append(t)
    vod=list(zip(href,title))
    
    return render(request,'testapp/health.html',{'mylist':indhealth[:2],"international":international,"related":related,"diabetes":diabetes[:3],"heart":heart[:3],"cancer":cancer[:3],"category":indhealth[1:5],"yt":vod[:4]})


#**************************************************************************Technology*************************************************************
#**************************************************************************Technology*************************************************************
#**************************************************************************Technology*************************************************************
#**************************************************************************Technology*************************************************************
#**************************************************************************Technology*************************************************************
#**************************************************************************Technology*************************************************************
#**************************************************************************Technology*************************************************************
#**************************************************************************Technology*************************************************************
def Technology(request):
    newsapi = NewsApiClient(api_key='680381b7da6f46a8833923dbc433f2c8')
    techheadline=newsapi.get_top_headlines(category='business',country='in')
    technology=techheadline['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
   
    for i in range(len(technology)):
        desc.append(technology[i]['description'])
        title.append(technology[i]['title'])
        img.append(technology[i]["urlToImage"])
        readmore.append(technology[i]['url'])
    indtechnology=list(zip(title,desc,img,readmore))

    international=newsapi.get_top_headlines(category='technology',country='us')
    technology=international['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(technology)):
        desc.append(technology[i]['description'])
        title.append(technology[i]['title'])
        img.append(technology[i]["urlToImage"])
        readmore.append(technology[i]['url'])
    international=list(zip(title,desc,img,readmore))

    related=newsapi.get_top_headlines(category='technology')
    technology=related['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(technology)):
        desc.append(technology[i]['description'])
        title.append(technology[i]['title'])
        img.append(technology[i]["urlToImage"])
        readmore.append(technology[i]['url'])
    related=list(zip(title,desc,img,readmore))
    

    hardwarenews=newsapi.get_top_headlines(category='technology',q='hardware')
    technology=hardwarenews['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(technology)):
        desc.append(technology[i]['description'])
        title.append(technology[i]['title'])
        img.append(technology[i]["urlToImage"])
        readmore.append(technology[i]['url'])
    hardware=list(zip(title,desc,img,readmore))

    
    softwarenews=newsapi.get_top_headlines(category='technology',q='software')
    technology=softwarenews['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(technology)):
        desc.append(technology[i]['description'])
        title.append(technology[i]['title'])
        img.append(technology[i]["urlToImage"])
        readmore.append(technology[i]['url'])
    software=list(zip(title,desc,img,readmore))

    it=newsapi.get_top_headlines(category='technology',q='it')
    technology=it['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(technology)):
        desc.append(technology[i]['description'])
        title.append(technology[i]['title'])
        img.append(technology[i]["urlToImage"])
        readmore.append(technology[i]['url'])
    info=list(zip(title,desc,img,readmore))


    opt=Options()
    opt.headless=True
    browser=webdriver.Chrome("C:/Users/DELL/chromedriver.exe",chrome_options=opt)
    browser.get("https://www.youtube.com/channel/UClnA6kw0Qb_Cn-ersL7xg7A")
    anchor=[]
    videos=browser.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    for video in videos:
        a=video.find_elements_by_xpath('.//*[@id="video-title"]')
        anchor.append(a)
    href=[]
    title=[]
    for j in anchor:
        h=j[0].get_attribute('href')
        t=j[0].get_attribute('title')
        k='https://www.youtube.com/'+'embed/'+h[32:]
        href.append(k)
        title.append(t)
    vod=list(zip(href,title))
    
    return render(request,'testapp/technology.html',{'mylist':indtechnology[:2],"international":international,"related":related,"info":info[:3],"hardware":hardware[:3],"software":software[:3],"category":indtechnology[1:5],"yt":vod[:4]})

#************************************************************************Science******************************************************************
#************************************************************************Science******************************************************************
#************************************************************************Science******************************************************************
#************************************************************************Science******************************************************************
#************************************************************************Science******************************************************************
#************************************************************************Science******************************************************************
#************************************************************************Science******************************************************************
def Science(request):
    newsapi = NewsApiClient(api_key='680381b7da6f46a8833923dbc433f2c8')
    scienceheadline=newsapi.get_top_headlines(category='science',country='in')
    science=scienceheadline['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
   
    for i in range(len(science)):
        desc.append(science[i]['description'])
        title.append(science[i]['title'])
        img.append(science[i]["urlToImage"])
        readmore.append(science[i]['url'])
    indscience=list(zip(title,desc,img,readmore))

    international=newsapi.get_top_headlines(category='science',country='us')
    science=international['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(science)):
        desc.append(science[i]['description'])
        title.append(science[i]['title'])
        img.append(science[i]["urlToImage"])
        readmore.append(science[i]['url'])
    international=list(zip(title,desc,img,readmore))

    related=newsapi.get_top_headlines(category='science')
    science=related['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(science)):
        desc.append(science[i]['description'])
        title.append(science[i]['title'])
        img.append(science[i]["urlToImage"])
        readmore.append(science[i]['url'])
    related=list(zip(title,desc,img,readmore))
    

    spacenews=newsapi.get_top_headlines(category='science',q='space')
    science=spacenews['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(science)):
        desc.append(science[i]['description'])
        title.append(science[i]['title'])
        img.append(science[i]["urlToImage"])
        readmore.append(science[i]['url'])
    space=list(zip(title,desc,img,readmore))

    
    earthnews=newsapi.get_top_headlines(category='science',q='earth')
    science=earthnews['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(science)):
        desc.append(science[i]['description'])
        title.append(science[i]['title'])
        img.append(science[i]["urlToImage"])
        readmore.append(science[i]['url'])
    earth=list(zip(title,desc,img,readmore))

    humansnews=newsapi.get_top_headlines(category='science',q='humans')
    science=humansnews['articles']
    desc=[]
    img=[]
    title=[]
    readmore=[]
    videos=[]
    for i in range(len(science)):
        desc.append(science[i]['description'])
        title.append(science[i]['title'])
        img.append(science[i]["urlToImage"])
        readmore.append(science[i]['url'])
    humans=list(zip(title,desc,img,readmore))


    opt=Options()
    opt.headless=True
    browser=webdriver.Chrome("C:/Users/DELL/chromedriver.exe",chrome_options=opt)
    browser.get("https://www.youtube.com/channel/UCZYTClx2T1of7BRZ86-8fow/videos")
    anchor=[]
    videos=browser.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    for video in videos:
        a=video.find_elements_by_xpath('.//*[@id="video-title"]')
        anchor.append(a)
    href=[]
    title=[]
    for j in anchor:
        h=j[0].get_attribute('href')
        t=j[0].get_attribute('title')
        k='https://www.youtube.com/'+'embed/'+h[32:]
        href.append(k)
        title.append(t)
    vod=list(zip(href,title))
    return render(request,'testapp/science.html',{'mylist':indscience[:2],"international":international,"related":related,"humans":humans[:3],"earth":earth[:3],"space":space[:3],"category":indscience[1:5],"yt":vod[:4]})



#********************************************************save bookmark******************************************************************
#***********************************************************save bookmark******************************************************************
#******************************************************************save bookmark******************************************************************
#*********************************************************save bookmark******************************************************************
#***************************************************************save bookmark******************************************************************
#**********************************************************save bookmark******************************************************************
#***************************************************************save bookmark******************************************************************

def SaveBookmark(request):
    if request.method=="POST":
        img=request.POST["image"]
        title=request.POST["title"]
        readmore=request.POST["readmore"]
        print(readmore)
        user=request.user.username
        bmrk=Bookmark(title=title,image=img,readmore=readmore,user_id=user)
        bmrk.save()
        messages.success(request, "Your bookmark has been added successfully") 
        return redirect('/home/')



#****************************************************************delete bookmark******************************************************************
#****************************************************************delete bookmark*********************************************************
#****************************************************************delete bookmark******************************************************************

def deletebookmark(request):
    if request.method=="POST":
        no=request.POST["sno"]
        Bookmark.objects.filter(sno=no).delete()
        messages.success(request, "Your bookmark has been deleted successfully") 
        user_bookmark = Bookmark.objects.filter(user_id=request.user.username)
        return render(request,"testapp/Display.html",{"user_bookmark":user_bookmark})

#************************************************************display bookmark******************************************************************
#************************************************************display bookmark******************************************************************
#************************************************************display bookmark******************************************************************
#************************************************************display bookmark******************************************************************
#************************************************************display bookmark******************************************************************
#************************************************************display bookmark******************************************************************
#**************************************** *******************display bookmark******************************************************************

def display(request):
    user_bookmark = Bookmark.objects.filter(user_id=request.user.username)
    return render(request,"testapp/Display.html",{"user_bookmark":user_bookmark})

#*    *******************************************************MY FEED******************************************************************
#************************************************************MY FEED******************************************************************
#************************************************************MY FEED******************************************************************
#************************************************************MY FEED******************************************************************

def myfeed(request):
    return render(request,"testapp/MyFeed.html",{"check":""})



def myfeedreply(request):
    d={"India":"in","United States":"us","Russia":"ru","China":"cn","United Kingdom":"gb"}
    if request.method=="POST":
        country=request.POST["country"]
        category=request.POST["category"]
        newsapi = NewsApiClient(api_key='680381b7da6f46a8833923dbc433f2c8')
        top=  newsapi.get_top_headlines(country=d[country],category=category)
        json=top['articles']
        desc=[]
        img=[]
        title=[]
        mylist=[]
        readmore=[]
        for i in range(len(json)):
            desc.append(json[i]['description'])
            title.append(json[i]['title'])
            img.append(json[i]['urlToImage'])
            readmore.append(json[i]['url'])
        mylist=list(zip(title,desc,img,readmore))
        print(mylist)
        return render(request,"testapp/MyFeed.html",{"check":"Yes","myfeed":mylist})
            
