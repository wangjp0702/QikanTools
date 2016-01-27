from selenium import webdriver
from bs4 import BeautifulSoup
import re,time,requests,json,io
import os,traceback
from PIL import Image
#driver =webdriver.PhantomJS(executable_path='D:\Python34\Scripts\phantomjs.exe')
#driver.get('http://weixin.sogou.com/weixin?query=%E9%BE%99%E6%BA%90%E7%BD%91&type=2&page=2&ie=utf8')

#driver.find_element_by_id('sogou_next').click()
#data=driver.find_element_by_class_name('results').text
#print(data)
#num=driver.find_element_by_class_name('mun').text
#print(num)
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
def getText(text):
    imgTag={"text":text}
    return imgTag

def getImg(imgurl):
    response = requests.get(imgurl)
    img = Image.open(io.BytesIO(response.content))
    if(img.format=='GIF'):
        return ''
    size=str(img.size[0])+','+str(img.size[1])
    largeSize=int(img.size[0])*int(img.size[1])
    imgTag={"image":imgurl,"size":size}
   
    return (imgTag,largeSize)

def parseContent(soup):
    list=[]
    largestImg=''
    largestSize=0
    pcount=0
    for line in soup.findAll('p'):
         pcount=pcount+1
         if(line.find('img')!=None):#len(line.find('img'))>0):
             r=getImg(line.find('img').get('src'))
             print('          ------图片：%s------'%(pcount))
             if(r!=''):
                 list.append(r[0])
                 if(largestSize>r[1]):
                     continue
                 else:
                     largestSize=r[1]
                     largestImg=line.find('img').get('src')
                 
         else:
             print('          ------段落：%s------'%(pcount))
             r=getText(line.get_text())
             list.append(r)
    data={"content":list}
    return (data,largestImg)
try:

    con = pymongo.MongoClient(host="192.168.13.22", port=27017)

except ConnectionFailure:

    sys.stderr.write("Could not connect to MongoDB: %s" % e)

    sys.exit(1)
db = con.master



driver =webdriver.PhantomJS(executable_path='D:\Python34\Scripts\phantomjs.exe')

brandlist=[
'http://toutiao.com/m5495741207/',
'http://toutiao.com/m4241104536/'
]
brandname=''
for brand in brandlist:

    for i in range(1,20):
        try:
            response= requests.get('%sp%s'%(brand,i))
            result=response.content.decode('UTF8')
            soup = BeautifulSoup(result)
            brandname=soup.find(class_='profile_name').find('a').string
            count=0
            for article in soup.findAll(class_='pin'):
                #if(article.find(class_='pin-content').find('h3',class_='list-h3')==None):
                #    continue
                count+=1
                title=article.find(class_='pin-content').find('h3').find('a').string
                url=article.find(class_='pin-content').find('h3').find('a').get('href')
                if(db.articles.find({"titleurl":url}).count()>0):
                    continue
                #driver.get(url)
                #articlefull=driver.page_source
                response= requests.get(url)
                articlefull=response.content.decode('UTF8')
                articlefull = BeautifulSoup(articlefull)
                title=articlefull.find(class_='title').find('h1').string
                content=articlefull.find(class_='article-content')

                date=articlefull.find(class_='time').string
                print('[%s-%s-%s],%s,%s'%(brandname,i,count,title,url))
                result=parseContent(content)
                entry={
                    'brandname':brandname,
                    'brandurl':brand,
                    'titleId':url.replace('http://toutiao.com/item/','').replace('/',''),
                    'titleurl':url,
                    'title':title,
                    'content':result[0],
                    'pnum':len(content.findAll('p')),
                    'imgnum':len(content.findAll('img')),
                    'largestImg':result[1],
                    'createDate':date
                    }
        
                id=db.articles.insert_one(entry).inserted_id
               
        except:
            f = open(r'D:\\qikan_data\\article\\log.txt','a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
    print('------头条号：%s-%s------'%(brandname,brand))
print("done")


