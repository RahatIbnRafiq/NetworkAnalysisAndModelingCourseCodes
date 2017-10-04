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




f = open("following_userid_100.txt","r")
followers = []
for line in f:
    line = line.strip()
    values = line.split(",")
    followers.append(values[0])
f.close()

communities = []
f = open("community_following_leading_eigenvector_100.txt","r")
line = f.readline()
line = f.readline()
for line in f:
    line = line.strip()
    communities.append(line)
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

print len(postList)
count = 0
g = open("commentsPerCommunityFollowing.txt","w")
for comm in communities:
    count = count + 1
    g.write("comments for community:"+str(count)+"\n")
    values = comm.split(",")
    communityFollowers = []
    for index in values[0:len(values)-1]:
        communityFollowers.append(followers[int(index)])
    for post in postList:
        loop = len(post.commenttexts)-1
        if loop == -1:
            continue
        while loop > -1:
            try:
                c = post.commenters[loop]
                ct = post.commenttexts[loop]
                if c in communityFollowers:
                    g.write(str(ct)+"\n")
                loop = loop - 1
            except Exception as e:
                print len(post.commenters)
                print len(post.commenttexts)
                print loop
                print str(e)
                loop = loop -1
                continue 
g.close()
