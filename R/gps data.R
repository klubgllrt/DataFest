# Mamie Trigg
# Data Hacks 
# 4/5/19 7pm, initial look at the data

setwd("/Volumes/GoogleDrive/My Drive/DataFest 2019/data-for-datafest-2019/Original DataSets")

library(dplyr)
library(tidyverse)
library(readxl)
library(ggplot2)

games <- read.csv(file="games.csv", na.strings = "NA")
gps <-  read.csv(file="gps.csv", na.strings = "NA")
rpe <- read.csv(file="rpe.csv", na.strings = "NA")
wellness <- read.csv(file="wellness.csv", na.strings = "NA")

# can sample data, here is a sampled 10000 points.
sample_gps <- sample_n(gps, 10000)

summary_gps <- gps %>% group_by(GameID, Half, PlayerID, Time) %>% summarise(mean_speed=mean(Speed))
summary_gps_perplayer <- gps %>% group_by(GameID, Half, PlayerID) %>% summarise(mean_speed=mean(Speed))
summary_gps <- gps %>% group_by(PlayerID) %>% summarise(mean_speed=mean(Speed), max_speed=max(Speed))

gps_Game1_Player2 <- read_excel("/Volumes/GoogleDrive/My Drive/DataFest 2019/MT/MT Excel Sheets/gps_GameID_PlayerID2.xlsx")
gps_Game1_Player2_byTime <- gps_Game1_Player2 %>% group_by(GameClock) %>% summarise(avgSpeed=mean(Speed))

# data sets for each player
gps_Player1 <- gps %>% filter(PlayerID==1)
gps_Player2 <- gps %>% filter(PlayerID==2)
gps_Player3 <- gps %>% filter(PlayerID==3)
gps_Player4 <- gps %>% filter(PlayerID==4)
gps_Player5 <- gps %>% filter(PlayerID==5)
gps_Player6 <- gps %>% filter(PlayerID==6)
gps_Player7 <- gps %>% filter(PlayerID==7)
gps_Player8 <- gps %>% filter(PlayerID==8)
gps_Player9 <- gps %>% filter(PlayerID==9)
gps_Player10 <- gps %>% filter(PlayerID==10)
gps_Player11 <- gps %>% filter(PlayerID==11)
gps_Player12 <- gps %>% filter(PlayerID==12)
gps_Player13 <- gps %>% filter(PlayerID==13)
gps_Player14 <- gps %>% filter(PlayerID==14)
gps_Player15 <- gps %>% filter(PlayerID==15)
gps_Player16 <- gps %>% filter(PlayerID==16)
gps_Player17 <- gps %>% filter(PlayerID==17)
gps_Player18 <- gps %>% filter(PlayerID==18)
gps_Player19 <- gps %>% filter(PlayerID==19)
gps_Player20 <- gps %>% filter(PlayerID==20)
gps_Player21 <- gps %>% filter(PlayerID==21)

# Datasets for Games
gps_Game1 <- gps %>% filter(GameID==1)
gps_Game2 <- gps %>% filter(GameID==2)
gps_Game3 <- gps %>% filter(GameID==3)
write.csv(gps_Game3,"/Volumes/GoogleDrive/My Drive/DataFest 2019/MT/MT R/gps_Game3.csv")

gps_Game4 <- gps %>% filter(GameID==4)
gps_Game5 <- gps %>% filter(GameID==5)
gps_Game6 <- gps %>% filter(GameID==6)
gps_Game7 <- gps %>% filter(GameID==7)
gps_Game8 <- gps %>% filter(GameID==8)
gps_Game9 <- gps %>% filter(GameID==9)
gps_Game10 <- gps %>% filter(GameID==10)
gps_Game11 <- gps %>% filter(GameID==11)
gps_Game12 <- gps %>% filter(GameID==12)
gps_Game13 <- gps %>% filter(GameID==13)
gps_Game14 <- gps %>% filter(GameID==14)
gps_Game15 <- gps %>% filter(GameID==15)
gps_Game16 <- gps %>% filter(GameID==16)
gps_Game17 <- gps %>% filter(GameID==17)
gps_Game18 <- gps %>% filter(GameID==18)
gps_Game19 <- gps %>% filter(GameID==19)
write.csv(gps_Game19,"/Volumes/GoogleDrive/My Drive/DataFest 2019/MT/MT R/gps_Game19.csv")

