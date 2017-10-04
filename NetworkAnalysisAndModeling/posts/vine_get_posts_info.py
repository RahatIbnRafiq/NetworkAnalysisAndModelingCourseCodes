import sys, os
sys.path.append('/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1]))
import urllib2

import vinepy
import json
import datetime
import time

def getPost(vine,user_id,page):
    posts = vine.get_user_timeline(user_id=user_id,size='20',page = page)
    return posts

def parsePostData(postList,g):
    for item in postList:
        for post in item:
            for i in post:
                try:
                    g.write(str(i)+":"+str(post[i])+"\n")
                except Exception as ex:
                    try:
                        g.write(str(i)+":"+str(post[i].encode('utf-8'))+"\n")   
                    except Exception:
                        continue
            g.write("__________________________"+"\n")
        

print "Get Recent 30 Posts!"
password = ""
g = open("Pass.txt","r")
for line in g:
    password = line
    break
vine = vinepy.API(username='rahatibnrafiq@gmail.com', password=password)
g.close()
f = open("vine_users_sampled_4000.txt","r")
g = open("vine_users_post_meta_data_4000_30.txt","w")
usersDone = 0
for line in f:
    line = line.strip()
    userId =  line
    g.write("For the user:"+str(userId)+"\n")
    postList = []
    try:
        posts = getPost(vine,userId,'1')
    except Exception as e:
        if "permission" in str(e):
            print "private user"
            continue
        if "try again later" in str(e):
            print "going to sleep"
            print datetime.datetime.now()
            time.sleep(900)
            print "getting up from sleep"
            posts = getPost(vine,userId,'1')
    postList.append(posts)
    parsePostData(postList,g)
    usersDone = usersDone + 1
    print str(usersDone)+" users done!"
    
f.close()
g.close()
