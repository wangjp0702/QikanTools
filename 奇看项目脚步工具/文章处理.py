import hashlib, hmac,json, urllib.request
import HttpHandle,time,sys, re, json 
def getImg(imgurl):
    imgTag={"resource_url":imgurl,"resource_description":{"type":1,"image_size":500,"image_crop_rect":"0,0,", "image_width_rate":1}}
    return json.dumps(imgTag)
def getText(text):
    imgTag={"resource_description":{"type":2,"text":text,"text_alignment":0}}
    return json.dumps(imgTag)

url ='http://123.57.206.48:8080/register'
urluser='http://123.57.206.48:8080/user'
appid= 'app_test_000000000000001'


fr = open(r'D:\\qikan_data\\article\\1\1.txt','r+',-1,'utf-8')
#fwss = open(r'E:\\Code\?????????????????━??━??\????????????????━??━??\qikan_data\????.csv','w+')
re_title = re.compile('<title>(.*)</title>')
re_subtitle = re.compile('<subtitle>(.*)</subtitle>')
re_cover = re.compile('<cover>(.*)</cover>')
re_p = re.compile('<p>(.*)</p>')
re_img = re.compile('<img>(.*)</img>')
re_title = re.compile('<title>(.*)</title>')
re_title = re.compile('<title>(.*)</title>')

title=""
subtitle=""
creator=""
cover=""
content=""
for line in fr:
    m=re.search(re_title,line)
    if(m !=None):
        title=m.group(1)
    m=re.search(re_subtitle,line)
    if(m !=None):
        subtitle=m.group(1)
    m=re.search(re_cover,line)
    if(m !=None):
        cover=m.group(1)
    m=re.search(re_p,line)
    if(m !=None):
        text=m.group(1)
        r=getText(text)
        content+=r
    m=re.search(re_img,line)
    if(m !=None):
        img=m.group(1)      
        r=getImg(img)
        content+=r
print (content)
#db.getCollection('users').find({nickName:/Appuser/})

