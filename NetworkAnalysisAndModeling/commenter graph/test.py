


class Post:
    def __init__(self,postid,comment,commenterid,commentername):
        self.postid = postid
        self.comment = comment
        self.commenterid=commenterid
        self.commentername=commentername

class User:
    def __init__(self,userid,posts):
        self.userid = userid
        self.posts = posts


def getPostFromPostList(postid):
    for post in posts:
        if str(post.postid) == str(postid):
            return post

def getPostIDs(owner):
    for user in users:
        if str(user.userid) == str(owner):
            return user.posts

def getComments(post,commenterid):
    count = len(post.comment)
    commentList = []
    while count > 0:
        commenter = post.comment[count-1] 
        count = count -1


f = open("postids_for_100_users.txt","r")
line = f.readline()
line = line.strip()
index = line.index(":")
userid = line[index+1:]
posts = []
users = []
for line in f:
    line = line.strip()
    if "For the user:" in line:
        u = User(userid,posts)
        users.append(u)
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
comments = []
commenterids = []
commenternames = []
posts = []
for line in f:
    line = line.strip()
    if "For the post:" in line:
        p = Post(postid,comments,commenterids,commenternames)
        posts.append(p)
        comments = []
        commenterids = []
        commenternames = []
        index = line.index(":")
        postid = line[index+1:]
    elif "comment:" in line:
        index = line.index(":")
        comment = line[index+1:]
        comments.append(comment)
    elif "userId:" in line:
        index = line.index(":")
        commenterid = line[index+1:]
        commenterids.append(commenterid)
    elif "username:" in line:
        index = line.index(":")
        commentername = line[index+1:]
        commenternames.append(commentername)
f.close()



f = open("OwnerCommenterGraphMoreThanSixComment.txt","r")

for line in f:
    line = line.strip()
    values = line.split(",")
    commenter = values[0]
    owner = values[1]
    postids = getPostIDs(owner)
    for postid in postids:
        post = getPostFromPostList(postid)
        commentList = getComments(post,commenterid)
