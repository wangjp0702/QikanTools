import os,HttpHandle, json
from urllib.parse import urlparse

url=urlparse('http://g.bitauto.com/c2.aspx?queryStr=LxEQ/3+tfuMMUYXM467eiw==&adposid=17004&c=&f=http://11.m.yiche.com/&adurl=http://m.yichemall.com/car/detail/index?modelId=3100&source=yc-11-1yuandraw-1&k=32023936')

print(url.query)

#fr = open(r'D:\\cookie.txt','r+',-1,'utf-8')
#i=1
#for line in fr:
#    line=line.replace('\n','')
#    http=HttpHandle.Request()
#    http.url='http://fsp.yxziben.com/dss/mall/'+line
#    http.method='GET'
#    jsonresult=json.loads(http.RequestGet())
#    visits=jsonresult['visits']
#    i=i+1
#    for v in visits:
#        text=''
#        modelid=v['modelId']
#        score=v['score']
#        text=line+","+str(modelid)+","+str(score)+"\n"
#        f = open(r'D:\\cookieresult.txt','a')
#        f.writelines(text)
#        f.flush()
#        f.close()
#    print(i)