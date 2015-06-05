import hashlib, hmac,json, urllib.request
import HttpHandle,time
url ='http://123.57.206.48:8080/channel/backgroundImage'

appid= 'app_test_000000000000001'
fr = open(r'd:\dclu.csv','r+')
fw = open(r'd:\dclu2.csv','w+')
for line in fr:
    user=line.split(',')
    name=user[0].replace('\n','')
    filename=user[1].replace('\n','')
   

  
    accessKey='app_test_000000000000001|3f3907d90c3b108a7fa8c6fe580ec398c6ee83bb6e424a17dfe97f8ff0bd6165616294a1ce9790b3|41c5b3f8eb0fea407a96eb66e33dc92c537c9b37|1430457601513' 
    headers = { 'AccessKey' : accessKey, 'content-type':'application/json' }
    values = {}
  
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.headers=headers
    http.data=values
    http.filename=filename
    http.filepath='d:\\'+filename
    http.contentType='image/png'
    http.accessKey=accessKey
    jsonresult=''
    jsonresult=json.loads(http.RequestPostFile())
   
    id=jsonresult['_id']
    imgurl=jsonresult['url']
    list0 =('%s,%s,%s\n') % (name,filename,id)   
                                                 
    fw.write(list0)
fw.flush()
fw.close()