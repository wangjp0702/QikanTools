import pymongo,time,datetime
con = pymongo.MongoClient('192.168.8.13', 27017)

mydb=con.master
users=mydb.users.find()

for user in users:
    print(user['_id'])