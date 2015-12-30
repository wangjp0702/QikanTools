import hashlib, hmac,json, urllib.request
import HttpHandle,time,sys

url ='http://123.57.206.48:8080/register'
urluser='http://123.57.206.48:8080/user'
appid= 'app.qikan.ios.001'


#userid='55c450d200b0b291197bd9d1'
#token='098af9b41357e568838cb4a10b02e0b894a1ddaff7afb4666e849828fc453adec67121aa0ecd69ce'
#timestamp=int(time.time())
#plaintext=userid+'|'+str(timestamp)
#h=hmac.new('7cYooWzTzNLWGsCtddhPTgCt'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
#accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 
#print(accessKey)

userid='55c4443560b2e5453f7abc8b'
token='ab7b9d759a591cd85f4139963fadd29647dc7c045ef952d6231dd633f7dce848f964c2c9b167ffaf'
timestamp=1439803807
plaintext=userid+'|'+str(timestamp)
h=hmac.new('7cYooWzTzNLWGsCtddhPTgCt'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 
print(accessKey)