gps_Game19filtered <- gps_Game19 %>% filter(Longitude != "NA")
write.csv(gps_Game19filtered,"/Volumes/GoogleDrive/My Drive/DataFest 2019/MT/MT R/gps_Game19.csv")

gps_Game20 <- gps %>% filter(GameID==20)
summary(gps_Game20)

gps_Game21 <- gps %>% filter(GameID==21)
gps_Game22 <- gps %>% filter(GameID==22)
gps_Game23 <- gps %>% filter(GameID==23)
gps_Game24 <- gps %>% filter(GameID==24)

write.csv(gps_Game24,"/Volumes/GoogleDrive/My Drive/DataFest 2019/MT/MT R/gps_Game24.csv")
gps_Game25 <- gps %>% filter(GameID==25)
gps_Game26 <- gps %>% filter(GameID==26)
gps_Game27 <- gps %>% filter(GameID==27)
gps_Game28 <- gps %>% filter(GameID==28)
gps_Game29 <- gps %>% filter(GameID==29)
gps_Game30 <- gps %>% filter(GameID==30)
gps_Game31 <- gps %>% filter(GameID==31)
gps_Game32 <- gps %>% filter(GameID==32)
gps_Game33 <- gps %>% filter(GameID==33)
gps_Game34 <- gps %>% filter(GameID==34)
gps_Game35 <- gps %>% filter(GameID==35)
gps_Game36 <- gps %>% filter(GameID==36)
gps_Game37 <- gps %>% filter(GameID==37)
gps_Game38 <- gps %>% filter(GameID==38)

for (gameID in 1:38) {
  test <- gps %>% filter(GameID==gameID) %>% select(-FrameID, -Time)
  print(unique(test$PlayerID))
}

# speed vs frame. What happened after frame 2000?
ggplot(gps_Game1_Player2, aes(x=FrameID, y=Speed)) + 
  geom_point() +
  geom_smooth()

gps_Game1_Player3 <- gps %>% filter(GameID==1, PlayerID==3)
ggplot(gps_Game1_Player3, aes(x=FrameID, y=Speed)) + 
  geom_point() +
  geom_smooth()

# obtain window frame graph of each player
# ggplot(gps, aes(x=FrameID, y=Speed)) +
#   geom_point()

gps_Game1_Player4 <- gps %>% filter(GameID==1, PlayerID==4)

#Caleb asked for this:
write.csv(gps_Game1_Player4, file = "/Volumes/GoogleDrive/My Drive/DataFest 2019/MT/MT R/gps_Game1_Player4.csv")






# Trying to match playerID with the first 3 games.
# Roster data from: https://www.world.rugby/sevens-series/stage/1888/match#match-26710

gamesAll<-read.csv("/Volumes/GoogleDrive/My Drive/DataFest 2019/MT/MT Excel Sheets/GameID1-3.csv", na.strings = "-")

game1 <- games13 %>% select(Name, Age, Weight..kg.,height..Cm.,GameID.1)
game2 <- games13 %>% select(Name, Age, Weight..kg.,height..Cm.,GameID.2)
game3 <- games13 %>% select(Name, Age, Weight..kg.,height..Cm.,GameID.3)
games123 <- games13 %>% select(Name, Age, Weight..kg.,height..Cm.,GameID.1,GameID.2,GameID.3)

# filtered_gamesAll <- gamesAll %>% filter()
# filtered_gamesAll <- gamesAll[which(gamesAll$Name != "FANCY CHAVEZ" 
                                    # || gamesAll$Name != "KENDRA COUSINEAU" 
                                    # || gamesAll$Name != "BETHANY CUDMORE" 
                                    # || gamesAll$Name != "OLIVIADE COUVREUR"), ]


