import hashlib, hmac,json, urllib.request
import HttpHandle,time
url ='http://localhost:8080/register'
urluser='http://123.57.206.48:8080/channel'
appid= 'app_test_000000000000001'
fr = open(r'd:\dclu2.csv','r+')
fw = open(r'd:\dclu3.csv','w+')
#fw = open('E:\Code\?????????????????????━????????━????\????????????????????━????????━????\qikan_data\???????????：??????.csv','w+')
for line in fr:
    user=line.split(',')
    name=user[0].replace('\n','')
    fileid=user[2].replace('\n','')
   

  
    accessKey='app_test_000000000000001|3f3907d90c3b108a7fa8c6fe580ec398c6ee83bb6e424a17dfe97f8ff0bd6165616294a1ce9790b3|41c5b3f8eb0fea407a96eb66e33dc92c537c9b37|1430457601513' 
    headers = { 'AccessKey' : accessKey, 'content-type':'application/json' }
    values = {"name":name,"backgroundImageId":fileid}
    http=HttpHandle.Request()
    http.url=urluser
    http.method='POST'
    http.headers=headers
    http.data=values
   
    jsonresult=json.loads(http.RequestPost())   
    id=jsonresult['_id']
    
    list0 =('%s,%s\n') % (name,id)                                                  
    fw.write(list0)
fw.flush()
fw.close()