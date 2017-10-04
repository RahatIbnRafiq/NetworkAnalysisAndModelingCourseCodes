#pdf("cpu_load.pdf")
#pdf("mem_usage.pdf")

fpe<-read.table("community_graph_data_follower.txt", sep=",")
plot_colors <- c("red","blue","black")


names(fpe)<-c("community", "coeff", "reciprocity", "posPercentage" , "posSeverity", "negPercentage", "negSeverity")


xrange <- range(fpe$reciprocity) 
yrange <- range(fpe$posSeverity) 


plot(xrange,yrange, type="n", xlab="reciprocity", ylab="positive severity of posts", cex.lab=1.5,cex.axis=1.5)
lines(fpe$reciprocity, fpe$posSeverity, type="p", lwd=3,lty=1, col="red", pch=1,cex=1.5)



#dev.off()