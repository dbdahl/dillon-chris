library(lme4)
library(broom.mixed)
library(knitr)

d <- read.csv("2cmPlieData.csv")

# Make sure the variables are factors
d$Date <- factor(d$Date)
d$Dancer <- factor(d$Dancer)
d$Trial <- factor(d$Trial)
d$Rep <- factor(d$Rep)

# Interaction term to create nesting identifier for Trial
d$TrialID <- interaction(d$Date, d$Dancer, d$Trial, drop = TRUE)
d$RepID <- interaction(d$TrialID, d$Rep, drop = TRUE)

# Problematic data as itentified by Rebecca Mecham.
d2 <- d[!(d$Date == '03/27/25' & d$Dancer == 2), ]

# Model with crossed Date and Dancer, nested Trial and Rep
fm1 <- lmer(Slope ~ 1 + (1 | Date) + (1 | Dancer) + (1 | TrialID), data = d2)
summary(fm1)

fm2 <- lmer(WaveSpeed_Ratio ~ 1 + (1 | Date) + (1 | Dancer) + (1 | TrialID), data = d2)
summary(fm2)

