import hashlib, hmac,json, urllib.request
import HttpHandle,time,sys

url ='http://dev.qikan.avosapps.com/api/register'
urluser='http://dev.qikan.avosapps.com/api/user'
appid= 'app.qikan.ios.001'

fw = open(r'd:\\生成用户\\bbT.csv','w+')
#fwss = open(r'E:\\Code\???????????????????¨¬?????¨¬???\??????????????????¨¬?????¨¬???\qikan_data\????.csv','w+')

users=[
    {'name': '杨二扯犊子', 'email': 'yangercheduzi@user.qikan.com', 'headimg': 'yangercheduzi.png', 'intro': '嘘！看朕为你扯下的江山'},
    {'name': '萌大官人biubiubiu', 'email': 'mengdaguanren@user.qikan.com', 'headimg': 'mengdaguanren.jpg', 'intro': '不要惹我，我发起火来自助餐厅老板都怕的'},
    {'name': '叭叭老撕', 'email': 'babalaosi@user.qikan.com', 'headimg': 'babalaosi.png', 'intro': '世界那么大 我都不知道先撕谁比较好'},
    {'name': 'TF姐姐饭', 'email': 'TFjiejiefan@user.qikan.com', 'headimg': 'tfjiejiefan.jpg', 'intro': ''},
    {'name': '鹿晗你帅懵我了', 'email': 'luhannishuaimengwole@user.qikan.com', 'headimg': 'luhan.jpg', 'intro': ''},
    {'name': '夏洛克不是夏洛特', 'email': 'xialuokebushixialuote@user.qikan.com', 'headimg': 'xialuote.jpg', 'intro': '请用腐的方式打开我'},
    {'name': '腐大仁', 'email': 'fudaren@user.qikan.com', 'headimg': 'fudaren.png', 'intro': '再看，再看我就掰弯你'},
    {'name': '无水印强迫症', 'email': 'wushuiyinqiangpozheng@user.qikan.com', 'headimg': 'wushuiyin.png', 'intro': ''},
    {'name': '香水泡菜味 ', 'email': 'xiangshuipaocaiwei@user.qikan.com', 'headimg': 'xiangshuipaocai.png', 'intro': ''},
    {'name': 'rose不爱我 ', 'email': 'rosebuaiwo@user.qikan.com', 'headimg': 'rosebuaiwo.jpg', 'intro': ''},
    {'name': '萌叁妖', 'email': 'mengsanyao@user.qikan.com', 'headimg': 'mengsanyao.png', 'intro': ''},
    {'name': '羊小拍', 'email': 'yangxiaopai@user.qikan.com', 'headimg': 'yangxiaopai.jpg', 'intro': ''},
    {'name': 'Dollywish  ', 'email': 'dollywish@user.qikan.com', 'headimg': 'Dollywish.jpg', 'intro': ''},
    {'name': '水滴君', 'email': 'shuidijun@user.qikan.com', 'headimg': 'shuidijun.JPG', 'intro': ''},
    {'name': '有文化的王胖子', 'email': 'youwenhuadewangpangzi@user.qikan.com', 'headimg': 'youwenhuadewangpangzi.png', 'intro': '我在文化圈里“面子”最大'},
    {'name': 'B哥假装在T台 ', 'email': 'BgejiazhuangzaiTtai@user.qikan.com', 'headimg': 'Bgejiazhuang.jpg', 'intro': '谁在装逼，好刺眼'},
    {'name': '阿拉贝斯克', 'email': 'alabeisike@user.qikan.com', 'headimg': 'alabeisike.png', 'intro': ''},
    {'name': '锡儿与馨儿', 'email': 'xieryuxiner@user.qikan.com', 'headimg': 'xieryuxiner.png', 'intro': ''},
    {'name': '王阿聪', 'email': 'wangacong@user.qikan.com', 'headimg': 'wangacong.png', 'intro': '这个人很懒，真的很懒……'},
    {'name': 'vivi在远方', 'email': 'vivizaiyuanfang@user.qikan.com', 'headimg': 'vvzaiyuanfang.jpg', 'intro': ''},
    {'name': '三叔家的大表哥', 'email': 'sanshujiadedabiaoge@user.qikan.com', 'headimg': 'sanshujia.JPG', 'intro': ''},
    {'name': '男神大掌柜', 'email': 'nanshendazhanggui@user.qikan.com', 'headimg': 'nanshen.png', 'intro': ''},
    {'name': 'Edisonlee', 'email': 'edisonlee@user.qikan.com', 'headimg': 'Edisonlee.jpg', 'intro': '还说你不欣赏我！！'},
    {'name': '狗粮不够吃', 'email': 'gouliangbugouchi@user.qikan.com', 'headimg': 'gouliang.png', 'intro': '萌宠更新 限量供应'},
    {'name': '热血大虎', 'email': 'rexuedahu@user.qikan.com', 'headimg': 'rexuedahu.jpg', 'intro': ''},
    {'name': '太虚道长', 'email': 'taixudaozhang@user.qikan.com', 'headimg': 'taixudazhang.png', 'intro': '超级漫画饭，不要跟我争论动漫，不然你会输的很惨'}
]

for user in users: 
    nickname=user['name']
    password='2016120'
    email=user['email']
    img=user['headimg']
    website=''
    intro=user['intro']
    accessKey =appid
    values = {"email":email, "username":nickname,"password":password}
    headers = { 'appid' : accessKey, 'content-type':'application/json' }
  
    http=HttpHandle.Request()
    http.url=url
    http.method='POST'
    http.headers=headers
    http.data=values
   
    jsonresult=json.loads(http.RequestPost())
   
    userid=jsonresult['id']
    token=jsonresult['token']
    list0 =('%s,%s,%s,%s\n') % (email,userid,img,token)  
   
 
    timestamp=int(time.time())
    plaintext=userid+'|'+str(timestamp)
    h=hmac.new('7cYooWzTzNLWGsCtddhPTgCt'.encode('utf-8'),plaintext.encode('utf-8'),digestmod=hashlib.sha1)
    accessKey= appid+'|'+token+'|'+h.hexdigest()+'|'+str(timestamp) 
    headers = { 'AccessKey' : accessKey, 'content-type':'application/json' }
    values = {"webSite":website,"intro":intro}

    http.url=urluser
    http.method='PUT'
    http.headers=headers
    http.data=values
   
    jsonresult=json.loads(http.RequestPost())                                                  
    fw.write(list0)
                         
fw.flush()
fw.close()
#db.getCollection('users').find({nickName:/Appuser/})