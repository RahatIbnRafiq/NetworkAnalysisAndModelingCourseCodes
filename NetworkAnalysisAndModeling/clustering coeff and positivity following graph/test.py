

class User:
    def __init__(self,userid,posts):
        self.userid = userid
        self.posts = posts
class Post:
    def __init__(self,postid,totalComment,totalNegComment,totalNegWord):
        self.postid = postid
        self.totalComment =totalComment
        self.totalNegComment=totalNegComment
        self.totalNegWord =totalNegWord


def getPost(postid):
    for post in posts:
        if str(post.postid) == str(postid):
            return post

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

f = open("positivity_comments_for_100.txt","r")
posts = []

for line in f:
    line = line.strip()
    values = line.split(",")
    post = Post(values[0],values[1],values[2],values[3])
    posts.append(post)
f.close()
print len(posts)


f = open("Per_User_positivity.txt","w")

for user in users:
    totalComment = 0
    totalNegComment = 0
    totalNegWord = 0
    for postid in user.posts:
        post = getPost(postid)
        totalComment = totalComment + int(post.totalComment)
        totalNegComment = totalNegComment + int(post.totalNegComment)
        totalNegWord = totalNegWord + int(post.totalNegWord)
    negCommentPercentage = float(float(totalNegComment)/float(totalComment))
    severityPercentage = float(float(totalNegWord)/float(totalNegComment))
    f.write(str(user.userid)+","+str(negCommentPercentage)+","+str(severityPercentage)+"\n")
f.close()
    
        


