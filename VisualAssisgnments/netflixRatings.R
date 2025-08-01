library(ggplot2)
dataValue <- read.csv("/Users/ndubisiekeh/Documents/GitHub/NexFordProgramming/VisualAssisgnments/Netflix_shows_movies.csv")
dataValue <- dataValue[!is.na(dataValue$rating), ]

ggplot(dataValue, aes(x = rating)) +
  geom_bar(fill = "steelblue") +
  labs(title = "Ratings Distribution (R)", x = "Rating", y = "Count") +
  theme_minimal()