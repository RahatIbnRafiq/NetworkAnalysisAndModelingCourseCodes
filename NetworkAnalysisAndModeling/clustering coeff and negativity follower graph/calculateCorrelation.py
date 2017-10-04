

import math


def calculateCorrelation(l1,l2):
    sum1 = 0.0
    sum2 = 0.0
    mean1 = 0.0
    mean2 = 0.0
    for l in l1:
        sum1 = sum1 + float(l)
    for l in l2:
        sum2 = sum2 + float(l)

    mean1 = float(sum1/float(len(l1)))
    mean2 = float(sum2/float(len(l2)))


    diff1 = []
    diff2 = []
    squaresum1 = 0.0
    squaresum2 = 0.0
    for l in l1:
        diff = 0.0
        diff = float(l) - mean1
        diff1.append(diff)
        diff = diff*diff
        squaresum1 = squaresum1 + diff
    for l in l2:
        diff = 0.0
        diff = float(l) - mean2
        diff2.append(diff)
        diff = diff*diff
        squaresum2 = squaresum2 + diff

    count = 0
    combinedSum = 0.0
    while count < len(diff1):
        value1 = float(diff1[count])
        value2 = float(diff2[count])
        combinedSum = combinedSum + float(value1*value2)
        count = count + 1

    value = math.sqrt(float(squaresum1)*float(squaresum2))
    coValue = float(float(combinedSum)/float(value))
    print coValue
    
        
        



f = open("PerUserNegCoeffSeverity.txt","r")

coeff = []
reciprocity = []
posPer = []
posSev = []
negPer = []
negSev = []

for line in f:
    line = line.strip()
    values = line.split(",")
    coeff.append(values[1])
    negPer.append(values[2])
    negSev.append(values[3])
f.close()


calculateCorrelation(coeff,negPer)
calculateCorrelation(coeff,negSev)

