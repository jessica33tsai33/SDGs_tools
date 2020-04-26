
raw<-read.csv("C://Users//Tsai Jessica//NTU//sdlab//SDGs_tools//Japan_DB_Colour_V3.0.csv", header=FALSE, sep=",", stringsAsFactors=FALSE, na.strings="")

pair<-matrix(nrow=169*169,ncol=2)

x = 1
for(g in 2:170){
  for(h in 2:170){
    if(is.na(raw[g,h])==FALSE){
      pair[x,1] <- raw[g,1]
      pair[x,2] <- raw[1,h]
      x = x + 1
    }
  }
}
