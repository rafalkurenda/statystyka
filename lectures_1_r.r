#ZAD 1

data <- read.csv("data/napoje_po_reklamie.csv",sep=";")

print("WSZYSTKIE: ")
print(summary(data[2:8]))

#ZAD 2

pepsi <- data[['pepsi']]
fanta <- data[['cola']]

print("PEPSI: ")
print(summary(pepsi))
print("FANTA: ")
print(summary(fanta))

#ZAD 3

wzr_csv <- read.csv("data/Wzrost.csv", header = FALSE, sep=",")

data_wzr <- as.numeric(wzr_csv[1,])

print("WZROST: ")
print(mean(data_wzr))
print(sd(data_wzr))
print(mad(data_wzr))
print(var(data_wzr))
print(min(data_wzr))
print(max(data_wzr))