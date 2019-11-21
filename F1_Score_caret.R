#install.packages('caret', dependencies = TRUE)
#library(MLmetrics)
library(caret)
solution <- read.csv(file="C:/Users/admin/Documents/Cax/contest_mortage/Contest_Mortgage/CAX_SolutionFile.csv", stringsAsFactors=TRUE,header=TRUE)
submission<- read.csv(file="C:/Users/admin/Desktop/practice_problems/mortgage_new/1_not_funded.csv",stringsAsFactors = TRUE , header = TRUE)

solution <- read.csv(file=commandArgs(TRUE)[2], stringsAsFactors=TRUE,header=TRUE)
submission<- read.csv(file=commandArgs(TRUE)[3], stringsAsFactors=TRUE,header=TRUE)

mer_all <-merge(x = solution, y = submission, by = "Unique_ID", all.x = TRUE)

public<- mer_all[ which(mer_all$Label=='public'), ]
private<- mer_all[ which(mer_all$Label=='private'), ]



###################calculating Fscore for public leader board ###################
y2 = public[,2]
predictions  = public[,4]

accuracy = Accuracy(predictions, y2)
ConfusionMatrix(predictions, y2)
public_score = F1_Score(predictions, y2, positive = "NOT FUNDED")

write.csv(public_score, commandArgs(TRUE)[5], row.names=FALSE)

###################calculating Fscore for private leader board ###################

y1 = private[,2]
predictions1  = private[,4]

accuracy = Accuracy(predictions1, y1)
ConfusionMatrix(predictions1, y1)
private_score = F1_Score(predictions1, y1, positive = NULL)

write.csv(private_score, commandArgs(TRUE)[4], row.names=FALSE)