filtered_GamesAll<- gamesAll %>% select(Name, Age, Weight..kg.,height..Cm.,GameID.1:GameID.38)

# gamesbyPlayer1 <- c(11:38)
# gamesbyPlayer2 <- c(1:38)
# gamesbyPlayer3 <- c(1:16,29:38)
# gamesbyPlayer4 <- c(1:17, 19:38)
# gamesbyPlayer5 <- c(11:38)
# gamesbyPlayer6 <- c(1:5)
# gamesbyPlayer7 <- c(1:14,19:38)
# gamesbyPlayer8 <- c(1:34)
# gamesbyPlayer9 <- c(1:10)
# gamesbyPlayer10 <- c(1:18, 20,21,25,26,35:38)
# gamesbyPlayer11 <- c(1:38)
# gamesbyPlayer12 <- c(1:28)
# gamesbyPlayer13 <- c(1:38)
# gamesbyPlayer14 <- c(4, 6:10, 15:18, 29:34, 35:38)



# create gps dataset that records if players started during start of game time
library(dplyr)
gps_startingPlayers <- gps %>% select(-FrameID, -Time) %>%
                      group_by(PlayerID, GameID, Half) %>% 
                      filter(Half==1, GameClock %in% times2 ) %>%
                      summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_startingPlayers2 <- gps_startingPlayers %>% filter(maxSpeed >1)
                      
                   
times <- c("00:00:00", "00:00:01", "00:00:02", "00:00:03", "00:00:04", "00:00:05", "00:00:06",
           "00:00:07", "00:00:08", "00:00:09", "00:00:10", "00:00:11", "00:00:12", "00:00:13",
           "00:00:14", "00:00:15", "00:00:16", "00:00:17", "00:00:18", "00:00:19", "00:00:20",
           "00:00:21", "00:00:22", "00:00:23", "00:00:24", "00:00:25", "00:00:26", "00:00:27", "00:00:28", "00:00:29", "00:00:30", "00:00:31", "00:00:32", "00:00:33", "00:00:34", "00:00:35", "00:00:36", "00:00:37", "00:00:38", "00:00:39", "00:00:40", "00:00:41", "00:00:42", "00:00:43", "00:00:44", "00:00:45", "00:00:46", "00:00:47", "00:00:48", "00:00:49", "00:00:50", "00:00:51", "00:00:52", "00:00:53", "00:00:54", "00:00:55", "00:00:56", "00:00:57", "00:00:58", "00:00:59", "00:01:00", "00:01:01", "00:01:02", "00:01:03", "00:01:04", "00:01:05", "00:01:06", "00:01:07", "00:01:08", "00:01:09", "00:01:10", "00:01:11", "00:01:12", "00:01:13", "00:01:14", "00:01:15", "00:01:16", "00:01:17", "00:01:18", "00:01:19", "00:01:20", "00:01:21", "00:01:22", "00:01:23", "00:01:24", "00:01:25", "00:01:26", "00:01:27", "00:01:28", "00:01:29", "00:01:30", "00:01:31", "00:01:32", "00:01:33", "00:01:34", "00:01:35", "00:01:36", "00:01:37", "00:01:38", "00:01:39", "00:01:40", "00:01:41", "00:01:42", "00:01:43", "00:01:44", "00:01:45", "00:01:46", "00:01:47", "00:01:48", "00:01:49", "00:01:50", "00:01:51", "00:01:52", "00:01:53", "00:01:54", "00:01:55", "00:01:56", "00:01:57", "00:01:58", "00:01:59", "00:02:00")

