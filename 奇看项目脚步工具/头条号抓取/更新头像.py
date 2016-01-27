import hashlib, hmac,json, urllib.request
import HttpHandle,time
url ='http://dev.qikan.avosapps.com/api/user/displayImage'
#ÐÞ¸ÄÍ·Ïñ
appid= 'app.qikan.ios.001'
fr = open(r'd:\\生成用户\\bbT.csv','r+')
fw = open(r'd:\\生成用户\\cc.csv','w+')
num=0
for line in fr:
    user=line.split(',')
    email=user[0]
    userid=user[1].replace('\n','')
    img1=user[2].replace('\n','')
    token=user[3].replace('\n','')
   
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('7cYooWzTzNLWGsCtddhPTgCt'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 
    headers = { 'AccessKey' : accessKey, 'content-type':'application/json' }
    values = {}
  
    http=HttpHandle.Request()
    http.url=url
    http.method='PUT'
    http.headers=headers
    http.data=values
    http.filename=img1
    http.filepath='D:\\生成用户\\头像\\'+img1
    http.contentType='image/'+img1[-3:]
    http.accessKey=accessKey
    jsonresult=''
    jsonresult=json.loads(http.RequestPostFile())
   
    id=jsonresult['id']
    imgurl=jsonresult['displayImage']
    list0 =('%s,%s,%s,%s\n') % (email,userid,id,imgurl)   
                                                 
    fw.write(list0)
fw.flush()
fw.close()