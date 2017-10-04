#pdf("cpu_load.pdf")
#pdf("mem_usage.pdf")

fpe<-read.table("PerUserPosCoeffSeverity.txt", sep=",")
plot_colors <- c("red","blue","black")


names(fpe)<-c("userid", "coeff", "posPercentage", "posSeverity")


xrange <- range(fpe$coeff) 
yrange <- range(fpe$posPercentage) 


plot(xrange,yrange, type="n", xlab="Local Clustering Coefficient", ylab="positive percentage of posts", cex.lab=1.5,cex.axis=1.5)
lines(fpe$coeff, fpe$posPercentage, type="p", lwd=3,lty=1, col="red", pch=1,cex=1.5)



#dev.off()