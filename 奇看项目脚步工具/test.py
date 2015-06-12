import os,re,Model,HttpHandle, json,time,hashlib, hmac
from PIL import Image
#图片处理
def getImg(user,imgname,imgdir):
    imagePath=imgdir+'\\'+imgname
    image=Image.open(imagePath);
    #im.format, im.size, im.mode
    imginfo=str(image.size[0])+','+str(image.size[1])

    appid=config["appid"]
    userid=user.UserID
    token=user.Token
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('0123456789abcd0123456789'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 

    values = {'resourceType':1}
    url =config["newitemresource"]
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.data=values
    http.filename=imgname
    http.filepath=imagePath
    http.contentType='image/'+image.format
    http.accessKey=accessKey
    jsonresult=''
    jsonresult=json.loads(http.RequestPostFileWithData())
    imgurl=jsonresult['url']
    imgTag={"resource_url":imgurl,"resource_description":{"type":1,"image_size":imginfo,"image_crop_rect":"0,0,"+imginfo, "image_width_rate":1}}
    return imgTag
#封面图片处理
def getCoverImgID(user,imgname,imgdir):
    imagePath=imgdir+'\\'+imgname
    image=Image.open(imagePath);
    #im.format, im.size, im.mode
    imginfo=str(image.size[0])+','+str(image.size[1])

    appid=config["appid"]
    userid=user.UserID
    token=user.Token
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('0123456789abcd0123456789'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 

    values = {'resourceType':1}
    url =config["newitemresource"]
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.data=values
    http.filename=imgname
    http.filepath=imagePath
    http.contentType='image/'+image.format
    http.accessKey=accessKey
    jsonresult=''
    jsonresult=json.loads(http.RequestPostFileWithData())
    imgid=jsonresult['_id']
    return imgid
#文字处理
def getText(text):
    imgTag={"resource_description":{"type":2,"text":text,"text_alignment":0}}
    return imgTag
#获取用户token
def getUserInfo(user):
    url=config["login"]
    appid=config["appid"]
    accessKey =appid
    values = {"email":user.Email,"password":user.Password}
    headers = { 'appid' : accessKey, 'content-type':'application/json' }
  
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.headers=headers
    http.data=values
    jsonresult=json.loads(http.RequestPost())
    user.UserID=jsonresult['_id']
    user.Token=jsonresult['token']
#解析文章
def updateFile(user,filepath,imgdir):
    
    fr = open(filepath,'r+',-1,'utf-8')
    re_title = re.compile('<title>(.*)</title>')
    re_subtitle = re.compile('<subtitle>(.*)</subtitle>')
    re_cover = re.compile('<cover>(.*)</cover>')
    re_p = re.compile('<p>(.*)</p>')
    re_img = re.compile('<img>(.*)</img>')

    title=""
    subtitle=""
    creator=""
    coverid=""
    content=""
    list=[]
    i=0
    for line in fr:
        i+=1
        print(i)
        m=re.search(re_title,line)
        if(m !=None):
            title=m.group(1)
            continue
        m=re.search(re_subtitle,line)
        if(m !=None):
            subtitle=m.group(1)
            continue
        m=re.search(re_cover,line)
        if(m !=None):
            coverid=m.group(1)
            coverid=getCoverImgID(user,coverid,imgdir)
            continue
        m=re.search(re_p,line)
        if(m !=None):
            text=m.group(1)
            r=getText(text)
            list.append(r)
            continue
        m=re.search(re_img,line)
        if(m !=None):
            img=m.group(1)      
            r=getImg(user,img,imgdir)
            list.append(r)
            continue
    data={"title":title,"subtitle":subtitle,"content":json.dumps(list,ensure_ascii=False),"converImageId":coverid}
    return data#json.dumps(data,ensure_ascii=False)
#创建文章
def createItem(data):
    appid=config["appid"]
    userid=user.UserID
    token=user.Token
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('0123456789abcd0123456789'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 
    headers = { 'AccessKey' : accessKey, 'content-type':'application/json' }
    values = data
    url =config["newitem"]
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.data=values
    http.headers=headers
    jsonresult=''
    jsonresult=json.loads(http.RequestPost())
    itemid=jsonresult['_id']
config={'datapath':'D:\\qikan_data\\article','appid':'app_test_000000000000001','login':'http://123.57.206.48:8080/login','newitem':'http://123.57.206.48:8080/item','newitemresource':'http://123.57.206.48:8080/item/resource'}
L = os.listdir(config['datapath'])
email = re.compile('(.*)-(.*)')
listUsers=[]
for li in L:
    m=re.search(email,li)
    if(m !=None):
        user=Model.User()
        
        email=m.group(1)
        user.UserDir=m.group()
        user.Email=email
        user.Password='123456'
        getUserInfo(user)
        listUsers.append(user)

for user in listUsers:
    filedir=("%s\\%s")%(config['datapath'],user.UserDir)
    fileList=os.listdir(filedir)
    for file in fileList:
        filepath=('%s\\%s\\%s\\%s.txt')%(config['datapath'],user.UserDir,file,file)   
        imgdir=('%s\\%s\\%s\\image')%(config['datapath'],user.UserDir,file)   
        result=updateFile(user,filepath,imgdir)
        createItem(result)
        print(result)