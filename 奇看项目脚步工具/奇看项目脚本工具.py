import pymongo,time,datetime

import urllib
con = pymongo.MongoClient('192.168.8.13', 27017)

#class User:
#    nickName=''
#    webSite=''
#    intro=''
#mydb=con.master
#users=mydb.users.find()

#user=User()


url = 'http://plus.qikan.com/api/sys/gettimestamp'
with urllib.request.urlopen(url) as response:
   result = response.read()

print (result)
#print(user)
#for user in users:
#    print(user['_id']) 