times3 <- c("00:00:00", "00:00:01", "00:00:02", "00:00:03", "00:00:04", "00:00:05", "00:00:06",
           "00:00:07", "00:00:08", "00:00:09", "00:00:10", "00:00:11", "00:00:12", "00:00:13",
           "00:00:14", "00:00:15", "00:00:16", "00:00:17", "00:00:18", "00:00:19", "00:00:20",
           "00:00:21", "00:00:22", "00:00:23", "00:00:24", "00:00:25", "00:00:26", "00:00:27", "00:00:28", "00:00:29", "00:00:30", "00:00:31", "00:00:32", "00:00:33", "00:00:34", "00:00:35", "00:00:36", "00:00:37", "00:00:38", "00:00:39", "00:00:40", "00:00:41", "00:00:42", "00:00:43", "00:00:44", "00:00:45", "00:00:46", "00:00:47", "00:00:48", "00:00:49", "00:00:50", "00:00:51", "00:00:52", "00:00:53", "00:00:54", "00:00:55", "00:00:56", "00:00:57", "00:00:58", "00:00:59", "00:01:00")

times4 <- c("00:00:00", "00:00:01", "00:00:02", "00:00:03", "00:00:04", "00:00:05", "00:00:06",
            "00:00:07", "00:00:08", "00:00:09", "00:00:10", "00:00:11", "00:00:12", "00:00:13",
            "00:00:14", "00:00:15", "00:00:16", "00:00:17", "00:00:18", "00:00:19", "00:00:20",
            "00:00:21", "00:00:22", "00:00:23", "00:00:24", "00:00:25", "00:00:26", "00:00:27", 
            "00:00:28", "00:00:29", "00:00:30")

#1
gps_Game1_Players <- gps %>% filter(GameID==1) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times4) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game1StartingPlayers <- gps_Game1_Players %>% filter(avgSpeed > 2)

#2
gps_Game2_Players <- gps %>% filter(GameID==2) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times4) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game2StartingPlayers <- gps_Game2_Players %>% filter(maxSpeed > 2)

#3
gps_Game3_Players <- gps %>% filter(GameID==3) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times4) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game3StartingPlayers <- gps_Game3_Players %>% filter(maxSpeed > 2)

#4
gps_Game4_Players <- gps %>% filter(GameID==4) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times4) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game4StartingPlayers <- gps_Game4_Players %>% filter(maxSpeed > 2)

#5
gps_Game5_Players <- gps %>% filter(GameID==5) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times4) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game5StartingPlayers <- gps_Game5_Players %>% filter(maxSpeed > 2)

#6
gps_Game6_Players <- gps %>% filter(GameID==6) %>% select(-FrameID, -Time) %>%
group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game6StartingPlayers <- gps_Game6_Players %>% filter(maxSpeed > 2)

#7
gps_Game7_Players <- gps %>% filter(GameID==7) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game7StartingPlayers <- gps_Game7_Players %>% filter(maxSpeed > 2)

#8
gps_Game8_Players <- gps %>% filter(GameID==8) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game8StartingPlayers <- gps_Game8_Players %>% filter(maxSpeed > 2)

#9 ----- ###HERE'S GAME 9 STARTERS (8 players)
gps_Game9_Players <- gps %>% filter(GameID==9) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game9StartingPlayers <- gps_Game9_Players %>% filter(maxSpeed >2)

#10
gps_Game10_Players <- gps %>% filter(GameID==10) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game10StartingPlayers <- gps_Game10_Players %>% filter(maxSpeed >2)

#11
gps_Game11_Players <- gps %>% filter(GameID==11) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game11StartingPlayers <- gps_Game11_Players %>% filter(maxSpeed >2)

#24
gps_Game24_Players <- gps %>% filter(GameID==24) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID, GameID, Half) %>%
  filter(Half==1, GameClock %in% times4) %>% 
  summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))
gps_Game24StartingPlayers <- gps_Game24_Players %>% filter(maxSpeed >2)



gps_Game9_AllPlayers <- gps %>% filter(GameID==9) %>% select(-FrameID, -Time) %>%
  group_by(PlayerID) %>%
  summarise(avgPlayerSpeed=mean())
  #summarise(avgSpeed=mean(Speed), maxSpeed=max(Speed))



