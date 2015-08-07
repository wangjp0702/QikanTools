import hashlib, hmac,json, urllib.request
import HttpHandle,time,sys

url ='http://dev.qikan.avosapps.com/api/register'
urluser='http://dev.qikan.avosapps.com/api/user'
appid= 'app.qikan.ios.001'
fr = open(r'd:\aaT.csv','r+')
fw = open(r'd:\bbT.csv','w+')
#fwss = open(r'E:\\Code\???????????????????¨¬?????¨¬???\??????????????????¨¬?????¨¬???\qikan_data\????.csv','w+')
for line in fr:
    user=line.split('##')
    nickname=user[0]
    password=user[1]
    email=user[2].replace(' ','')
    intro=user[3]
    website=user[4].replace('\n','')
    accessKey =appid
    values = {"email":email, "username":nickname,"password":password}
    headers = { 'appid' : accessKey, 'content-type':'application/json' }
  
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.headers=headers
    http.data=values
   
    jsonresult=json.loads(http.RequestPost())
   
    userid=jsonresult['id']
    token=jsonresult['token']
    list0 =('%s,%s,%s\n') % (email,userid,token)  
   
 
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('7cYooWzTzNLWGsCtddhPTgCt'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 
    headers = { 'AccessKey' : accessKey, 'content-type':'application/json' }
    values = {"webSite":website,"intro":intro}

    http.url=urluser
    http.method='PUT'
    http.headers=headers
    http.data=values
   
    jsonresult=json.loads(http.RequestPost())                                                  
    fw.write(list0)
fw.flush()
fw.close()
#db.getCollection('users').find({nickName:/Appuser/})