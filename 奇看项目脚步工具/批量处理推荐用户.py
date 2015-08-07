import hashlib, hmac,json, urllib.request
import HttpHandle,time
url ='http://dev.qikan.avosapps.com/api/recommend'
#ÐÞ¸ÄÍ·Ïñ
appid= 'app.qikan.ios.001'

fw = open(r'd:\ccuser.csv','w+')
users=['55c4443560b2e5453f7abc87',
    '55c4443560b2e5453f7abc8b',
    '55c4443560b2824f20dead5c',
    '55c4443760b2f809e42a1a8f',
    '55c4443860b2d140ca8e3cec',
    '55c4443960b2e4c604c9c1bc',
    '55c4443960b2f809e42a1ad7',
    '55c4443960b2e4c604c9c1d8',
    '55c4443a60b2824f20deae01',
    '55c4443b60b2d140ca8e3d40',
    '55c4443b60b2d140ca8e3d54',
    '55c4443b60b2c9d32a6e86b7',
    '55c4443b60b2279e8535b261',
    '55c4443c60b2f809e42a1b42',
    '55c4443c60b2824f20deae3f',
    '55c4443c60b2e5453f7abd72',
    '55c4443c60b2d140ca8e3d7e',
    '55c4443c60b2279e8535b27b',
    '55c4443c60b2c7de0ddb433c',
    '55c4443d60b2e5453f7abd89']
for user in users:
    
    accessKey='app.qikan.ios.001|098af9b41357e568838cb4a10b02e0b894a1ddaff7afb4666e849828fc453adec67121aa0ecd69ce|ed9dff9b1f7beaef83c5edabde93f2eb3c125add|1438929823' 
    headers = { 'AccessKey' : accessKey, 'content-type':'application/json' }
    values = {"id":user,"type":3}
  
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.headers=headers
    http.data=values

   
    jsonresult=json.loads(http.RequestPost())
   
    id=jsonresult['id']
    
    list0 =('%s\n') % (id)   
                                                 
    fw.write(list0)
fw.flush()
fw.close()