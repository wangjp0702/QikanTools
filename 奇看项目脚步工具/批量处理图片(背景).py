import hashlib, hmac,json, urllib.request
import HttpHandle,time
url ='http://dev.qikan.avosapps.com/api/user/backgroundimage'
#ÐÞ¸ÄÍ·Ïñ
appid= 'app.qikan.ios.001'
fr = open(r'd:\bbT.csv','r+')
fw = open(r'd:\cc.csv','w+')
for line in fr:
    user=line.split(',')
    email=user[0]
    userid=user[1].replace('\n','')
    token=user[2].replace('\n','')
    img1=user[3]
    img2=user[4].replace('\n','')
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
    http.filename=img2
    http.filepath='D:\\qikan_data\\backgroundImg\\'+img2
    http.contentType='image/jpg'
    http.accessKey=accessKey
    jsonresult=''
    jsonresult=json.loads(http.RequestPostFile())
   
    id=jsonresult['id']
    imgurl=jsonresult['displayImage']
    list0 =('%s,%s,%s,%s\n') % (email,userid,id,imgurl)   
                                                 
    fw.write(list0)
fw.flush()
fw.close()