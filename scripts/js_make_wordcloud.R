#/usr/bin/env Rscript

## Load libraries

library("argparse")
library("tm")
library("wordcloud")
library("wordcloud2")
library("RColorBrewer")
library("wesanderson")

parser <- ArgumentParser(description="This script make wordclouds based on text input")
parser$add_argument("-t", "--text", help="text file")
parser$add_argument("-o", "--output", help="Output to save")
args <- parser$parse_args()
print(args)


text <- readLines(args$text)

docs <- Corpus(VectorSource(text))

dtm <- TermDocumentMatrix(docs)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 10)

pdf(file=args$output)
set.seed(1234)

## for wordcloud
#pal <- wes_palette("IsleofDogs1", 6, type = "discrete")
pal <- wes_palette("Darjeeling1", 5, type = "discrete")
#pal <- wes_palette("Darjeeling2", 5, type = "discrete")
#pal <- wes_palette("Cavalcanti1", 5, type = "discrete")

wordcloud(words = d$word, freq = d$freq, min.freq = 1,
          max.words=150, random.order=FALSE, rot.per=0.2,
          colors=pal)


dev.off()
