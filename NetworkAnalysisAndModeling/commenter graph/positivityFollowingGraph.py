


def computeNegativityPositivity(comments):
    totalComments = len(comments)
    totalNegComment = 0
    totalNegWord = 0
    totalPosComment = 0
    totalPosWord = 0
    for comment in comments:
        found = 0
        values = comment.split(" ")
        for word in values:
            if word in negword:
                found = 1
                totalNegWord = totalNegWord + 1
        if found == 1:
            totalNegComment = totalNegComment + 1
    for comment in comments:
        found = 0
        values = comment.split(" ")
        for word in values:
            if word in posword:
                found = 1
                totalPosWord = totalPosWord + 1
        if found == 1:
            totalPosComment = totalPosComment + 1
    posPercentage = float(float(totalPosComment)/float(totalComments))
    posSeverity = float(float(totalPosWord)/float(totalPosComment))
    negPercentage = float(float(totalNegComment)/float(totalComments))
    negSeverity = float(float(totalNegWord)/float(totalNegComment))
    f = open("CommentsData.txt","a")
    f.write(str(7)+","+str(posPercentage)+","+str(posSeverity)+","+str(negPercentage)+","+str(negSeverity)+"\n")
    f.close()
            

negword = []
f = open("new_neg_list1.csv","r")

for line in f:
    line = line.strip()
    negword.append(line)
f.close()

posword = []
f = open("new_pos_list1.csv","r")

for line in f:
    line = line.strip()
    posword.append(line)
f.close()

f = open("PerPostSevenCommentsCommenterscomments.txt","r")

comments = []
for line in f:
    line = line.strip()
    comments.append(line)
f.close()
computeNegativityPositivity(comments)
