#pdf("cpu_load.pdf")
#pdf("mem_usage.pdf")

fpe<-read.table("PerUserNegCoeffSeverity.txt", sep=",")
plot_colors <- c("red","blue","black")


names(fpe)<-c("userid", "coeff", "negPercentage", "negSeverity")


xrange <- range(fpe$coeff) 
yrange <- range(fpe$negSeverity) 


plot(xrange,yrange, type="n", xlab="Local Clustering Coefficient", ylab="negative severity of posts", cex.lab=1.5,cex.axis=1.5)
lines(fpe$coeff, fpe$negSeverity, type="p", lwd=3,lty=1, col="red", pch=1,cex=1.5)



#dev.off()