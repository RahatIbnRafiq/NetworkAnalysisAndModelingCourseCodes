

class User:
    def __init__(self,userid,coeff):
        self.userid = userid
        self.coeff = coeff


def getUser(userid):
    for user in users:
        if str(user.userid) == str(userid):
            return user

f = open("clustetring_coefficient_Full_Graph_nodes_following1.txt","r")

users = []
for line in f:
    line = line.strip()
    values = line.split(",")
    u = User(values[0],values[1])
    users.append(u)
f.close()

f = open("Per_User_negativity.txt","r")
g = open("PerUserNegCoeffSeverity.txt","w")

for line in f:
    line = line.strip()
    values = line.split(",")
    userid =  values[0]
    user = getUser(userid)
    g.write(str(userid)+","+str(user.coeff)+","+str(values[1]+","+str(values[2])+"\n"))
    
f.close()
g.close()
