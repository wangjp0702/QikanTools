import os,re,Model,HttpHandle,requests, json,time,hashlib, hmac, traceback
from PIL import Image
import pymongo,io
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure
#图片处理
def getImg(user,img):
    response = requests.get(img)
    image = Image.open(io.BytesIO(response.content))
   
    #im.format, im.size, im.mode
    imginfo=str(image.size[0])+','+str(image.size[1])

    appid=config["appid"]
    userid=user.UserID
    token=user.Token
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('7cYooWzTzNLWGsCtddhPTgCt'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 

    values ={}
    url =config["newitemresource"]
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.data=values
    http.filename=img.replace('http://p3.pstatp.com/','').replace('/','')+"."+image.format.lower()
    http.content=response.content
    http.contentType='image/'+image.format
    http.accessKey=accessKey
    jsonresult=''
    jsonresult=json.loads(http.RequestPostFileByte())
    imgurl=jsonresult['url']
    imgTag={"resource_url":imgurl,"resource_description":{"type":1,"image_size":imginfo,"image_crop_rect":"0,0,"+imginfo, "image_width_rate":1}}
    return imgTag
#封面图片处理
def getCoverImgID(user,largestImg):
    response = requests.get(largestImg)
    image = Image.open(io.BytesIO(response.content))
   
    #im.format, im.size, im.mode
    imginfo=str(image.size[0])+','+str(image.size[1])

    appid=config["appid"]
    userid=user.UserID
    token=user.Token
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('7cYooWzTzNLWGsCtddhPTgCt'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 

    values = {}
    url =config["newitemresource"]
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.data=values
    http.filename=largestImg.replace('http://p3.pstatp.com/','').replace('/','')+"."+image.format.lower()
    http.content=response.content
    http.contentType='image/'+image.format
    http.accessKey=accessKey
    jsonresult=''
    jsonresult=json.loads(http.RequestPostFileByte())
    imgid=jsonresult['id']
    return imgid
#文字处理
def getText(text):
    imgTag={"resource_description":{"type":2,"text":text,"text_alignment":0}}
    return imgTag
#小标题处理
def getTitleText(text):
    titleTag={"resource_description":{"type":3,"text":text,"text_alignment":0}}  
    return titleTag
def getIndexText(text):
    titleTag={"resource_description":{"type":4,"text":text,"text_alignment":0}}  
    return titleTag
#获取用户token
def getUserInfo(user):
    url=config["login"]
    appid=config["appid"]
    accessKey =appid
    values = {"username":user.UserName,"password":user.Password}
    headers = { 'appid' : accessKey, 'content-type':'application/json' }
  
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.headers=headers
    http.data=values
    jsonresult=json.loads(http.RequestPost())
    user.UserID=jsonresult['id']
    user.Token=jsonresult['token']
#解析文章
def updateFile(user,article):
    
 
    title=article['title']
    subtitle=""
    creator=""
    coverid=""
    content=""
    list=[]
    i=0
    if(article['largestImg']!=None):
        coverid=getCoverImgID(user,article['largestImg'])
        print('          ------封面：%s------')
    pcount=0
    for line in article['content']['content']:
        pcount=pcount+1
        if('image' in line):
             r=getImg(user,line['image'])
             list.append(r)
             print('          ------图片：%s------'%(pcount))
        if('text' in line):
             r=getText(line['text'])
             list.append(r)
             print('          ------段落：%s------'%(pcount))
    list.append(getText('本文来自 头条号 '+article['brandname']))
    data={"title":title,"subTitle":subtitle,"content":json.dumps(list,ensure_ascii=False),"coverImageId":coverid,"createdAt":article['createDate'],"status":1}
    return data#json.dumps(data,ensure_ascii=False)
#创建文章
def createItem(data):
    appid=config["appid"]
    userid=user.UserID
    token=user.Token
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('7cYooWzTzNLWGsCtddhPTgCt'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
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
    itemid=jsonresult['id']
    return itemid
config={'datapath':'D:\\qikan_data\\article','appid':'app.qikan.ios.001','login':'http://dev.qikan.avosapps.com/api/login','newitem':'http://dev.qikan.avosapps.com/api/story','newitemresource':'http://dev.qikan.avosapps.com/api/story/resource'}
L = os.listdir(config['datapath'])
re_email = re.compile('(.*)-(.*)')
listUsers=[]


users=[
   
    {'username': '韩妞妞', 'email': '001533871739432@user.qikan.com'},
    {'username': '八酱', 'email': '001533872078405@user.qikan.com'},
    {'username': 'Veeeee', 'email': '001533873417378@user.qikan.com'},
    {'username': '半颗凯妃糖', 'email': '001533874756350@user.qikan.com'},
    {'username': '正能量小甜食', 'email': '001533875095322@user.qikan.com'},
    {'username': '月光粥', 'email': '001533876434293@user.qikan.com'},
    {'username': '二喜子', 'email': '001533877773264@user.qikan.com'},
    {'username': 'kangkang_', 'email': '001533878112235@user.qikan.com'},
    {'username': 'Solo', 'email': '001533879451205@user.qikan.com'},
    {'username': '怎样了？', 'email': '001533880790175@user.qikan.com'},
    {'username': 'arbacid', 'email': '001533881129144@user.qikan.com'},
    {'username': 'hirai ken', 'email': '001533882468113@user.qikan.com'},
    {'username': '貓豬', 'email': '001533883807081@user.qikan.com'},
    {'username': '瞅你咋地', 'email': '001533884146049@user.qikan.com'},
    {'username': 'DARKMAN', 'email': '001533885485016@user.qikan.com'},
    {'username': 'Cindou', 'email': '001533886823983@user.qikan.com'},
    {'username': '雷司令', 'email': '001533887162950@user.qikan.com'},
    {'username': 'Narcissism', 'email': '001533888501916@user.qikan.com'},
    {'username': '幼齿控', 'email': '001533889840882@user.qikan.com'},
    {'username': '快闪碗里来', 'email': '001533890179847@user.qikan.com'},
    {'username': '我要变成大瘦子', 'email': '001533891518812@user.qikan.com'},
    {'username': '屁股大坐的稳', 'email': '001533892857776@user.qikan.com'},
    {'username': '肚子兔子', 'email': '001533893196740@user.qikan.com'},
    {'username': '怪你过分美丽', 'email': '001533894535704@user.qikan.com'},
    {'username': '你就像烈酒', 'email': '001533895874667@user.qikan.com'},
    {'username': '拖延症患者', 'email': '001533896213629@user.qikan.com'},
    {'username': '我说我不知道', 'email': '001533897552591@user.qikan.com'},
    {'username': 'alexiachen', 'email': '001533898891553@user.qikan.com'},
    {'username': '棉花糖甜甜甜甜', 'email': '001533899230515@user.qikan.com'},
    {'username': '小王子的面包树 ', 'email': '001533900569475@user.qikan.com'},
    {'username': '拔丝红薯大赢家', 'email': '001533901908436@user.qikan.com'},
    {'username': '别扭的鸵鸟', 'email': '001533902247396@user.qikan.com'},
    {'username': '芋头比我美', 'email': '001533903586356@user.qikan.com'},
    {'username': '卡罗莱大魔王', 'email': '001533904925315@user.qikan.com'},
    {'username': '困伐醒呃懒破驹', 'email': '001533905264273@user.qikan.com'},
    {'username': '冲田总悟', 'email': '001533906603232@user.qikan.com'},
    {'username': '乌云乌云快走开', 'email': '001533907942190@user.qikan.com'},
    {'username': '梅长苏的玉冠', 'email': '001533908281147@user.qikan.com'},
    {'username': '谁家那小谁', 'email': '001533909620104@user.qikan.com'},
    {'username': '奥黛丽·和平', 'email': '001533910959060@user.qikan.com'},
    {'username': '清热解毒板蓝根', 'email': '001533911298017@user.qikan.com'},
    {'username': '蕾丝李', 'email': '001533912636972@user.qikan.com'},
    {'username': '平胸少女', 'email': '001533913975927@user.qikan.com'},
    {'username': '奶酪永动机', 'email': '001533914314882@user.qikan.com'},
    {'username': '大婶来买豆沙包', 'email': '001533915653837@user.qikan.com'},
    {'username': '爱ci布丁的布丁', 'email': '001533916992790@user.qikan.com'},
    {'username': '你们都没有我美', 'email': '001533917331744@user.qikan.com'},
    {'username': '凌晨喝咖啡', 'email': '001533918670697@user.qikan.com'},
    {'username': '一胖二白', 'email': '001533919009650@user.qikan.com'},
    {'username': '撒西不理', 'email': '001533920348602@user.qikan.com'},
    {'username': '阿花小姐', 'email': '001533921687553@user.qikan.com'},
    {'username': '尊小肥', 'email': '001533922026505@user.qikan.com'},
    {'username': '周二围', 'email': '001533923365456@user.qikan.com'},
    {'username': ' 悟空的金箍棒', 'email': '001533924704406@user.qikan.com'},
    {'username': 'kkkkkkkira ', 'email': '001533925043356@user.qikan.com'},
    {'username': '姨妈的鸭', 'email': '001533926382306@user.qikan.com'},
    {'username': ' 貌美的小黄鸡', 'email': '001533927721255@user.qikan.com'},
    {'username': ' 喝醉酒的蚊子', 'email': '001533928060203@user.qikan.com'},
    {'username': '夜夜夜夜', 'email': '001533929399152@user.qikan.com'},
    {'username': '橙子子子子', 'email': '001533930738099@user.qikan.com'},
    {'username': 'Geronimo', 'email': '001533931077047@user.qikan.com'},
    {'username': ' 远在远方的风', 'email': '001533932415994@user.qikan.com'},
    {'username': '牛先生的鹿小姐', 'email': '001533933754940@user.qikan.com'},
    {'username': ' HammerWong', 'email': '001533934093886@user.qikan.com'},
    {'username': '菇凉身边很凉快', 'email': '001533935432832@user.qikan.com'},
    {'username': 'Summer Melody', 'email': '001533936771777@user.qikan.com'},
    {'username': '吼吼吼菜菜大包', 'email': '001533937110722@user.qikan.com'},
    {'username': ' 蛋黄派讲故事', 'email': '001533938449666@user.qikan.com'},
    {'username': ' 一天不犯傻比我就会死掉', 'email': '001533939788610@user.qikan.com'},
    {'username': '哲学家吉他手', 'email': '001533940127553@user.qikan.com'},
    {'username': '列宁的奶猫', 'email': '001533941466496@user.qikan.com'},
    {'username': 'KK_en_france', 'email': '001533942805439@user.qikan.com'},
    {'username': ' cherieleeeeee', 'email': '001533943144381@user.qikan.com'},
    {'username': '沉沦的mojito', 'email': '001533944483323@user.qikan.com'},
    {'username': ' 宇宙大魔王', 'email': '001533945822264@user.qikan.com'},
    {'username': 'La Habana', 'email': '001533946161205@user.qikan.com'},
    {'username': '脸大了怎么样', 'email': '001533947500145@user.qikan.com'},
    {'username': ' 煲汤的高压锅', 'email': '001533948839085@user.qikan.com'},
    {'username': '哼一首歌给哈尼', 'email': '001533949178025@user.qikan.com'}
]
try:

    con = pymongo.MongoClient(host="192.168.13.22", port=27017)

except ConnectionFailure:

    sys.stderr.write("Could not connect to MongoDB: %s" % e)

    sys.exit(1)
db = con.master
count=0
try:
    for l in users:
            user=Model.User()
            user.UserName=l['username']
            user.Password='qikanuser2016111'
            getUserInfo(user)
            listUsers.append(user)

            

    for user in listUsers:
        count=count+1
        articles=db.articles.find({"largestImg":{ "$ne":""},"_id":{"$gt":ObjectId('56942e850a18f758e46c4dd2')}}).sort("_id").skip((count-1)*30).limit(30)
        for article in articles:
            try:
                result=updateFile(user,article)
                itemid=createItem(result)
                successlog='文章id:%s 用户:%s 文章:%s \n'%(itemid,user.UserName,article['title'])
                print(successlog)
                f = open(r'D:\\qikan_data\\article\\success.txt','a')
                f.writelines(successlog)
                f.writelines('--------------------------------------------------------------------\n')
                f.flush()
                f.close()
            except:
                continue
except:
    f = open(r'D:\\qikan_data\\article\\log.txt','a')
    traceback.print_exc(file=f)
    f.flush()
    f.close()
