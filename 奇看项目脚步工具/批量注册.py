import hashlib, hmac,json, urllib.request
import HttpHandle
url = 'http://localhost:8080/register'

fr = open(r'd:\aa.csv','r+')
fw = open(r'd:\bb.csv','w+')
#fw = open('E:\Code\奇看项目脚本工具\奇看项目脚步工具\qikan_data\数据结果.csv','w+')
for line in fr:
    user=line.split(',')
    nickname=user[0]
    password=user[1]
    email=user[2]
    intro=user[3]
    website=user[4].replace('\n','')
    accessKey = 'app_test_000000000000001'
    values = {"email":email, "nickName":nickname,"password":password}
    headers = { 'appid' : accessKey, 'content-type':'application/json' }


    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.headers=headers
    http.data=values
    data =json.dumps(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url,data=data,headers=headers,method='POST')
    response = urllib.request.urlopen(req)
   # print(response.read().decode('UTF8'))
    jsonresult=json.loads(response.read().decode('UTF8'))
   
    userid=jsonresult['_id']
    list0 =('%s,%s,%s,%s,%s,%s\n') % (nickname,password,email,intro,website,userid)                                                          
    fw.write(list0)
fw.flush()
fw.close()