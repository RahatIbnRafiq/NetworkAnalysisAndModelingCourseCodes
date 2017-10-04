class User:
    def __init__(self,userid,following,follower,posts):
        self.userid = userid
        self.follower = follower
        self.following = following
        self.posts = posts

class Post:
    def __init__(self,postid,commenters,commenttexts):
        self.postid= postid
        self.commenters = commenters
        self.commenttexts = commenttexts


def getUser(userid):
    for user in users:
        if str(user.userid) == str(userid):
            return user
    return 0

def getUserByPostId(postid):
    for user in users:
        for post in user.posts:
            if str(post) == str(postid):
                return user
    return 0

def getFollowingForPost(postid):
    for user in users:
        for post in user.posts:
            if str(post) == str(postid):
                return user.following
            
def getFollowerForPost(postid):
    for user in users:
        for post in user.posts:
            if str(post) == str(postid):
                return user.follower

users = []
posts = []
f = open("vine_user_follower_100.txt","r")
for line in f:
    line = line.strip()
    values = line.split(",")
    userid = values[1]
    followerid = values[0]
    user = getUser(userid)
    if user == 0:
        follower = []
        following = []
        follower.append(followerid)
        u = User(userid,following,follower,posts)
        users.append(u)
    else:
        user.follower.append(followerid)
    
f.close()


f = open("vine_user_following_100.txt","r")
for line in f:
    line = line.strip()
    values = line.split(",")
    userid = values[0]
    followingid = values[1]
    user = getUser(userid)
    if user == 0:
        follower = []
        following = []
        following.append(followingid)
        u = User(userid,following,follower,posts)
        users.append(u)
    else:
        user.following.append(followingid)
    
f.close()




f = open("postids_for_100_users.txt","r")

line = f.readline()
line = line.strip()
index = line.index(":")
userid = line[index+1:]
for line in f:
    line = line.strip()
    if "For the user:" in line:
        user = getUser(userid)
        user.posts = posts
        posts = []
        index = line.index(":")
        userid = line[index+1:]
        
    else:
        index = line.index(":")
        postid = line[index+1:]
        posts.append(postid)
f.close()


f = open("comments_for_100_from_compressed.txt","r")

line = f.readline()
line = line.strip()
index = line.index(":")
postid = line[index+1:]

postList = []
commenters = []
commenttexts = []
p = Post(postid,commenters,commenttexts)
for line in f:
    line = line.strip()
    if "userId:" in line:
        index = line.index(":")
        commenters.append(line[index+1:])
    elif "comment:" in line:
        index = line.index(":")
        commenttexts.append(line[index+1:])
    elif "For the post:" in line:
        postList.append(p)
        index = line.index(":")
        postid = line[index+1:]
        commenters = []
        commenttexts = []
        p = Post(postid,commenters,commenttexts)            
f.close()
g = open("followerComment.txt","w")
h = open("followingComment.txt","w")
count = 0


count = 0
for post in postList:
    postid =  post.postid
    print postid
    user = getUserByPostId(postid)
    if user == 0:
        continue
    userid = user.userid
    followers = user.follower
    followings = user.following
    commenters = post.commenters
    loop = len(post.commenttexts)-1
    if loop == -1:
        continue
    while loop > -1:
        try:
            c = post.commenters[loop]
            ct = post.commenttexts[loop]
            if c in followers:
                g.write(str(ct)+"\n")
            if c in followings:
                h.write(str(ct)+"\n")
            loop = loop - 1
        except Exception as e:
            print len(post.commenters)
            print len(post.commenttexts)
            print loop
            print str(e)
            loop = loop -1
            continue
        
print count

g.close()
    
