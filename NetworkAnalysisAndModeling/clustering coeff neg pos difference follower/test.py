

f = open("PerUserNegCoeffSeverity.txt","r")
g = open("PerUserPosCoeffSeverity.txt","r")
h = open("PerUserCoeffDifference.txt","w")

for line in f:
    line = line.strip()
    values = line.split(",")
    userid = values[0]
    coeff= float(values[1])
    negPercentage = float(values[2])
    negSeverity = float(values[3])
    line = g.readline()
    line = line.strip()
    values = line.split(",")
    posPercentage = float(values[2])
    posSeverity = float(values[3])

    percentageRatio = float(negPercentage/posPercentage)
    severityRatio = float(negSeverity/posSeverity)

    h.write(str(userid)+","+str(coeff)+","+str(percentageRatio)+","+str(severityRatio)+"\n")

    print userid
    print coeff
    print percentageRatio
    print severityRatio
f.close()
g.close()
h.close()
