#readvgsales
library(dplyr)
vgsales = read.csv('pandas/vgsales.csv', stringsAsFactors = F)

ps3 = 
  vgsales %>% 
  dplyr::filter(Platform == 'PS3') %>% 
  dplyr::filter(Year != "N/A") %>% 
  dplyr::select(-Rank) %>% 
  dplyr::arrange(Year, Name)
which(is.na(ps3))

write.csv(ps3, file='pandas/ps3.csv', row.names = F)

