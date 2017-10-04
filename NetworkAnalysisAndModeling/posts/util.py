import json 
f = open("Post_meta_100_users.txt","r")
g = open("post_info_for_100_users.txt","w")


for line in f:
    line = line.strip()
    if "json" in line:
        d = json.loads(line[5:])
        likes = d["likes"]["count"]
        comments = d["comments"]["count"]
        loops = d["loops"]["count"]
        postId = d["postId"]
        verified = d["verified"]
        g.write(str(postId)+","+str(likes)+","+str(comments)+","+str(loops)+","+str(verified)+"\n")

f.close()
g.close()

