######Accuracy#######
rm(list=ls())

#setwd(commandArgs(TRUE)[1])

solution <- read.csv(file="C:/Users/admin/Documents/Cax/Contest_characters/SolutionFile_characters.csv", stringsAsFactors=TRUE,header=TRUE)
submission<- read.csv(file="C:/Users/admin/Desktop/Book2.csv", stringsAsFactors=TRUE,header=TRUE)

mer_all <-merge(x = solution, y = submission, by = "Filename", all.x = TRUE)

public<- mer_all[ which(mer_all$Label=='public'), ]
private<- mer_all[ which(mer_all$Label=='private'), ]

private_score <- sum(ifelse(private[,2] == private[,4],1,0))/nrow(private)
#write.csv(private_score, "C:/Users/admin/Documents/Cax/Contest_characters/file.csv", row.names=FALSE)

public_score <- sum(ifelse(public[,2] == public[,4],1,0))/nrow(public)
#write.csv(public_score, "C:/Users/admin/Documents/Cax/Contest_characters/file_public.csv", row.names=FALSE)
