#pdf("cpu_load.pdf")
#pdf("mem_usage.pdf")

fpe<-read.table("commentsData.txt", sep=",")
plot_colors <- c("red","blue","black")


names(fpe)<-c("numberOfComments", "posPercentage", "posSeverity", "negPercentage" , "negSeverity")


xrange <- range(fpe$numberOfComments) 
yrange <- range(fpe$negPercentage) 


plot(xrange,yrange, type="n", xlab="Number Of Comments", ylab="negative percentage of posts", cex.lab=1.5,cex.axis=1.5)
lines(fpe$numberOfComments, fpe$negPercentage, type="p", lwd=3,lty=1, col="red", pch=1,cex=1.5)



#dev.off()