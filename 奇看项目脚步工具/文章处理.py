import hashlib, hmac,json, urllib.request
import HttpHandle,time,sys, re, json, HttpHandle 
from PIL import Image
import requests
import io
import imghdr
#imghdr.what()

def getImg(imgname):
    imagePath='D:\\qikan_data\\article\\1\\image\\'+imgname
    image=Image.open(imagePath);
    #im.format, im.size, im.mode
    imginfo=str(image.size[0])+','+str(image.size[1])

    appid='app_test_000000000000001'
    userid='557225a7883c06080947864d'
    token='5fd8669fdb82b1fb5b7cd53dc1aafa64e721267db6c38b3cab8961cfe472fa0ab17035e422c23565'
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('0123456789abcd0123456789'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 

    values = {'resourceType':1}
    url ='http://123.57.206.48:8080/item/resource'
    #url='http://localhost:8080/channel/backgroundImage'
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.data=values
    http.filename=imgname
    http.filepath=imagePath
    http.contentType='image/'+image.format
    http.accessKey=accessKey
    jsonresult=''
    jsonresult=json.loads(http.RequestPostFileWithData())
    imgurl=jsonresult['url']
    imgTag={"resource_url":imgurl,"resource_description":{"type":1,"image_size":imginfo,"image_crop_rect":"0,0,"+imginfo, "image_width_rate":1}}
    return imgTag
def getCoverImgID(imgname):
    imagePath='D:\\qikan_data\\article\\1\\image\\'+imgname
    image=Image.open(imagePath);
    #im.format, im.size, im.mode
    imginfo=str(image.size[0])+','+str(image.size[1])

    appid='app_test_000000000000001'
    userid='557225a7883c06080947864d'
    token='5fd8669fdb82b1fb5b7cd53dc1aafa64e721267db6c38b3cab8961cfe472fa0ab17035e422c23565'
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('0123456789abcd0123456789'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 

    values = {'resourceType':1}
    url ='http://123.57.206.48:8080/item/resource'
    #url='http://localhost:8080/channel/backgroundImage'
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.data=values
    http.filename=imgname
    http.filepath=imagePath
    http.contentType='image/'+image.format
    http.accessKey=accessKey
    jsonresult=''
    jsonresult=json.loads(http.RequestPostFileWithData())
    imgid=jsonresult['_id']
    return imgid
def getText(text):
    imgTag={"resource_description":{"type":2,"text":text,"text_alignment":0}}
    return imgTag

import sys

#url ='http://123.57.206.48:8080/register'
#urluser='http://123.57.206.48:8080/user'
#appid= 'app_test_000000000000001'


#fr2 = open(path.decode('gbk').encode('utf8'))
fr2=open(r'D:\qikan_data\article\超形态视觉艺术解析\1.txt','r+',-1,'utf-8')
for line in fr2:
    print(line)
fr = open(r'D:\\qikan_data\\article\\1\1.txt','r+',-1,'utf-8')
fw = open(r'D:\\qikan_data\\article\\1\2.txt','w+')
re_title = re.compile('<title>(.*)</title>')
re_subtitle = re.compile('<subtitle>(.*)</subtitle>')
re_cover = re.compile('<cover>(.*)</cover>')
re_p = re.compile('<p>(.*)</p>')
re_img = re.compile('<img>(.*)</img>')
#re_title = re.compile('<title>(.*)</title>')
#re_title = re.compile('<title>(.*)</title>')

title=""
subtitle=""
creator=""
coverid=""
content=""
list=[]
i=0
for line in fr:
    i+=1
    print(i)
    m=re.search(re_title,line)
    if(m !=None):
        title=m.group(1)
        continue
    m=re.search(re_subtitle,line)
    if(m !=None):
        subtitle=m.group(1)
        continue
    m=re.search(re_cover,line)
    if(m !=None):
        coverid=m.group(1)
        coverid=getCoverImgID(coverid)
        continue
    m=re.search(re_p,line)
    if(m !=None):
        text=m.group(1)
        r=getText(text)
        list.append(r)
        continue
    m=re.search(re_img,line)
    if(m !=None):
        img=m.group(1)      
        r=getImg(img)
        list.append(r)
        continue

data={"title":title,"subtitle":subtitle,"content":json.dumps(list,ensure_ascii=False),"converImageId":coverid}
#print(data)
fw.write(json.dumps(data,ensure_ascii=False))
fw.flush()
fw.close()
#db.getCollection('users').find({nickName:/Appuser/})

