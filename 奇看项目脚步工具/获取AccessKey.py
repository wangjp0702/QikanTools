import hashlib, hmac,json, urllib.request
import HttpHandle,time,sys

url ='http://123.57.206.48:8080/register'
urluser='http://123.57.206.48:8080/user'
appid= 'app_test_000000000000001'


userid='557225a7883c060809478648'
token='5fd8669fdb82b1fb5b7cd53dc1aafa645665d1f3da8f07b5c28776dee38654c09e036666847eb555'
timestamp=int(time.time())
plaintext=userid+'|'+str(timestamp)
h=hmac.new('0123456789abcd0123456789'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 
print(accessKey)