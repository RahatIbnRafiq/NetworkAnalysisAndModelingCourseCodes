


def computeNegativity(comments):
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
    f = open("negativity_other.txt","a")
    f.write(str(totalComments)+","+str(totalNegComment)+","+str(totalNegWord)+"\n")
    f.close()
            

negword = []
f = open("new_neg_list1.csv","r")

for line in f:
    line = line.strip()
    negword.append(line)
f.close()

f = open("otherComment.txt","r")

comments = []
for line in f:
    line = line.strip()
    comments.append(line)
f.close()
computeNegativity(comments)
