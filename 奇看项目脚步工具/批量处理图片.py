import hashlib, hmac,json, urllib.request
import HttpHandle,time
url ='http://localhost:8080/user/displayImage'

appid= 'app_test_000000000000001'
fr = open(r'd:\bb.csv','r+')
fw = open(r'd:\cc.csv','w+')
for line in fr:
    user=line.split(',')
    nickname=user[0]
    password=user[1]
    email=user[2]
    intro=user[3]
    website=user[4].replace('\n','')
    userid=user[5].replace('\n','')
    token=user[6].replace('\n','')

    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('0123456789abcd0123456789'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 
    headers = { 'AccessKey' : accessKey, 'content-type':'application/json' }
    values = {"nickName":nickname,"webSite":website,"intro":intro}
  
    http=HttpHandle.Request()
    http.url=url
    http.method='PUT'
    http.headers=headers
    http.data=values
    http.filename='secondarytile.png'
    http.filepath='d:\\a.jpg'
    http.contentType='image/jpg'
    http.accessKey=accessKey
    jsonresult=''
    jsonresult=json.loads(http.RequestPostFile())
   
    id=jsonresult['_id']
    imgurl=jsonresult['url']
    list0 =('%s,%s,%s,%s,%s,%s,%s,%s\n') % (nickname,password,email,intro,website,userid,id,imgurl)   
                                                 
    fw.write(list0)
fw.flush()
fw.close()