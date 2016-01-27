import os,HttpHandle, json
from urllib.parse import urlparse



fr = open(r'D:\\url.txt','r+',-1,'utf-8')
i=1
for line in fr:
    line=line.replace('\n','')
    http=HttpHandle.Request()
    http.url=line
    http.method='GET'
    jsonresult=json.loads(http.RequestGet())
    visits=jsonresult['visits']
    cookie=jsonresult['cookie']
    i=i+1
    for v in visits:
        text=''
        modelid=v['modelId']
        score=v['score']
        style=v['styleId']
        sku=v['skuId']
        type=v['type']
        text=cookie+","+str(modelid)+","+str(style)+","+str(sku)+","+str(type)+","+str(score)+"\n"
        f = open(r'D:\\urlresult.txt','a')
        f.writelines(text)
        f.flush()
        f.close()
    print(i)