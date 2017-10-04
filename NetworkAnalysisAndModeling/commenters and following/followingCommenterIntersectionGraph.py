
class User:
    def __init__(self,userid,following,posts):
        self.userid = userid
        self.following = following
        self.posts = posts

class Post:
    def __init__(self,postid,commenters,userid):
        self.postid = postid
        self.userid = userid
        self.commenters = commenters
    
def getUser(userid):
    for user in users:
        if str(user.userid) == str(userid):
            return user
    return 0

def getFollowingForPost(postid):
    for user in users:
        for post in user.posts:
            if str(post) == str(postid):
                return user.following

users = []
posts = []
f = open("vine_user_following_100.txt","r")
for line in f:
    line = line.strip()
    values = line.split(",")
    userid = values[0]
    followingid = values[1]
    user = getUser(userid)
    if user == 0:
        following = []
        following.append(followingid)
        u = User(userid,following,posts)
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


f = open("PostsWithCommentersAndOwners.txt","r")
postList = []
for line in f:
    line = line.strip()
    values = line.split(",")
    posts = []
    postid = values[0]
    userid = values[len(values)-1]
    for post in values[1:len(values)-1]:
        posts.append(post)
    p = Post(postid,posts,userid)
    postList.append(p)
f.close()



f = open("followingCommenterIntersectionGraph.txt","w")
for post in postList:
    try:
        following = getFollowingForPost(post.postid)
        commenters = list(post.commenters)
        commenters = set(commenters)
        following = set(following)
        commonusers = list(set(following).intersection(commenters))
        if len(commonusers) > 0:
            for user in commonusers:
                f.write(str(post.userid)+","+str(user)+"\n")

    except Exception:
        continue
f.close()
 



