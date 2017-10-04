


def computeNegativity(comments,community):
    totalComments = len(comments)
    totalNegComment = 0
    totalNegWord = 0
    for comment in comments:
        found = 0
        values = comment.split(" ")
        for word in values:
            if word in negword:
                found = 1
                totalNegWord = totalNegWord + 1
        if found == 1:
            totalNegComment = totalNegComment + 1
    f = open("positivity_per_community_follower.txt","a")
    f.write(str(community)+","+str(totalComments)+","+str(totalNegComment)+","+str(totalNegWord)+"\n")
    f.close()
            

negword = []
f = open("new_pos_list1.csv","r")

for line in f:
    line = line.strip()
    negword.append(line)
f.close()

f = open("commentsPerCommunityFollower.txt","r")

comments = []
line = f.readline()
line = line.strip()
index = line.index(":")
community = line[index+1:]

for line in f:
    line = line.strip()
    if "comments for community:" in line:
        computeNegativity(comments,community)
        comments = []
        index = line.index(":")
        community = line[index+1:]
    else:
        comments.append(line)
f.close()
