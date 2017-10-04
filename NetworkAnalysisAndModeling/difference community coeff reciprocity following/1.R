#pdf("cpu_load.pdf")
#pdf("mem_usage.pdf")

fpe<-read.table("diff.txt", sep=",")
plot_colors <- c("red","blue","black")


names(fpe)<-c("coeff", "reciprocity", "percentageRatio", "severityRatio")


xrange <- range(fpe$reciprocity) 
yrange <- range(fpe$percentageRatio) 


plot(xrange,yrange, type="n", xlab="Reciprocity", ylab="positive negative percentage ratio", cex.lab=1.5,cex.axis=1.5)
lines(fpe$reciprocity, fpe$percentageRatio, type="p", lwd=3,lty=1, col="red", pch=1,cex=1.5)



#dev.off()