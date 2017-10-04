

f = open("community_following_leading_eigenvector_100_global_clustering.txt","r")
g = open("negativity_per_community_following.txt","r")
h = open("positivity_per_community_following.txt","r")
i = open("following_reciprocity_for_communities_leading_eigenvector_100.txt","r")
j = open("community_graph_data_following.txt","w")


for line1 in f:
    line1 = line1.strip()
    line2 = g.readline().strip()
    line3 = h.readline().strip()
    line4 = i.readline().strip()
    value1 = line1.split(",")
    community = value1[0]
    coeff = value1[1]
    value2 = line2.split(",")
    print value2
    totalComment = value2[1]
    totalNegComment = value2[2]
    totalNegWord = value2[3]
    try:
        negPercentage = float(float(totalNegComment)/float(totalComment))
    except Exception:
        negPercentage = 0
    try:
        negSeverity = float(float(totalNegWord)/float(totalNegComment))
    except Exception:
        negSeverity = 0
    value3 = line3.split(",")
    totalComment = value3[1]
    totalPosComment = value3[2]
    totalPosWord = value3[3]
    try:
        posPercentage = float(float(totalPosComment)/float(totalComment))
    except Exception:
        posPercentage = 0
    try:
        posSeverity = float(float(totalPosWord)/float(totalPosComment))
    except Exception:
        posSeverity = 0
    value4 = line4.split(",")
    reciprocity = value4[1]

    j.write(str(community)+","+str(coeff)+","+str(reciprocity)+","+str(posPercentage)+","+str(posSeverity)+","+str(negPercentage)+","+str(negSeverity)+"\n")
f.close()
g.close()
h.close()
i.close()
j.close()
