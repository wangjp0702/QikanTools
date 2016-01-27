import hashlib, hmac,json, urllib.request
import HttpHandle,time,sys

url ='http://dev.qikan.avosapps.com/api/register'
urluser='http://dev.qikan.avosapps.com/api/user'
appid= 'app.qikan.ios.001'
fr = open(r'd:\aaT.csv','r+')
fw = open(r'd:\bbT.csv','w+')
#fwss = open(r'E:\\Code\???????????????????¨¬?????¨¬???\??????????????????¨¬?????¨¬???\qikan_data\????.csv','w+')

users=[
    {username: 'Arno', email: '001528769607277@user.qikan.com'},
    {username: 'pangcky', email: '001528770948482@user.qikan.com'},
    {username: '老炮儿', email: '001528771289688@user.qikan.com'},
    {username: 'hahaha', email: '001528772630892@user.qikan.com'},
    {username: '木子', email: '001528773972096@user.qikan.com'},
    {username: '栾虎', email: '001528774313300@user.qikan.com'},
    {username: '骆驼', email: '001528775654504@user.qikan.com'},
    {username: 'Arzes', email: '001528776995707@user.qikan.com'},
    {username: '紫醉金迷', email: '001528777336909@user.qikan.com'},
    {username: '扎西布一', email: '001528778678111@user.qikan.com'},
    {username: '龙尼 ', email: '001528779019313@user.qikan.com'},
    {username: '泥萌够了', email: '001528780360514@user.qikan.com'},
    {username: '偶像费玉清', email: '001528781701715@user.qikan.com'},
    {username: '蘑菇不开花', email: '001528782042915@user.qikan.com'},
    {username: '斯坦不二子', email: '001528783384115@user.qikan.com'},
    {username: '幽明怙主', email: '001528784725314@user.qikan.com'},
    {username: 'ＣactuS 光', email: '001528785066513@user.qikan.com'},
    {username: 'kehan', email: '001528786407712@user.qikan.com'},
    {username: 'MISS.想太多', email: '001528787748910@user.qikan.com'},
    {username: '念念鱼', email: '001528788090107@user.qikan.com'},
    {username: '魔法师小青', email: '001528789431305@user.qikan.com'},
    {username: 'Licerain在豆瓣', email: '001528790772501@user.qikan.com'},
    {username: 'mini大苏', email: '001528791113698@user.qikan.com'},
    {username: '囍囍囍囍囍囍囍', email: '001528792454894@user.qikan.com'},
    {username: '冬天暖暖哒', email: '001528793796089@user.qikan.com'},
    {username: '六个花卷 ', email: '001528794137284@user.qikan.com'},
    {username: '病娇小公举', email: '001528795478479@user.qikan.com'},
    {username: '差不多和在路上', email: '001528796819673@user.qikan.com'},
    {username: '吃遍南宁的果果', email: '001528797160867@user.qikan.com'},
    {username: 'dodo不会飞', email: '001528798502060@user.qikan.com'},
    {username: '炮弹下不死不勃', email: '001528799843253@user.qikan.com'},
    {username: '过期少年', email: '001528800184445@user.qikan.com'},
    {username: 'LULUxxx', email: '001528801525637@user.qikan.com'},
    {username: '美艳的小麋鹿', email: '001528802866828@user.qikan.com'},
    {username: '点赞的伊丽莎白', email: '001528803208020@user.qikan.com'},
    {username: '手癌晚期', email: '001528804549210@user.qikan.com'},
    {username: '化了妆的泥霸霸', email: '001528805890400@user.qikan.com'},
    {username: '哎呀你个小可爱', email: '001528806231590@user.qikan.com'},
    {username: '叔叔而已', email: '001528807572779@user.qikan.com'},
    {username: '叽里咕噜澎恰恰', email: '001528808913968@user.qikan.com'},
    {username: '奥利芙和奥利奥', email: '001528809255157@user.qikan.com'},
    {username: '陆地上的乌龟', email: '001528810596345@user.qikan.com'},
    {username: '沙滩上德脚印', email: '001528811937532@user.qikan.com'},
    {username: '尼古拉斯赵驷', email: '001528812278719@user.qikan.com'},
    {username: '一个无趣的人', email: '001528813619906@user.qikan.com'},
    {username: '吃土少女', email: '001528814961092@user.qikan.com'},
    {username: '地瓜我是蛋卷啊', email: '001528815302278@user.qikan.com'},
    {username: 'Oguri的真爱', email: '001528816643464@user.qikan.com'},
    {username: '汤圆酱姨', email: '001528817984649@user.qikan.com'},
    {username: '叽里咕噜澎恰恰', email: '001528818325833@user.qikan.com'},
    {username: '提莫队长', email: '001528819667017@user.qikan.com'},
    {username: '碎花袄', email: '001528820008201@user.qikan.com'},
    {username: '铁皮姑娘', email: '001528821349384@user.qikan.com'},
    {username: '苹果果', email: '001528822690567@user.qikan.com'},
    {username: '呵呵哒', email: '001528823031749@user.qikan.com'},
    {username: '啵珠是波珠', email: '001528824372931@user.qikan.com'},
    {username: '疯了的鲸七七', email: '001528825714112@user.qikan.com'},
    {username: '洛洛就是爱二熊', email: '001528826055293@user.qikan.com'},
    {username: '瓦令瓦令', email: '001528827396474@user.qikan.com'},
    {username: '布衣书食', email: '001528828737654@user.qikan.com'},
    {username: '等会吃什么', email: '001528829078834@user.qikan.com'},
    {username: '倪嗨嗨', email: '001528830420013@user.qikan.com'},
    {username: '不靠谱的文艺犯', email: '001528831761192@user.qikan.com'},
    {username: '长尾豹尾巴MUA', email: '001528832102370@user.qikan.com'},
    {username: '烟圈里的绵绵', email: '001528833443548@user.qikan.com'},
    {username: '曹肥肥??', email: '001528834784725@user.qikan.com'},
    {username: '三毛或二毛', email: '001528835125902@user.qikan.com'},
    {username: 'Nirvana', email: '001528836467079@user.qikan.com'},
    {username: '喵大哥白露西', email: '001528837808255@user.qikan.com'},
    {username: '花伦的小丸子', email: '001528838149431@user.qikan.com'},
    {username: '你看起来很美味', email: '001528839490606@user.qikan.com'},
    {username: '没头脑和不高兴', email: '001528840831781@user.qikan.com'},
    {username: '大王来巡山', email: '001528841172955@user.qikan.com'},
    {username: '长颈鹿小姐', email: '001528842514129@user.qikan.com'},
    {username: '烟圈里的绵绵', email: '001528843855303@user.qikan.com'},
    {username: '姐姐是个老中医', email: '001528844196476@user.qikan.com'},
    {username: '惊慌少女', email: '001528845537649@user.qikan.com'},
    {username: '小小耽', email: '001528846878821@user.qikan.com'},
    {username: '木木.夕', email: '001528847219993@user.qikan.com'},
    {username: '进击中的小伍长', email: '001528848561164@user.qikan.com'},
    {username: '叉丽十二', email: '001528849902335@user.qikan.com'},
    {username: 'Jeremy_Sun', email: '001528850243505@user.qikan.com'},
    {username: '米兰小铁匠', email: '001528851584675@user.qikan.com'},
    {username: 'zeo~郑郑郑', email: '001528852925845@user.qikan.com'},
    {username: '过期少年', email: '001528853267014@user.qikan.com'},
    {username: '密斯宗', email: '001528854608183@user.qikan.com'},
    {username: 'HMNNV_A', email: '001528855949351@user.qikan.com'},
    {username: '小结巴菌', email: '001528856290519@user.qikan.com'},
    {username: 'zikunniee', email: '001528857631686@user.qikan.com'},
    {username: '貓先生', email: '001528858972853@user.qikan.com'},
    {username: 'crystal是只猫', email: '001528859314020@user.qikan.com'},
    {username: '李麻烦', email: '001528860655186@user.qikan.com'},
    {username: '诶诶诶', email: '001528861996351@user.qikan.com'},
    {username: '安静的小逗比', email: '001528862337517@user.qikan.com'},
    {username: '妮玛太后', email: '001528863678681@user.qikan.com'},
    {username: 'Ray-Ban先生', email: '001528864019846@user.qikan.com'},
    {username: '猫奶奶', email: '001528865361010@user.qikan.com'},
    {username: 'Not A Bad Guy', email: '001528866702173@user.qikan.com'},
    {username: '跳动 NIK.  SAGA', email: '001528867043336@user.qikan.com'},
    {username: '绿绿变红红', email: '001528868384499@user.qikan.com'},
    {username: '黑沼爽子', email: '001528869725661@user.qikan.com'},
    {username: '卷卷', email: '001528870066822@user.qikan.com'},
    {username: '丢啊丢', email: '001528871407984@user.qikan.com'},
    {username: 'Leolure', email: '001528872749144@user.qikan.com'},
    {username: 'Ningill', email: '001528873090305@user.qikan.com'},
    {username: '十七七七七', email: '001528874431465@user.qikan.com'},
    {username: '翟郦', email: '001528875772624@user.qikan.com'},
    {username: 'sesame', email: '001528876113783@user.qikan.com'},
    {username: '歪是只猫', email: '001528877454942@user.qikan.com'},
    {username: 'Bingo kila', email: '001528878796100@user.qikan.com'},
    {username: '.M.i.a.', email: '001528879137258@user.qikan.com'},
    {username: 'inwhat', email: '001528880478415@user.qikan.com'},
    {username: '幼安笔记', email: '001528881819572@user.qikan.com'},
    {username: '方哩个方', email: '001528882160728@user.qikan.com'},
    {username: '地瓜我是蛋卷啊', email: '001528883501884@user.qikan.com'},
    {username: 'babibobi', email: '001528884843040@user.qikan.com'},
    {username: 'cc-mm-hh', email: '001528885184195@user.qikan.com'},
    {username: 'Kenneth', email: '001528886525350@user.qikan.com'},
    {username: '只只只只', email: '001533868722510@user.qikan.com'},
    {username: '烏雲君', email: '001533869061485@user.qikan.com'},
    {username: '豆啊瓣啊酱', email: '001533870400459@user.qikan.com'},
    {username: '韩妞妞', email: '001533871739432@user.qikan.com'},
    {username: '八酱', email: '001533872078405@user.qikan.com'},
    {username: 'Veeeee', email: '001533873417378@user.qikan.com'},
    {username: '半颗凯妃糖', email: '001533874756350@user.qikan.com'},
    {username: '正能量小甜食', email: '001533875095322@user.qikan.com'},
    {username: '月光粥', email: '001533876434293@user.qikan.com'},
    {username: '二喜子', email: '001533877773264@user.qikan.com'},
    {username: 'kangkang_', email: '001533878112235@user.qikan.com'},
    {username: 'Solo', email: '001533879451205@user.qikan.com'},
    {username: '怎样了？', email: '001533880790175@user.qikan.com'},
    {username: 'arbacid', email: '001533881129144@user.qikan.com'},
    {username: 'hirai ken', email: '001533882468113@user.qikan.com'},
    {username: '貓豬', email: '001533883807081@user.qikan.com'},
    {username: '瞅你咋地', email: '001533884146049@user.qikan.com'},
    {username: 'DARKMAN', email: '001533885485016@user.qikan.com'},
    {username: 'Cindou', email: '001533886823983@user.qikan.com'},
    {username: '雷司令', email: '001533887162950@user.qikan.com'},
    {username: 'Narcissism', email: '001533888501916@user.qikan.com'},
    {username: '幼齿控', email: '001533889840882@user.qikan.com'},
    {username: '快闪碗里来', email: '001533890179847@user.qikan.com'},
    {username: '我要变成大瘦子', email: '001533891518812@user.qikan.com'},
    {username: '屁股大坐的稳', email: '001533892857776@user.qikan.com'},
    {username: '肚子兔子', email: '001533893196740@user.qikan.com'},
    {username: '怪你过分美丽', email: '001533894535704@user.qikan.com'},
    {username: '你就像烈酒', email: '001533895874667@user.qikan.com'},
    {username: '拖延症患者', email: '001533896213629@user.qikan.com'},
    {username: '我说我不知道', email: '001533897552591@user.qikan.com'},
    {username: 'alexiachen', email: '001533898891553@user.qikan.com'},
    {username: '棉花糖甜甜甜甜', email: '001533899230515@user.qikan.com'},
    {username: '小王子的面包树 ', email: '001533900569475@user.qikan.com'},
    {username: '拔丝红薯大赢家', email: '001533901908436@user.qikan.com'},
    {username: '别扭的鸵鸟', email: '001533902247396@user.qikan.com'},
    {username: '芋头比我美', email: '001533903586356@user.qikan.com'},
    {username: '卡罗莱大魔王', email: '001533904925315@user.qikan.com'},
    {username: '困伐醒呃懒破驹', email: '001533905264273@user.qikan.com'},
    {username: '冲田总悟', email: '001533906603232@user.qikan.com'},
    {username: '乌云乌云快走开', email: '001533907942190@user.qikan.com'},
    {username: '梅长苏的玉冠', email: '001533908281147@user.qikan.com'},
    {username: '谁家那小谁', email: '001533909620104@user.qikan.com'},
    {username: '奥黛丽·和平', email: '001533910959060@user.qikan.com'},
    {username: '清热解毒板蓝根', email: '001533911298017@user.qikan.com'},
    {username: '蕾丝李', email: '001533912636972@user.qikan.com'},
    {username: '平胸少女', email: '001533913975927@user.qikan.com'},
    {username: '奶酪永动机', email: '001533914314882@user.qikan.com'},
    {username: '大婶来买豆沙包', email: '001533915653837@user.qikan.com'},
    {username: '爱ci布丁的布丁', email: '001533916992790@user.qikan.com'},
    {username: '你们都没有我美', email: '001533917331744@user.qikan.com'},
    {username: '凌晨喝咖啡', email: '001533918670697@user.qikan.com'},
    {username: '一胖二白', email: '001533919009650@user.qikan.com'},
    {username: '撒西不理', email: '001533920348602@user.qikan.com'},
    {username: '阿花小姐', email: '001533921687553@user.qikan.com'},
    {username: '尊小肥', email: '001533922026505@user.qikan.com'},
    {username: '周二围', email: '001533923365456@user.qikan.com'},
    {username: ' 悟空的金箍棒', email: '001533924704406@user.qikan.com'},
    {username: 'kkkkkkkira ', email: '001533925043356@user.qikan.com'},
    {username: '姨妈的鸭', email: '001533926382306@user.qikan.com'},
    {username: ' 貌美的小黄鸡', email: '001533927721255@user.qikan.com'},
    {username: ' 喝醉酒的蚊子', email: '001533928060203@user.qikan.com'},
    {username: '夜夜夜夜', email: '001533929399152@user.qikan.com'},
    {username: '橙子子子子', email: '001533930738099@user.qikan.com'},
    {username: 'Geronimo', email: '001533931077047@user.qikan.com'},
    {username: ' 远在远方的风', email: '001533932415994@user.qikan.com'},
    {username: '牛先生的鹿小姐', email: '001533933754940@user.qikan.com'},
    {username: ' HammerWong', email: '001533934093886@user.qikan.com'},
    {username: '菇凉身边很凉快', email: '001533935432832@user.qikan.com'},
    {username: 'Summer Melody', email: '001533936771777@user.qikan.com'},
    {username: '吼吼吼菜菜大包', email: '001533937110722@user.qikan.com'},
    {username: ' 蛋黄派讲故事', email: '001533938449666@user.qikan.com'},
    {username: ' 一天不犯傻比我就会死掉', email: '001533939788610@user.qikan.com'},
    {username: '哲学家吉他手', email: '001533940127553@user.qikan.com'},
    {username: '列宁的奶猫', email: '001533941466496@user.qikan.com'},
    {username: 'KK_en_france', email: '001533942805439@user.qikan.com'},
    {username: ' cherieleeeeee', email: '001533943144381@user.qikan.com'},
    {username: '沉沦的mojito', email: '001533944483323@user.qikan.com'},
    {username: ' 宇宙大魔王', email: '001533945822264@user.qikan.com'},
    {username: 'La Habana', email: '001533946161205@user.qikan.com'},
    {username: '脸大了怎么样', email: '001533947500145@user.qikan.com'},
    {username: ' 煲汤的高压锅', email: '001533948839085@user.qikan.com'},
    {username: '哼一首歌给哈尼', email: '001533949178025@user.qikan.com'}
]
for line in fr:
    user=line.split('##')
    nickname=user[0]
    password=user[1]
    email=user[2].replace(' ','')
    intro=user[3]
    website=user[4].replace('\n','')
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
    list0 =('%s,%s,%s\n') % (email,userid,token)  
   
 
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