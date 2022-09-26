# print("hello world")

#print("Hello my name is Raj")

#Ctemp = 38.4
#Ftemp = (Ctemp * 1.8) + 32
#print(Ctemp)
#print(Ftemp)

runs = 48426
battedtimes = 1014
notout = 162
matches = 609
battingavg = runs / (battedtimes - 162)
print(round(battingavg,2))



g1 = 113
g2 = 175
g3 = 12
total = g1 + g2 + g3
leftovergroup = total % 24
fullgroup = (total - (total % 24)) / 24
print(fullgroup, "full groups")
print(leftovergroup, "students left over")