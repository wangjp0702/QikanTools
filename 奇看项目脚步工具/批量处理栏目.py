import hashlib, hmac,json, urllib.request
import HttpHandle,time
url ='http://localhost:8080/register'
urluser='http://localhost:8080/user'
appid= 'app_test_000000000000001'
fr = open(r'd:\aa.csv','r+')
fw = open(r'd:\bb.csv','w+')
#fw = open('E:\Code\???????????????¡§¡§??\??????????????¡§¡§??\qikan_data\??????¡ì???.csv','w+')
for line in fr:
    user=line.split(',')
    nickname=user[0]
    password=user[1]
    email=user[2]
    intro=user[3]
    website=user[4].replace('\n','')
    accessKey =appid
    values = {"email":email, "nickName":nickname,"password":password}
    headers = { 'appid' : accessKey, 'content-type':'application/json' }
  
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.headers=headers
    http.data=values
   
    jsonresult=json.loads(http.RequestPost())
   
    userid=jsonresult['_id']
    token=jsonresult['token']
    list0 =('%s,%s,%s,%s,%s,%s,%s\n') % (nickname,password,email,intro,website,userid,token)   
   
    #?¨¹?????¡ì???? 
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('0123456789abcd0123456789'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 
    headers = { 'AccessKey' : accessKey, 'content-type':'application/json' }
    values = {"nickName":nickname,"webSite":website,"intro":intro}

    http.url=urluser
    http.method='PUT'
    http.headers=headers
    http.data=values
   
    jsonresult=json.loads(http.RequestPost())                                                  
    fw.write(list0)
fw.flush()
fw.close()