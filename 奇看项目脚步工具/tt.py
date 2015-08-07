import hashlib, hmac,json,urllib
#url = 'http://localhost:8080/user/5540a483a68994b411618808'
url = 'http://localhost:8080/register'

import HttpHandle
import time
print (int(time.time()))

accessKey = 'app_test_000000000000001|3f3907d90c3b108a7fa8c6fe580ec398c6ee83bb6e424a17dfe97f8ff0bd6165616294a1ce9790b3|41c5b3f8eb0fea407a96eb66e33dc92c537c9b37|1430457601513'
values = {'name' : 'WHY',    
         'location' : 'SDU',    
         'language' : 'Python',
         'ie' : 'utf-8',
         'wd' : 'python' }
headers = { 'accessKey' : accessKey } 


#http=HttpHandle.Request()
#http.url='http://localhost:8080/user/5540a483a68994b411618808'
#http.method='GET'
#http.headers=headers
#http.data=''

h=hmac.new('0123456789abcd0123456789'.encode('utf-8'),'5540a483a68994b411618808|1430356494320'.encode('utf-8'),digestmod=hashlib.sha1)
print(h.hexdigest())
values={"email":"146127310@qq.com", "nickName":"aaa","password":"123456"}
#headers = { 'accessKey' : accessKey }
headers = { 'appId' : 'app_test_000000000000001','content-type':'application/json' }
data =json.dumps(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data=data,headers=headers,method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('UTF8'))
#json=json.loads(req)
#print(json)