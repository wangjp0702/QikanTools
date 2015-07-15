import hashlib, hmac,json, urllib.request
import HttpHandle,time,sys

url ='http://123.57.206.48:8080/register'
urluser='http://123.57.206.48:8080/user'
appid= 'app_test_000000000000001'


userid='5570442b6c857fac09486812'
token='a0d45a92588a3f3f492c739e55116e5d1a7ed48777dad109d93b02bdd6a0956b0e8adb0cc461a6dd'
timestamp=int(time.time())
plaintext=userid+'|'+str(timestamp)
h=hmac.new('0123456789abcd0123456789'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 
print(accessKey)