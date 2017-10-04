

f = open("community_graph_data_following.txt","r")
coeff = []
reci = []
posper = []
possev = []
negper = []
negsev=[]

for line in f:
    line = line.strip()
    values = line.split(",")
    coeff.append(values[1])
    reci.append(values[2])
    posper.append(values[3])
    possev.append(values[4])
    negper.append(values[5])
    negsev.append(values[6])
f.close()


count = 0

g = open("diff.txt","w")
while count < 18:
    try:
        perRatio = float(float(posper[count])/float(negper[count]))
        sevRatio = float(float(possev[count])/float(negsev[count]))
        g.write(str(coeff[count])+","+str(reci[count])+","+str(perRatio)+","+str(sevRatio)+"\n")
        count = count + 1
    except Exception:
        count = count + 1
        continue
g.close()  
