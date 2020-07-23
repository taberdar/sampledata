#readvgsales
library(dplyr)
vgsales = read.csv('pandas/vgsales.csv', stringsAsFactors = F)

ps3 = vgsales %>% dplyr::filter(Platform == 'PS3') %>% dplyr::filter(Year != "N/A")
which(is.na(ps3))

write.csv(ps3, file='pandas/ps3.csv', row.names = F)

